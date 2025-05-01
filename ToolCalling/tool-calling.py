from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import os
load_dotenv()

@tool
def multiplier(a:int,b:int) ->int:
    """given 2 numbers as input this tool returns their product"""

    print('\n\nmultiplier called\n\n')
    return a * b

res = multiplier.invoke({"a":2, "b":3})

print(res)
print(multiplier.name)
print(multiplier.description)
print(multiplier.args)

model = ChatGoogleGenerativeAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    model = "gemini-2.0-flash-exp"
)

llm_with_tools = model.bind_tools([multiplier])

history = []

query = 'what is the multiplication of 2 and 3' #HumanMessage Object

history.append(HumanMessage(query)) #Adding HumanMessage Object to history

result = llm_with_tools.invoke(query)  #AIMessage Object

history.append(result)

result = multiplier.invoke(result.tool_calls[0])  #ToolMessage Object

history.append(result)          

print(history)  

final_result = llm_with_tools.invoke(history)

print(final_result.content)