import os
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, START, END
from .nodes.interviewer import extract_claim_data
from .nodes.auditor import audit_claim

# 1. Define the "Shared Memory" (State)
class LexaState(TypedDict):
    user_input: str      # The raw story
    case_details: dict   # The structured Pydantic object
    verdict: str         # The final Auditor's report

# 2. Wrap your nodes for the Graph
def node_interviewer(state: LexaState):
    print("--- 🎤 LEXA: STARTING INTAKE ---")
    details = extract_claim_data(state["user_input"])
    return {"case_details": details}

def node_auditor(state: LexaState):
    print("--- ⚖️ LEXA: ANALYZING COMPLIANCE ---")
    report = audit_claim(state["case_details"])
    return {"verdict": report}

# 3. Build the Workflow
workflow = StateGraph(LexaState)

workflow.add_node("interviewer", node_interviewer)
workflow.add_node("auditor", node_auditor)

workflow.add_edge(START, "interviewer")
workflow.add_edge("interviewer", "auditor")
workflow.add_edge("auditor", END)

# Compile the App
lexa_app = workflow.compile()