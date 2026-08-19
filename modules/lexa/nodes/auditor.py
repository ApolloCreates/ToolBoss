import os

from langchain_groq import ChatGroq
from dotenv import load_dotenv

from .librarian import get_vector_db

load_dotenv()

# 1. Setup Paths (Same logic as Librarian)


def audit_claim(case_details):
    print(f"--- ⚖️ AUDITOR: ANALYZING COMPLIANCE ---")

    vector_db = get_vector_db()

    # 1. Search for rules
    query = f"Policy limits and exclusions for {case_details.incident_type} of {case_details.item_name}"
    relevant_rules = vector_db.similarity_search(query, k=3)
    
    # 2. Extract the text AND the source (page numbers if available)
    context = ""
    sources = []
    for doc in relevant_rules:
        context += f"\n{doc.page_content}"
        # Grab the page number from the PDF metadata
        page = doc.metadata.get("page", "Unknown")
        sources.append(f"Page {page}: {doc.page_content[:100]}...")

    # 3. Reasoning Phase
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
    prompt = f"Using this policy text: {context}\n\nAnalyze this claim: {case_details}. Provide a verdict and cite specific rules."
    
    response = llm.invoke(prompt)
    
    # Return BOTH the verdict and the raw sources
    return {"verdict": response.content, "sources": sources}