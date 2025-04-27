from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

Loader = DirectoryLoader(

    path = 'directory_loader_multiple_pdfs',

    glob = '*.pdf',

    loader_cls = PyPDFLoader,

    show_progress=True,

)

'''
docs is a list of documents objects with page content and metadata
 where all pdf pages either from single pdf or multiple pdfs are in same list
 '''
 
docs = Loader.load()


print(

      f"type of documents: {type(docs)}\n\n"

      f"length of documents(length is equal to number of pages in pdf): {len(docs)}\n\n"

      f"data type of object in list: {type(docs[0])}\n\n"

    #   f"whole data of first object: {docs[0]}\n\n"

      f"content of object: {docs[0].page_content}\n\n"

      f"metadata of object: {docs[0].metadata}\n\n"

      f"content of object: {docs[1].page_content}\n\n"
      
      f"metadata of object: {docs[1].metadata}\n\n"

      )