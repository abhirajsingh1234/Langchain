from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder  
from langchain_ollama import ChatOllama
from pydantic_core.core_schema import model_field

template = ChatPromptTemplate(
    messages=[
        ('system', 'you are a helpfull chat assistant'),
        MessagesPlaceholder(variable_name = 'chat_history'),
        ('user','{query}')
    ]
)
model = ChatOllama(model = 'llama3.2')
chat_history=[]
with open('db.txt') as f:
    chat_history.extend(f.readlines())

chain = template | model
while True:
    query = input('You: ')
    if query.lower() == 'exit':
        break
    answer = chain.invoke({
        'chat_history': chat_history,
        'query': query
    })
    chat_history.append(f"user: {query}, ")
    chat_history.append(f"assistant: {answer.content}, ")
    print("Assistant:", answer.content)

with open('db.txt', 'w') as f:
    f.writelines([str(item) for item in chat_history])