from langchain_community.document_loaders import TextLoader

#loader is an object of TextLoader
loader = TextLoader('text.txt')

#loader object has a load method that loads the text file into a list of documents objects with page content and metadata
documents = loader.load()

print(
      f"type of documents: {type(documents)}\n"
      f"data type of object in list: {type(documents[0])}\n"
      f"length of documents: {len(documents)}\n"
      f"content of object: {documents[0].page_content}\n"
      f"metadata of object: {documents[0].metadata}\n"
      )
          