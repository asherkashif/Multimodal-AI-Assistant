from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS 
from app.config import GEMINI_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=GEMINI_API_KEY
)

def create_vector_store(chunks):
    vector_db = FAISS.from_texts(chunks, embeddings)
    
    vector_db.save_local("data/faiss_index")