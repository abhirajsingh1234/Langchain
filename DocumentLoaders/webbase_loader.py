from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

loader = WebBaseLoader(

    web_path = 'https://github.com/abhirajsingh1234?tab=repositories'

)

documents = loader.load()

print(f"type of documents: {type(documents)}\n\n")

print(f"length of pages fetched: {len(documents)}\n\n")

# print(f"content of object: {documents[0].page_content}\n\n")

print(f"metadata of object: {documents[0].metadata}\n\n")

prompt = PromptTemplate(
    
    input_variables = ['question'],

    partial_variables = {'text': documents[0].page_content},

    template = 

    """

    analyze the following github repositories data of user.

    answer the user question on the basis of the data provided.

    answer should be properly formatted.

    data: {text}

    question: {question}

    """

)

llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))

chain = prompt | llm

response = chain.invoke({'question':'what is the name of the repositories available?'})

print(response.content)

print(type(response))