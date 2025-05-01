from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings


loader  = DirectoryLoader(
    path = 'directory_loader_multiple_pdfs',
    glob = '*.pdf',
    loader_cls = PyPDFLoader,
    show_progress=True,
)
document_list = loader.load()

embedding  = OllamaEmbeddings(model = 'nomic-embed-text:latest')


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 512,
    chunk_overlap = 70
)

data_list = splitter.split_documents(document_list)

vector_store = Chroma.from_documents(

    documents = data_list,
    
    embedding = embedding,

    collection_name = 'chroma_vector_store',

    persist_directory = './chroma_store'
    
)

retriever = vector_store.as_retriever(

    search_type = 'similarity',
    search_kwargs = {'k':3}
)

query = retriever.invoke('what happens at light speed')

for doc in query:
    print(doc.page_content)
