# multi-agent-rag-local-ai
Multi-Agent RAG system that answers questions from YouTube videos using local AI (FAISS, Whisper, Ollama) without API keys.

# 🎥 Multi-Agent RAG (Local AI)

A powerful **Multi-Agent Retrieval-Augmented Generation (RAG)** system that allows you to **ask questions from any YouTube video** using **local AI models** — no API keys required.

---

## 🚀 Features

* 🔍 Ask questions from any YouTube video
* 🧠 Multi-Agent system (Retriever + Generator)
* 🎤 Automatic transcript extraction
* 🔄 Whisper fallback for videos without subtitles
* ⚡ Fast semantic search using FAISS
* 🤖 Local LLM (Llama3 via Ollama)
* 🔐 100% local — no API keys needed

---

## 🧠 How It Works

### 1️⃣ Input

* Enter YouTube Video ID
* Ask any question

### 2️⃣ Transcript Extraction

* Uses **YouTube Transcript API**
* If not available → falls back to **Whisper (Speech-to-Text)**

### 3️⃣ Text Processing

* Splits transcript into chunks
* Converts text into embeddings

### 4️⃣ Vector Search (FAISS)

* Stores embeddings in vector database
* Retrieves most relevant chunks

### 5️⃣ Answer Generation

* Uses **Llama3 (via Ollama)**
* Generates final answer based on context

---

## 🏗️ Tech Stack

* **Frontend:** Streamlit
* **Embedding Model:** Sentence Transformers
* **Vector DB:** FAISS
* **Transcript:** youtube-transcript-api
* **Speech-to-Text:** OpenAI Whisper
* **LLM:** Ollama (Llama3)
* **Downloader:** yt-dlp

---

## 📂 Project Structure

```
multi-agent-rag-local-ai/
│── app.py              # Streamlit UI
│── rag_pipeline.py     # Data processing + retrieval
│── agents.py           # Multi-agent system (LLM)
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/vaibhav07772/multi-agent-rag-local-ai.git
cd multi-agent-rag-local-ai
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Ollama (for LLM)

Download from: https://ollama.com

Then run:

```bash
ollama run llama3
```

### 4️⃣ Install FFmpeg (IMPORTANT for Whisper)

Download: https://ffmpeg.org/download.html

Add it to system PATH and verify:

```bash
ffmpeg -version
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📌 Usage

1. Copy YouTube Video ID
   Example:

   ```
   https://youtu.be/v00DUIxRX0c → v00DUIxRX0c
   ```

2. Paste in app

3. Ask question

4. Get AI-generated answer 🎉

---

## ⚠️ Limitations

* Some videos may not have transcripts
* Whisper fallback requires **FFmpeg installed**
* CPU-based Whisper is slower
* yt-dlp may fail without proper environment setup

---

## 💡 Future Improvements

* 🌐 Deploy on cloud (Render / Streamlit Cloud)
* 🎨 Better UI/UX
* 📊 Chat history support
* 🔊 Real-time streaming answers
* 📁 Support PDFs + documents (RAG upgrade)

---

## 💼 Use Case

* 🎓 Learning from YouTube videos
* 📚 Quick video summarization
* 🔍 Search inside long videos
* 🤖 AI-powered video assistant

---

## 👨‍💻 Author

**Vaibhav Singh**
Aspiring NLP Engineer 🚀

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🧠 Build something awesome

---

