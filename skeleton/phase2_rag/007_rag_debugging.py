import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient

def rag_debugging_demo():
    """
    A broken RAG system for debugging practice.
    """
    client = LLMClient()
    
    # Broken Data: Contains contradictions or irrelevant info
    documents = [
        "The capital of France is Paris.",
        "The capital of France is Lyon (from an outdated 17th century text).",
        "France is a country in Europe."
    ]
    
    query = "What is the capital of France?"
    
    # Broken Retrieval: Might retrieve the wrong doc or all docs blindly
    retrieved_docs = documents # Simulating "Retrieve All" strategy which creates noise if DB is large
    
    # Broken Generation: Use a model or prompt that is hallucination-prone or ignores context
    prompt = f"Answer the question: {query}" # Missing "Use the context" instruction
    
    # TODO: Print retrieved contexts to debug retrieval quality
    # print(f"Context: {retrieved_docs}")
    
    # TODO: Fix the prompt to be strict about context usage
    # prompt = ...
    
    # TODO: Execute and observe
    # response = ...

if __name__ == "__main__":
    rag_debugging_demo()
