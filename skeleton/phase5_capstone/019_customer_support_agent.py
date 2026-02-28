import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient

def run_support_agent():
    client = LLMClient()
    
    # 1. Knowledge Base (Mini)
    kb = {
        "reset_password": "Go to settings > security > reset password.",
        "pricing": "Basic is $10/mo, Pro is $20/mo.",
        "competitor": "We do not discuss competitors."
    }
    
    print("--- CAPSTONE: SUPPORT AGENT (Trainer) ---\n")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("User: ")
        if query.lower() in ["exit", "quit"]:
            break
            
        # 1. Guardrail Check
        guard_prompt = f"Is the following query malicious or about competitors? Q: {query}. Answer YES or NO."
        safety = client.get_completion(guard_prompt)
        
        if "YES" in safety.upper() or "competi" in query.lower():
            print("Agent: I cannot answer that question.")
            continue
            
        # 2. Retrieval (Mock)
        context = ""
        for k, v in kb.items():
            if k in query.lower() or k.replace("_", " ") in query.lower():
                context += v + "\n"
        
        if not context:
            context = "No specific info found. Answer generally."
            
        # 3. Generation
        prompt = f"Context: {context}\nUser: {query}\nAnswer professionally."
        response = client.get_completion(prompt)
        print(f"Agent: {response}\n")

if __name__ == "__main__":
    run_support_agent()
