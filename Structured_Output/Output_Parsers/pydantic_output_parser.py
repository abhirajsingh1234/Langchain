from pydantic import BaseModel,Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))
class base_model(BaseModel):
    name:str = Field(description= 'name of the person')
    age:int = Field(gt=18,description= 'age of the person')
    city:str = Field(description= 'city of the person')

parser = PydanticOutputParser(pydantic_object = base_model)

template = PromptTemplate(
    template ="""
    generate the name age and city of {person}\n dont include any comments\n{format}"""
    ,
    input_variables = ['person'],
    partial_variables= {'format':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'person':'captain america'})
print(result)
print(type(result))

print(template)


prompt_1 = template.format(person = 'captain america')
print(prompt_1)
