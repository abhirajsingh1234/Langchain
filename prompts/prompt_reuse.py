


# # to save prompt template


# from langchain_core.prompts import PromptTemplate
# list = ['AAdhar', 'Voter ID', 'PAN', 'electricity bill']

# template=PromptTemplate(
#     template="""
#     user question only contain queries related to which indian document it is according to given data in question.
#     answer only with one word.
#     document is going to be one of the following: {list}



# **Question:** {question}
# output json format: {{
#         "document": "..."
#     }}
# """,
#     input_variables=['question', 'list'],
    
# )
# template.save('template.json')


# to load prompt template

from langchain_core.prompts import load_prompt
from langchain_ollama import ChatOllama

model = ChatOllama(model='llama3.2')
list = ['AAdhar', 'Voter ID', 'PAN', 'electricity bill']
string_list = ', '.join(list)
template=load_prompt('template.json')

chain = template | model
response = chain.invoke({
    "question": "which document contains number like 1111 1111 1111",

})
print(response.content)