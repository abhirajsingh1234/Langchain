import os
import pickle
from typing import Dict, Set, List,TypedDict
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from pydantic import BaseModel,Field
from langgraph.graph import StateGraph,END,START
from langchain_core.retrievers import BaseRetriever
from langchain_core.messages import HumanMessage
from langchain.retrievers.multi_query import MultiQueryRetriever
from prompt import multiquery_or_ambigious_system_prompt,retrieval_argumented_generation_system_prompt, category_classification_system_prompt,multiquery_splitter_system_prompt


#SCHEMAS

class MultiQueryOutput(BaseModel):
    multiple_queries: List[str] = Field(description="List of individual queries derived from the input multiquery.")

class collection_classification(BaseModel):
    collection_name : str  = Field(description = f'contain value from one of the defined category which is relatable to query') 

class multi_or_ambigious_classification(BaseModel):
    query_identification : str  = Field(description = f"contain value from one of the following : ['AMBIGIOUS', 'MULTIQUERY', 'NORMAL']") 

class RAG_State(TypedDict):
    input : str
    output : str

llm = ChatOpenAI(model='gpt-4o-mini', api_key='')

class DummyRetriever(BaseRetriever):
    def get_relevant_documents(self, query): return []
    async def aget_relevant_documents(self, query): return []

mqr = MultiQueryRetriever.from_llm(retriever=DummyRetriever(), llm=llm)

# ---------------- CONFIG ---------------- #
BASE_DIR = "./collections"     # put subfolders here (each subfolder = one collection)
INDEX_DIR = "./faiss_indexes"  # where per-collection FAISS indexes will be saved
EMBEDDINGS = OpenAIEmbeddings(model='text-embedding-3-small', api_key="")
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
# ---------------------------------------- #
