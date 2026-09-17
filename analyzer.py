import ollama
from rag.retriever import search_docs
def analyze(log_text):
 ctx=search_docs(log_text)
 r=ollama.chat(model='llama3.1',messages=[{'role':'user','content':f'Log:{log_text}
Context:{ctx}
Generate RCA and resolution'}])
 return r['message']['content']
