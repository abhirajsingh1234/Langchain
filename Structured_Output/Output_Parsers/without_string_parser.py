from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.output_parsers import StringOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

prompt_1 = PromptTemplate(
    input_variables = ['topic'],
    template = """create a detailed report on {topic} in 300 words"""
)
prompt_2 = PromptTemplate(
    input_variables = ['text'],
    template = """create a summary on {text} in 3 lines"""
)

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))

result = prompt_1.invoke({'topic':'time dilation'})
response = model.invoke(result)
print(f"\n\n\n{response.content}\n\n\n")

result = prompt_2.invoke({'text':response.content})
response2 = model.invoke(result)
print(response2.content)
