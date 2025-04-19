from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
schema =[
    ResponseSchema(name='character',description = 'name of the character'),
    ResponseSchema(name='age',description = 'integer representing age of the character'),
    ResponseSchema(name='city',description = 'city of the character'),
]
parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    input_variables = ['topic'],
    partial_variables = {'format_instruction': parser.get_format_instructions()},
    template = """who is {topic}?\n dont include any comments\n {format_instruction}"""
)

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))
prompt = template.format(topic = 'thor')
chain = template | model | parser

result = chain.invoke({'topic':'captain america'})
print(result)
print(type(result))

print(prompt)