from langchain_core.runnables import RunnableBranch, RunnableSequence, RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
import os

load_dotenv()

class options(BaseModel):
    
    options : Literal['positive','negative'] = Field(description = 'options to choose from')

parser2 = PydanticOutputParser(pydantic_object = options)

llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))

parser = StrOutputParser()

prompt = PromptTemplate(
    
    input_variables = ['text'],
    partial_variables = {'format': parser2.get_format_instructions()},
    
    template = 
    
    """
    
    classify the following feedbact '{text}' into positive and negative

    {format}
    
    """
)

prompt_positive = PromptTemplate(
    
    input_variables = ['text'],
    
    template = 
    
    """
    
    based on the positive feedback '{text}' generate a good feedback to customer in one line.
    
    """
)

prompt_negative = PromptTemplate(
    
    input_variables = ['text'],
    
    template = 
    
    """
    
    based on the negative feedback '{text}' generate a apologetic feedback to customer in one line.
    
    """
)

classifier_chain = prompt | llm 

positive_chain = prompt_positive | llm | parser

negative_chain = prompt_negative | llm | parser

conditional_chain = RunnableBranch(

    (lambda x: True if 'positive' in x.content else False,positive_chain),
    (lambda x: True if 'negative' in x.content else False,negative_chain),
    RunnableLambda(lambda x:True)

)

final_chain = RunnableSequence(

    classifier_chain | conditional_chain | parser
)

print(final_chain.invoke({'text':'i am not happy with the services provided by the company'}))