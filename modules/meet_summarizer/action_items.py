import spacy
import re

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_action_items(text: str) -> list:
    """
    Extracts potential action items from text using regex + NLP.
    Args:
        text (str): Transcript
    Returns:
        list: Extracted action item sentences
    """
    doc = nlp(text)
    action_items = []

    for sent in doc.sents:
        if re.search(r"\b(will|need to|should|must|schedule|assign|responsible)\b", sent.text, re.I):
            action_items.append(sent.text.strip())

    return action_items
