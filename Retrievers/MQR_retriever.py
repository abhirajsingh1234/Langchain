
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.retrievers import MultiQueryRetriever
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

docs = [

    Document(page_content = 'my name is abhiraj'),

    Document(page_content = ' my name is abhiraj singh'),

    Document(page_content = 'my name is piyush'),

    Document(page_content = 'my name given by my nana is piyush'),

    Document(page_content = 'why  was karna named sutputra'),
]

model = OllamaEmbeddings(model = 'nomic-embed-text:latest')

llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))

vector_store = FAISS.from_documents(

    documents = docs,

    embedding = model

)

retriever = vector_store.as_retriever(

    search_kwargs = {'k': 2,'lambda_mult':0.5},

    search_type = 'similarity'

)

multiquery_retriever = MultiQueryRetriever.from_llm(

    retriever = retriever,

    llm = llm
)

result = multiquery_retriever.invoke('name')

for res in result:

    print(res.page_content)