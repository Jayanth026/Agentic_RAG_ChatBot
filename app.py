import streamlit as st
import uuid
import os
from dotenv import load_dotenv
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

load_dotenv()

st.set_page_config(page_title="Agentic RAG Chatbot",layout="wide")
st.title("Agentic RAG Chatbot for Document QA")

uploaded_files = st.file_uploader("Upload documents(PDF, PPTX, DOCX, CSV, TXT)",accept_multiple_files=True)
question=st.text_input("Ask a question about your documents")

if "coordinator" not in st.session_state:
    st.session_state.coordinator={
        "ingestion":IngestionAgent(),
        "retrieval":RetrievalAgent(),
        "llm":LLMResponseAgent(os.getenv("openai_key"))}

if st.button("Get Answer") and uploaded_files and question:
    trace_id=str(uuid.uuid4())
    files={file.name: file for file in uploaded_files}

    ingest_msg=st.session_state.coordinator["ingestion"].process(files,trace_id)
    all_docs=ingest_msg['payload']['all_docs']

    st.session_state.coordinator["retrieval"].build_index(all_docs)
    retrieval_msg=st.session_state.coordinator["retrieval"].retrieve(question,trace_id)

    unique_chunks=list(dict.fromkeys(retrieval_msg['payload']['retrieved_context']))
    retrieval_msg['payload']['retrieved_context']=unique_chunks

    answer=st.session_state.coordinator["llm"].answer(retrieval_msg['payload'],trace_id)

    st.markdown("### Answer")
    st.success(answer)
