from langchain_community.retrievers import WikipediaRetriever

result = WikipediaRetriever(top_k_results =2 , lang ='en')

query = 'what is the latest news about the kashmir attack 2024'

docs = result.invoke(query)

for  doc in docs :
     print(doc.page_content)
