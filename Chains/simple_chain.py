from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

parser = StrOutputParser()

prompt_1 = PromptTemplate(

    input_variables = ['topic'],

    template = """
    
    create a detailed report on {topic} in 300 words

    """
)

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))


# this is the simple chain 

chain_1 = prompt_1 | model | parser 

result = chain_1.invoke({'topic':'time dilation'})

# print(f"\n\n\n{result}\n\n\n")

chain_1.get_graph().print_ascii()