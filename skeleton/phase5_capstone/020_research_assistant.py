import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient
from utils.tools import web_search

def run_research_assistant():
    client = LLMClient()
    topic = "Impact of Quantum Computing on Cryptography"
    print(f"--- RESEARCH ASSISTANT: {topic} ---\n")
    
    # 1. Planner
    print("[Planner] Generating research questions...")
    plan_prompt = f"Break down '{topic}' into 3 key research questions. Return JSON list of strings."
    plan_resp = client.get_completion(plan_prompt)
    questions = json.loads(plan_resp.replace("```json", "").replace("```", "").strip())
    
    findings = []
    
    # 2. Researcher (Loop)
    for q in questions:
        print(f"[Researcher] Investigating: {q}")
        # search_res = web_search(q) # Mock search
        search_res = f"Mock findings about {q}..."
        
        summary_prompt = f"Summarize these findings: {search_res}"
        summary = client.get_completion(summary_prompt)
        findings.append(f"Q: {q}\nA: {summary}")
        
    # 3. Writer
    print("\n[Writer] Compiling report...")
    context = "\n\n".join(findings)
    report_prompt = f"Write a research report based on:\n{context}"
    report = client.get_completion(report_prompt)
    
    print("\n--- FINAL REPORT ---\n")
    print(report)

if __name__ == "__main__":
    run_research_assistant()
