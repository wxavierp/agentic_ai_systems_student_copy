import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient

def demonstrate_reasoning_failure():
    """
    Demonstrate how LLMs can fail at multi-step reasoning.
    """
    client = LLMClient()
    
    print("--- MULTI-STEP REASONING DEMO ---\n")
    
    logic_puzzle = """
    I have 3 boxes on a table: A, B, and C.
    Initially:
    - Box A has a Red ball.
    - Box B has a Blue ball.
    - Box C has a Green ball.
    
    Perform these operations in order:
    1. Swap contents of A and B.
    2. Move contents of B to C (assume C's current contents are discarded/replaced? Let's say swapped to make it tracking heavy).
       OK, correction: Swap contents of B and C.
    3. Take the ball currently in A and put it in your pocket.
    4. Swap contents of A and C.
    
    Question: What is in Box A, Box B, Box C, and the Pocket at the end?
    """
    
    # Let's trace it manually to be sure:
    # Start: A=Red, B=Blue, C=Green
    # 1. Swap A,B -> A=Blue, B=Red, C=Green
    # 2. Swap B,C -> A=Blue, B=Green, C=Red
    # 3. Pocket A -> A=Empty, Pocket=Blue, B=Green, C=Red
    # 4. Swap A,C -> A=Red, C=Empty, B=Green, Pocket=Blue
    
    ground_truth = "A: Red ball, B: Green ball, C: Empty, Pocket: Blue ball"
    
    print(f"Puzzle: {logic_puzzle}")
    print("..." * 10)
    
    # Attempt 1: Zero-shot direct answer
    print("Attempt 1: Direct Answer (No Chain-of-Thought)")
    prompt_direct = logic_puzzle + "\nProvide only the final answer."
    response_1 = client.get_completion(prompt_direct, temperature=0.1)
    print(f"LLM Response:\n{response_1}\n")
    
    print(f"Ground Truth:\n{ground_truth}\n")
    
    if ground_truth.lower() in response_1.lower() or "blue" in response_1.lower():
         print("Note: Advanced models might get this right even without CoT. If so, try a harder puzzle or lower capability model.")
    else:
         print("ANALYSIS: Without intermediate steps, the model loses track of state.")

    print("-" * 50 + "\n")
    
    # Attempt 2: Chain-of-Thought
    print("Attempt 2: Chain-of-Thought ('Let's think step by step')")
    prompt_cot = logic_puzzle + "\nLet's think step by step."
    response_2 = client.get_completion(prompt_cot, temperature=0.1)
    print(f"LLM Response:\n{response_2}\n")
    
    print("ANALYSIS: Forcing the model to output its reasoning trace (thought items) usually fixes the logic.")

if __name__ == "__main__":
    demonstrate_reasoning_failure()
