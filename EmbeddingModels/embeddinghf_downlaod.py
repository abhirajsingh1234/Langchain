from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name= 'sentence-transformers/all-MiniLM-L6-v2')

result = embedding.embed_query('hello world')
print(result)

result = embedding.embed_documents(['hello world', 'how are you', 'how are you doing?'])
print(result)
