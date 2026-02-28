import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient
from utils.tracer import SimpleTracer

def json_tracing_demo():
    """
    Demonstrate structured JSON tracing.
    """
    # TODO: Initialize Tracer
    # tracer = SimpleTracer("my_trace.json")
    
    client = LLMClient()
    query = "What is 2 + 2?"
    
    # TODO: Log the initial query
    # tracer.log_event("query", {"text": query})
    
    # TODO: Log the LLM call
    # tracer.log_event("llm_start", {"model": "gpt-3.5"})
    
    response = client.get_completion(query)
    
    # TODO: Log the Result
    # tracer.log_event("llm_end", {"response": response})
    
    print(response)
    
    # TODO: Save trace
    # tracer.save()

if __name__ == "__main__":
    json_tracing_demo()
