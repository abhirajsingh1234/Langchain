from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large',dimension=36)

docs = ['hello world', 'how are you', 'how are you doing?']
result = embedding.embed_documents(docs)
print(result)