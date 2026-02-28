import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient

def demonstrate_action_vs_description():
    """
    Show how an LLM describes what it *would* do, rather than doing it.
    """
    client = LLMClient()
    
    print("--- ACTION vs DESCRIPTION DEMO ---\n")
    
    prompt = "Check the current weather in Tokyo and tell me if I should wear a coat."
    
    print(f"User: {prompt}\n")
    response = client.get_completion(prompt)
    
    print(f"LLM Response:\n{response}\n")

    # 1. Weather Request
    prompt_1 = "Why didn't you check the current weather in Tokyo?"
    print(f"Goal 1: {prompt_1}")
    
    print("Executing...")
    response_1 = client.get_completion(prompt_1)
    
    print(f"LLM Response:\n{response_1}\n")
    print("ANALYSIS: Without tools, the LLM is just a text generator. It can describe checking weather, or refuse, but it cannot *act*.")
    print("-" * 50 + "\n")
    
    # 2. Email Request
    email_target = "boss@company.com"
    prompt_2 = f"Send an email to {email_target} saying I'll be late."
    print(f"Goal 2: {prompt_2}")
    
    print("Executing...")
    response_2 = client.get_completion(prompt_2)
    
    print(f"LLM Response:\n{response_2}\n")
    print("ANALYSIS: It generated the *text* of an email, but no email was sent. This is the core limitation agents solve.")

if __name__ == "__main__":
    demonstrate_action_vs_description()
