from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader('text.txt')

documents = loader.load()

text = ''

for doc in documents:
    text += f'{doc.page_content}\n'

splitter = CharacterTextSplitter(

    chunk_size = 100,

    chunk_overlap = 20,

    separator = ''   # Default separator is space.
)

result_list = splitter.split_text(text)

print(result_list)

print(len(result_list))