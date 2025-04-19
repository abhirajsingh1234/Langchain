from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from dotenv import load_dotenv
import os






print("first way")
'''first way  of passing parsers in prompttemplate to specify model to give json output only'''

load_dotenv()
parser = JsonOutputParser()
prompt_1 = PromptTemplate(
    input_variables = [],
    partial_variables = {'format_instruction':parser.get_format_instructions()},
    template = """give me the name age and city of a marvel movie character.\n dont include any comments \n {format_instruction}"""
)

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))
prompt = prompt_1.format()
chain = prompt_1 | model | parser

result = chain.invoke({})
print(result)
print(type(result))

print(prompt)






print("second way")
'''second way of passing parsers in chatprompttemplate to specify model to give json output only'''

prompt_1 = ChatPromptTemplate([
    ('system','you are a helpful assistant\ndont include any comments\n{format_instruction}'),
    ('user','give me the name age and city of {topic} marvel movie character.')
])

# prompt = prompt_1.format(format_instruction = parser.get_format_instructions())
prompt = prompt_1.invoke(
    {'format_instruction':parser.get_format_instructions(),
                        'topic':'spiderman'
                        })
result = model.invoke(prompt)
parsed_result=parser.parse(result.content)
print(parsed_result)
print(type(parsed_result))






print("third way")
'''third way of passing parsers in chain to specify model to give json output only'''

chain = prompt_1 | model | parser

result = chain.invoke({'format_instruction':parser.get_format_instructions(),
                        'topic':'ironman'})
print(result)
print(type(result))