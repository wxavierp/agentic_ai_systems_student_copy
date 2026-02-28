import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient

def manual_tracing_agent():
    """
    A simple agent loop that we will debug using manual print tracing.
    """
    client = LLMClient()
    
    query = "What is the capital of France?"
    
    # TODO: Add print statements to trace the execution flow
    # print(f"[TRACE] Starting agent with query: {query}")
    
    # Step 1: Decide tool
    # TODO: Trace the decision
    tool = "search"
    
    # Step 2: Execute tool
    # TODO: Trace the tool input and output
    result = "Paris"
    
    # Step 3: Final Answer
    # TODO: Trace the final output generation
    answer = f"The capital is {result}"
    
    print(answer)

if __name__ == "__main__":
    manual_tracing_agent()
