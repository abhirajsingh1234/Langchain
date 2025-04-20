from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal
import os


load_dotenv()

#feedback format is going to be consistent for all the feedbacks , positive or negative

class feedback_format(BaseModel):

    sentiment:Literal['positive','negative'] = Field(description = 'sentiment of the feedback')

parser2 =PydanticOutputParser(pydantic_object = feedback_format)

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))

parser = StrOutputParser()

feedback = """ i am not happy with the services provided by the company. 
"""

prompt = PromptTemplate(

    input_variables = ['feedback'],

    partial_variables={'format':parser2.get_format_instructions()},

    template = 
    
    """

    classify the sentiment of the following feedback into positive, negative \n"{feedback}\n{format}".
    
    """
)

happy_prompt = PromptTemplate(

    input_variables = ['feedback'],

    template = 
    
    """

    based on the positive feedback '{feedback}' generate a good feedback to customer.
    
    """
)

sad_prompt = PromptTemplate(

    input_variables = ['feedback'],

    template = 
    
    """

    based on the negative feedback '{feedback}' generate a apologetic feedback to customer.
    
    """
)

chain_classifier= prompt | model | parser2

chain_response = chain_classifier.invoke({'feedback':feedback})

print(chain_response.sentiment)

#now we are going to create a chain that will generate a response based on the sentiment of the feedback

happy_chain = happy_prompt | model | parser

sad_chain = sad_prompt | model | parser

branch_chain = RunnableBranch(

    (lambda x:x.sentiment == 'positive',happy_chain),

    (lambda x:x.sentiment == 'negative',sad_chain),

    RunnableLambda(lambda x:x.sentiment == 'null')
    
)

final_chain = chain_classifier | branch_chain

final_chain_response = final_chain.invoke({'feedback':feedback})

print(final_chain_response)

final_chain.get_graph().print_ascii()
