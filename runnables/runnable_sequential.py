from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
import os

load_dotenv()

parser = StrOutputParser()

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))

prompt1 = PromptTemplate(
    
    input_variables = ['topic'],
    
    template = 
    
    """
    create a detailed report on {topic} in 300 words
    
    """
)

prompt2 = PromptTemplate(
    
    input_variables = ['text'],
    
    template = 
    
    """
    create a summary on {text} in 3 lines
    
    """
)

chain = RunnableSequence(
    
    prompt1 | model | parser | prompt2 | model | parser
)

result = chain.invoke({'topic':'time dilation'})

print(f"\n\n\n{result}\n\n\n")


