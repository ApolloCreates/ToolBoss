import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. Get the absolute path of this specific file (librarian.py)
current_file_path = os.path.abspath(__file__)

# 2. Go up two levels to reach the 'Lexa' root folder
# app/nodes/librarian.py -> app/nodes/ -> app/ -> Lexa/
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))

# 3. Define absolute paths for data and the database
PDF_PATH = os.path.join(project_root, "data", "policy.pdf")
DB_PATH = os.path.join(project_root, "lexa_db")

def ingest_policy():
    print(f"🔍 Searching for PDF at: {PDF_PATH}")
    
    if not os.path.exists(PDF_PATH):
        print(f"❌ ERROR: File not found at {PDF_PATH}")
        return

    # 1. Load
    loader = PyPDFLoader(PDF_PATH)
    data = loader.load()

    # 2. Split
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(data)
    print(f"✅ Split PDF into {len(chunks)} chunks.")

    # 3. Embed & Store
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    print(f"💾 Saving Vector Database to: {DB_PATH}")
    vector_db = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=DB_PATH
    )
    print("✨ SUCCESS: lexa_db created in the root folder!")
    return vector_db

if __name__ == "__main__":
    ingest_policy()