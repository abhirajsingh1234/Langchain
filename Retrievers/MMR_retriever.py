from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

docs = [

    Document(page_content = 'my name is abhiraj'),

    Document(page_content = ' my name is abhiraj singh'),

    Document(page_content = 'my name is piyush'),

    Document(page_content = 'my name given by my nana is piyush'),

    Document(page_content = 'why  was karna named sutputra')

]

model = OllamaEmbeddings(model = 'nomic-embed-text:latest')

vector_store = FAISS.from_documents(

    documents = docs,

    embedding = model
)

retriever = vector_store.as_retriever(

    search_kwargs = {'k': 2,'lambda_mult':0.5},

    search_type = 'mmr'

)

result = retriever.invoke('what is my name')

for res in result:
    
    print(res.page_content)