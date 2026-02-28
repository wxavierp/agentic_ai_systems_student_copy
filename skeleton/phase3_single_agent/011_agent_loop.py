import sys
import os
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient
from utils.tools import web_search, calculator

def agent_loop(question, max_iterations=5):
    """
    A simple ReAct agent loop.
    """
    client = LLMClient()
    
    prompt = f"""
    Answer the question using tools: [WEB_SEARCH, CALCULATOR].
    Format:
    Question: {question}
    Thought: ...
    Action: TOOL_NAME
    Action Input: INPUT
    Observation: RESULT
    ...
    Final Answer: RESULT
    
    Begin!
    Question: {question}
    """
    
    history = prompt
    
    for i in range(max_iterations):
        print(f"\n--- Iteration {i+1} ---")
        
        # 1. Generate
        response = client.get_completion(history, stop=["Observation:"])
        print(f"LLM: {response}")
        history += response
        
        # 2. Check for Final Answer
        if "Final Answer:" in response:
            return response.split("Final Answer:")[-1].strip()
            
        # 3. Parse Action
        action_match = re.search(r"Action: (.*)", response)
        input_match = re.search(r"Action Input: (.*)", response)
        
        if action_match and input_match:
            tool = action_match.group(1).strip()
            arg = input_match.group(1).strip()
            
            # 4. Execute
            observation = f"Error: Tool {tool} not found"
            if tool == "WEB_SEARCH":
                observation = web_search(arg)
            elif tool == "CALCULATOR":
                observation = calculator(arg)
                
            print(f"Observation: {observation}")
            
            # 5. Update History
            history += f"\nObservation: {observation}\n"
        else:
            print("No action detected. Ending.")
            break
            
    return "No answer found."

if __name__ == "__main__":
    print(agent_loop("What is the stock price of AAPL doubled?"))
