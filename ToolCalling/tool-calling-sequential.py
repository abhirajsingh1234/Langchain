from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from dotenv import load_dotenv
import os

load_dotenv()

@tool
def multiplier(a: int, b: int) -> int:
    """Given 2 numbers as input this tool returns their product"""
    return a * b

@tool
def adder(a: int, b: int) -> int:
    """Given 2 numbers as input this tool returns their sum"""
    return a + b

@tool
def divider(a: int, b: int) -> float:
    """Given 2 numbers as input this tool returns their quotient (a/b)"""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Initialize the LLM with your API key
llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    model="gemini-2.0-flash-exp"
)

# Bind all tools to the LLM
tools = [multiplier, adder, divider]
llm_with_tools = llm.bind_tools(tools)

chat_history = []

print("Type 'exit' to end the conversation")
while True:
    query = input("\nEnter your query: ")
    
    if query.lower() == 'exit':
        print("Ending conversation. Goodbye!")
        break

    # Add the human message to chat history
    human_message = HumanMessage(content=query)
    chat_history.append(human_message)
    
    # Get the initial response from the LLM
    result = llm_with_tools.invoke(chat_history)
    chat_history.append(result)
    
    # Check if there are any tool calls
    tool_called = False
    try:
        if hasattr(result, 'tool_calls') and result.tool_calls:
            # Save the assistant's response before tool execution
            assistant_planning = AIMessage(content=result.content)
            
            for tool_call in result.tool_calls:
                print(f"\nTool call detected: {tool_call['name']} with args: {tool_call['args']}")
                
                # Find the appropriate tool and invoke it
                for tool in tools:
                    if tool.name == tool_call['name']:
                        tool_result = tool.invoke(tool_call['args'])
                        print(f"Tool result: {tool_result}")
                        
                        # Add the tool response to chat history
                        tool_message = ToolMessage(
                            content=str(tool_result),
                            name=tool_call['name'],
                            tool_call_id=tool_call['id']
                        )
                        chat_history.append(tool_message)
                        tool_called = True
                        break
            
            # If tools were called, get a new response from the LLM
            if tool_called:
                final_result = llm_with_tools.invoke(chat_history)
                result = final_result  # Update result for later use
    except Exception as e:
        print(f"Error processing tool call: {e}")
    
    # Add the AI response to chat history
    chat_history.append(result)
    # chat_history.append(AIMessage(content="the answer is "))
    
    # Display the final response
    print("\nChat history:")
    for msg in chat_history:

        print('-'*30)
        if isinstance(msg, HumanMessage):
            print(f"\nHuman: {msg.content}")
        elif isinstance(msg, AIMessage):
            print(f"\nAI: {msg.content}")
        elif isinstance(msg, ToolMessage):
            print(f"\nTool call: {msg.content}")
        else:
            print(f"Unknown message type: {msg}")
        print('-'*30)
    print(f"\nFinal response: {result.content}")