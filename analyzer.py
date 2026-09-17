import ollama
import yaml
from rag.retriever import search_docs

with open("config.yaml") as f:
    config = yaml.safe_load(f)

MODEL = config["ollama"]["model"]

def analyze(log_text):

    context = search_docs(log_text)

    prompt = f"""
Log:
{log_text}

Context:
{context}

Generate:
1. Severity
2. RCA
3. Resolution
4. Preventive Actions
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
