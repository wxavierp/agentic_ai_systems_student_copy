import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient

def prompt_engineering_demo():
    """
    Demonstrate how different prompt templates affect RAG performance.
    """
    client = LLMClient()
    
    context = """
    Product: SmartWhisk 3000
    Features: 
    - 5-speed control
    - Self-cleaning mode (press button for 3s)
    - Battery life: 2 hours continuous use
    - Warranty: 1 year limited
    - Price: $49.99
    
    Customer Complaint: "My whisk stopped working after 3 months. It won't turn on."
    """
    
    query = "How should the customer service agent respond?"
    
    # Template 1: Basic
    # TODO: Write a simple prompt template
    # prompt1 = ...
    
    # Template 2: Persona-based + Empathy
    # TODO: Write a prompt that adopts a persona ("You are a helpful support agent...")
    # prompt2 = ...
    
    # Template 3: Chain-of-Thought / Structured Output
    # TODO: Ask for reasoning before the final answer
    # prompt3 = ...
    
    # TODO: Test all prompts and compare outputs

if __name__ == "__main__":
    prompt_engineering_demo()
