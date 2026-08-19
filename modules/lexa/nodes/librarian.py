import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


CURRENT_FILE = os.path.abspath(__file__)

# librarian.py
#   ↓ nodes
#   ↓ lexa
#   ↓ modules
#   ↓ ToolBoss
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(CURRENT_FILE)
        )
    )
)

PDF_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "lexa",
    "policy.pdf"
)

DB_PATH = os.path.join(
    PROJECT_ROOT,
    "lexa_db"
)

def ingest_policy():

    print(f"🔍 Searching for PDF at: {PDF_PATH}")

    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError(
            f"Policy PDF not found at: {PDF_PATH}"
        )

    print("📄 Loading policy...")

    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    print(f"📄 Loaded {len(documents)} pages.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(documents)

    print(f"✂️ Created {len(chunks)} chunks.")

    print("🧠 Creating embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    print(f"💾 Creating Chroma database at: {DB_PATH}")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    print("✅ LEXA knowledge base created.")

    return vector_db


def get_vector_db():

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # If database doesn't exist, create it
    if not os.path.exists(DB_PATH):
        print("⚠️ Chroma database not found.")
        print("🚀 Creating LEXA knowledge base...")
        return ingest_policy()

    print("📚 Loading existing LEXA knowledge base...")

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )