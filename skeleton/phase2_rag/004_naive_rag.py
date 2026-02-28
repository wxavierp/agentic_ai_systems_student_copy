import sys
import os
import glob

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient

def naive_rag():
    """
    Implement a naive RAG system that simply concatenates all documents into the context window.
    """
    client = LLMClient()
    
    # 1. Load Documents
    docs_path = os.path.join(os.path.dirname(__file__), "../../data/sample_documents/*.txt")
    documents = []
    # TODO: Glob all text files and read them into the 'documents' list
    
    print(f"Loaded {len(documents)} documents.")
    
    # 2. Concatenate
    # TODO: Join all documents into a single string
    context = ""
    
    # 3. Query
    query = "What is the policy on remote work?"
    
    # TODO: Construct prompt with context
    # prompt = ...
    
    # TODO: Send to LLM
    # response = ...
    # print(response)
    
    # 4. Fail
    # TODO: Add a really long dummy document to 'documents' list to simulate context overflow failure
    # and observe error or truncation.

    # ========================================================================
    # BONUS: Try the same RAG pipeline with a different LLM provider
    # ========================================================================
    # Uncomment to test how different models handle the same context + query.
    # You may notice differences in how models respect context boundaries.
    #
    # --- Using Groq (free, fast inference) ---
    # groq_client = LLMClient(provider="groq")
    # groq_response = groq_client.get_completion(prompt)
    # print(f"\n--- Groq Response ---\n{groq_response}")
    #
    # --- Using Google Gemini (free tier) ---
    # google_client = LLMClient(provider="google")
    # google_response = google_client.get_completion(prompt)
    # print(f"\n--- Google Gemini Response ---\n{google_response}")
    # ========================================================================

if __name__ == "__main__":
    naive_rag()
