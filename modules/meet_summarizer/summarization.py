# modules/summarization.py
import os
os.environ["TRANSFORMERS_BACKEND"] = "pt"  # force PyTorch, skip TF/Keras

from transformers import pipeline

# Load a summarization model fine-tuned for dialogues/meetings
summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum", framework="pt")

def summarize_text(text: str, max_chunk_words=500) -> str:
    words = text.split()
    chunks = [" ".join(words[i:i+max_chunk_words]) for i in range(0, len(words), max_chunk_words)]

    partial_summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=200, min_length=60, do_sample=False)
        partial_summaries.append(summary[0]['summary_text'])

    merged_summary = " ".join(partial_summaries)

    final_summary = summarizer(merged_summary, max_length=250, min_length=80, do_sample=False)
    return final_summary[0]['summary_text']
