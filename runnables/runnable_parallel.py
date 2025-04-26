from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()

parser = StrOutputParser()

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))

prompt1 = PromptTemplate(
    
    input_variables = ['text'],
    
    template = 
    
    """
    create a format report on {text} in 50 words
    
    """
)

prompt2 = PromptTemplate(
    
    input_variables = ['text'],
    
    template = 
    
    """
    create a quote on {text} 
    
    """
)

prompt3 = PromptTemplate(
    
    input_variables = ['report','quote'],
    
    template = 
    
    """
    merge the report {report} and quote {quote} into a single document. 
    
    """
)

chain = RunnableParallel(
    {'report': prompt1 | model |parser,
    'quote': prompt2 | model | parser}
)

chain3 = prompt3 | model | parser


final_chain = chain | chain3

result = final_chain.invoke({'text':'time dilation'})

print(f"\n\n\n{result}\n\n\n")


