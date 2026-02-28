import sys
import os

# Add parent directory to path to import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from utils.llm_client import LLMClient

def demonstrate_hallucination():
    """
    Demonstrate how LLMs can hallucinate facts about non-existent things.
    """
    client = LLMClient()
    
    print("--- HALLUCINATION DEMO ---\n")
    
    # 1. Fake Library
    fake_library = "PyGundam-7B"
    prompt = f"Tell me about the {fake_library} python library. What are its main features and how do I install it?"
    
    print(f"Query 1: {prompt}")
    print("..." * 10)
    
    response = client.get_completion(prompt)
    print(f"LLM Response:\n{response}\n")
    
    print("ANALYSIS: The LLM confidently invented a library that doesn't exist, including installation instructions!")
    print("-" * 50 + "\n")

    # 2. Fake Historical Event
    fake_event = "The Great Muffin War of 1892 in London"
    prompt_2 = f"Who won {fake_event} and what were the casualties?"
    
    print(f"Query 2: {prompt_2}")
    print("..." * 10)
    
    response_2 = client.get_completion(prompt_2)
    print(f"LLM Response:\n{response_2}\n")
    
    print("ANALYSIS: Without external grounding (RAG), the model relies on probability, not truth.")

if __name__ == "__main__":
    demonstrate_hallucination()
