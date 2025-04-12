from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
embedding = HuggingFaceEmbeddings(model_name= 'sentence-transformers/all-MiniLM-L6-v2')

def semantic_search(query):

    documents = ['hello world', 'how are you', 'how are you doing?','you are a killer ']
    

    document_embeddings = embedding.embed_documents(documents)
    query_embedding = embedding.embed_query(query)



    similarities = cosine_similarity([query_embedding], document_embeddings)[0]
    index,value=sorted(list(enumerate(similarities)),key= lambda x:x[1])[-1]
    # print(index)  #to see at what index the query is most similar
    # print(value)  #to see the similarity SCORE
    # print(documents[index])  #THE MOST SIMILAR VALUE
    return documents[index]



query = 'the world is full of killers'
data = semantic_search(query)
print(data)

