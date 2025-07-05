from utils.mcp import MCPMessage
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RetrievalAgent:
    def __init__(self):
        self.model=SentenceTransformer('all-MiniLM-L6-v2')
        self.index=None
        self.text_chunks=[]

    def build_index(self,docs):
        self.text_chunks=docs
        embeddings=self.model.encode(docs)
        self.index=faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))

    def retrieve(self,query,trace_id):
        query_vec=self.model.encode([query])
        D,I=self.index.search(np.array(query_vec),k=5)
        top_chunks=[self.text_chunks[i] for i in I[0]]
        return MCPMessage(
            sender="RetrievalAgent",
            receiver="LLMResponseAgent",
            msg_type="RETRIEVAL_RESULT",
            trace_id=trace_id,
            payload={"retrieved_context": top_chunks, "query": query}).get()
