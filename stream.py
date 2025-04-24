from langchain_core.runnables import RunnableSequence
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

# 1. Define a prompt template
prompt = ChatPromptTemplate.from_template("Tell me a fun fact about space.")

# 2. Define the LLM (using OpenAI model here)
llm = ChatOllama(model="gemma3:4b")

# 3. Create a chain using RunnableSequence
chain = prompt | llm

batches=[
    {'query':'who is tanjro'},
    {'query':'who is zentizu'}
]


# 4. Use .stream() to get real-time output
# This will print the output as it arrives, token by token.
# for token in chain.stream({}):
#     print(token.content, end='', flush=True)



prompt_2 = PromptTemplate(template="{query}",
                         input_variables=["query"])

chain_2 = prompt_2 | llm

response = chain_2.batch(batches)

for i in response:
    print(i.content)

