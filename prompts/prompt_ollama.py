from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model='llama3.2')
list = ['AAdhar', 'Voter ID', 'PAN', 'electricity bill']

template = PromptTemplate(
    template="""
    user question only contain queries related to which indian document it is according to given data in question.
    answer only with one word.
    document is going to be one of the following: {list}

    **Question:** {question}
    output json format: {{
        "document": "name of the document"
    }}

            """,
    input_variables=['list', 'question'],
 )

prompt = template.invoke({
    "list": list,
    "question": "which document contains number like 1111 1111 1111"
})
result = model.invoke(prompt)
print(result.content)
