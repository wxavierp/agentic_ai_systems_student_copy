import sys
import os
import chromadb
from chromadb.utils import embedding_functions

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm_client import LLMClient

def semantic_search_demo():
    """
    Implement semantic search using embeddings and a vector database.
    """
    client = LLMClient()
    
    # 1. Load Documents
    docs_path = os.path.join(os.path.dirname(__file__), "../../data/sample_documents")
    # For this demo, let's manually define some chunks if files aren't read, 
    # but better to read them.
    
    documents = [
        "The quick brown fox jumps over the lazy dog.",
        "A fast auburn vulpine leaps over a slothful canine.",
        "Python is a programming language.",
        "Pythons represent a family of non-venomous snakes.",
        "The weather in London is often rainy."
    ]
    
    print(f"Documents: {len(documents)}")
    
    # 2. Initialize Vector DB (Chroma)
    # TODO: Create a persistent or ephemeral Chroma client
    # chroma_client = ...
    # collection = ...
    
    # 3. Add Documents to Collection
    # TODO: Generate IDs for documents
    # TODO: Add documents to collection (embeddings are handled automatically by Chroma usually, 
    # but here we might want to show manual embedding using our client for learning purposes,
    # or just use Chroma's default.)
    
    # Let's stick to using our LLMClient for embeddings to understand the process.
    # ids = [...]
    # embeddings = [client.get_embedding(doc) for doc in documents]
    
    # TODO: Add to collection with embeddings
    
    # 4. Query
    query = "tell me about snakes"
    # query_embedding = client.get_embedding(query)
    
    # TODO: Query the collection
    # results = ...
    
    # TODO: Print results
    
if __name__ == "__main__":
    semantic_search_demo()
