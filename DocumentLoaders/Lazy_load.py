from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

Loader = DirectoryLoader(

    path = 'directory_loader_multiple_pdfs',

    glob = '*.pdf',

    loader_cls = PyPDFLoader,

    show_progress=True,

)

#lazy load converts document into a generator of documents unlike load which returns a list of documents 
document_lazy = Loader.lazy_load()

print(f"type of document_lazy: {type(document_lazy)}\n\n")

#iterate over the generator and print metadata of each document, consumes less memory power
for doc in document_lazy:
    print(f"content of object: {doc.metadata}\n\n")