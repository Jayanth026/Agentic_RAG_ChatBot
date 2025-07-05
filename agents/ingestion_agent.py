from utils.mcp import MCPMessage
from utils.document_loader import extract_text

class IngestionAgent:
    def __init__(self):
        self.storage = {}

    def process(self,files,trace_id):
        all_texts=[]
        for filename,file in files.items():
            content=extract_text(file,filename)
            self.storage[filename]=content
            all_texts.append(f"{filename}:\n{content}")
        return MCPMessage(
            sender="IngestionAgent",
            receiver="RetrievalAgent",
            msg_type="INGESTION_RESULT",
            trace_id=trace_id,
            payload={"all_docs": all_texts}).get()
