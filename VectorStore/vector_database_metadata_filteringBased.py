
import os
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_ollama import OllamaEmbeddings
from typing import List

CHROMA_DIR = os.getenv("CHROMA_DIR","./_chromadb")
embedding_model = OllamaEmbeddings(model = 'nomic-embed-text:latest')

def extract_data_docx():
    """
    Extracts content from DOCX files in the data_docx folder.
    
    Returns:
        list: List of document chunks with metadata.
    """
    print("Loading DOCX files...")
    
    loader = DirectoryLoader(
        path='data_pdfs',
        glob='*.docx',
        loader_cls=Docx2txtLoader,
        show_progress=True,
    )
    document_list = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=70
    )

    data_list = splitter.split_documents(document_list)
    
    # Add document type to metadata
    for doc in data_list:
        doc.metadata['document_type'] = 'docx'
        doc.metadata['file_name'] = os.path.basename(doc.metadata.get('source', ''))

    return data_list


def store_to_chroma(chunks: List[dict]):
    documents = [
        Document(page_content=c.page_content, metadata=c.metadata)
        for c in chunks
    ]

    Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=CHROMA_DIR,
        
        collection_name="pdf_collection"
    )

    print("Documents successfully embedded and stored in Chroma.")



def retrieve_from_chroma(query: str, filters: dict = None, k: int = 3):
    
    data = extract_data_docx()
    store_to_chroma(data)

    vectorstore = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embedding_model,
        collection_name="pdf_collection"
    )

    results = vectorstore.similarity_search(
        query,
        k=k,
        filter=filters
    )

    results

retrieve_from_chroma(
    "What is the final lending decision?",
    filters={"file_name": "Credit_GPT FAQ.docx"}
)
