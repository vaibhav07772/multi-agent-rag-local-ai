import subprocess


def generate_answer(context, question):
    prompt = f"""
You are a helpful AI assistant.

Context:
{context}

Question:
{question}

Answer in a clear and simple way:
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()


def multi_agent_system(query, index, chunks):
    from rag_pipeline import retrieve

    # Agent 1: Retrieve context
    context = retrieve(query, index, chunks)

    # Agent 2: Generate answer
    answer = generate_answer(context, query)

    return answer