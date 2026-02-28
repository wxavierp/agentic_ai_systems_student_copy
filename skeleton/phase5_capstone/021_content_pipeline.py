import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient

def run_content_pipeline():
    client = LLMClient()
    topic = "The Rise of Agentic AI" 
    print(f"--- CONTENT PIPELINE: {topic} ---\n")
    
    # 1. Ideation
    print("Stage 1: Ideation")
    outline = client.get_completion(f"Create a 3-point outline for a blog post about: {topic}")
    print(f"Outline:\n{outline}\n")
    
    # 2. Drafting
    print("Stage 2: Drafting")
    draft = client.get_completion(f"Write a short blog post based on this outline:\n{outline}")
    print(f"Draft (first 100 chars): {draft[:100]}...\n")
    
    # 3. Review (Critique)
    print("Stage 3: Review")
    critique = client.get_completion(f"Critique this draft for clarity and tone. Return only 3 bullet points of feedback.\nDraft:\n{draft}")
    print(f"Feedback:\n{critique}\n")
    
    # 4. Refinement
    print("Stage 4: Refinement")
    final = client.get_completion(f"Rewrite the draft incorporating this feedback:\n{critique}\n\nOriginal Draft:\n{draft}")
    
    print("--- FINAL POST ---\n")
    print(final)

if __name__ == "__main__":
    run_content_pipeline()
