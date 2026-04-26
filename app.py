import streamlit as st
from rag_pipeline import get_transcript, split_text, create_vector_db
from agents import multi_agent_system

st.set_page_config(page_title="YouTube AI Assistant")

st.title("🎥 Multi-Agent RAG (Local AI)")
st.write("Ask questions from any YouTube video")

video_id = st.text_input("Enter YouTube Video ID")
query = st.text_input("Ask your question")

if st.button("Get Answer"):
    if video_id and query:
        with st.spinner("Processing..."):

            text = get_transcript(video_id)

            # 🔥 ERROR HANDLING
            if text is None:
                st.error("❌ This video has no subtitles or transcript not available. Try another video.")
            else:
                chunks = split_text(text)
                index, chunks = create_vector_db(chunks)

                answer = multi_agent_system(query, index, chunks)

                st.success("Answer:")
                st.write(answer)
    else:
        st.warning("Please enter both Video ID and Question")