import os
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
import time

load_dotenv()

# 1. Define the "Case File" structure
class ClaimDetails(BaseModel):
    item_name: str = Field(description="The name of the item being claimed")
    incident_type: str = Field(description="Type of incident: theft, accidental damage, fire, etc.")
    value: float = Field(description="The monetary value of the item in local currency")
    location: str = Field(description="The city or specific location of the incident")
    date: str = Field(description="The date the incident occurred")

# 2. Setup the "Structured" LLM

def extract_claim_data(user_input: str):
    # 2026 Gold Standard for Tool Use on Groq
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
    structured_llm = llm.with_structured_output(ClaimDetails)
    
    messages = [
        SystemMessage(content="You are a data extraction engine. Extract the claim details into JSON format. Do not talk to the user."),
        HumanMessage(content=user_input)
    ]

    # Senior Tip: Implement a simple retry for API stability
    for attempt in range(3):
        try:
            print(f"--- 🎤 INTERVIEWER: ATTEMPT {attempt + 1} ---")
            return structured_llm.invoke(messages)
        except Exception as e:
            if attempt == 2: raise e
            time.sleep(1) # Wait a second before retrying

# --- QUICK TEST ---
if __name__ == "__main__":
    test_story = "My MacBook was stolen from my car in Bangalore last Friday. It costs 120000 rupees."
    case = extract_claim_data(test_story)
    print(f"✅ Extracted Case: {case.item_name} | Value: {case.value} | Type: {case.incident_type}")