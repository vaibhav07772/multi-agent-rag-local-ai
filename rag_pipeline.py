from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

import whisper
import yt_dlp
import os

# Load models
model = SentenceTransformer('all-MiniLM-L6-v2')
whisper_model = whisper.load_model("base")


# 🔥 Transcript + Whisper fallback
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([t['text'] for t in transcript])
        print("✅ Used YouTube Transcript")
        return text

    except Exception as e:
        print("⚠️ Transcript failed:", e)
        print("➡️ Using Whisper fallback...")

    try:
        url = f"https://www.youtube.com/watch?v={video_id}"

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'audio.%(ext)s',
            'quiet': False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # 🔍 Find downloaded audio file
        audio_file = None
        for file in os.listdir():
            if file.startswith("audio.") and (
                file.endswith(".webm") or
                file.endswith(".mp4") or
                file.endswith(".m4a")
            ):
                audio_file = file
                break

        print("📁 Downloaded file:", audio_file)

        if audio_file is None:
            print("❌ No audio file found")
            return None

        # 🎤 Whisper transcription
        result = whisper_model.transcribe(audio_file)

        # 🧹 Clean up
        os.remove(audio_file)

        print("✅ Used Whisper")
        return result["text"]

    except Exception as e:
        print("❌ Whisper failed:", e)
        return None


# 🔹 Split text
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_text(text)


# 🔹 Create vector DB
def create_vector_db(chunks):
    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, chunks


# 🔹 Retrieve relevant chunks
def retrieve(query, index, chunks, top_k=3):
    query_vec = model.encode([query])
    query_vec = np.array(query_vec).astype("float32")

    D, I = index.search(query_vec, top_k)
    results = [chunks[i] for i in I[0]]

    return " ".join(results)