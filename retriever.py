from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
emb=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db=Chroma(persist_directory="chroma_db",embedding_function=emb)
def search_docs(q):
 return "
".join([d.page_content for d in db.similarity_search(q,k=5)])
