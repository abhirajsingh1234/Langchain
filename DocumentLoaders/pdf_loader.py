from langchain_community.document_loaders import PyPDFLoader

loader_object = PyPDFLoader('demo_pdf.pdf')

list_of_documents = loader_object.load()

print(

      f"type of documents: {type(list_of_documents)}\n\n"

      f"length of documents(length is equal to number of pages in pdf): {len(list_of_documents)}\n\n"

      f"data type of object in list: {type(list_of_documents[0])}\n\n"

      f"whole data of first object: {list_of_documents[0]}\n\n"

      f"content of object: {list_of_documents[0].page_content}\n\n"
      
      f"metadata of object: {list_of_documents[0].metadata}\n\n"

      )
          