from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# Step 1: Define a simple PromptTemplate
prompt_2 = PromptTemplate(template="{query}", input_variables=["query"])

# Step 2: Set up the LLM (e.g., using the Ollama model)
llm = ChatOllama(model="gemma3:4b")

# Step 3: Chain the PromptTemplate with the LLM
chain_2 = prompt_2 | llm

# Step 4: Create a batch of inputs (questions)
batches = [
    {'query': 'What is the capital of France?'},
    {'query': 'Who wrote Hamlet?'},
    {'query': 'What is the square root of 64?'}
]

# Step 5: Use chain.batch() to process the batch of inputs
responses = chain_2.batch(batches)

# Step 6: Print the responses
for idx, response in enumerate(responses):
    print(f"Response {idx + 1}: {response.content}")
