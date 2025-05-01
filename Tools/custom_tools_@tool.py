from langchain_core.tools import tool

'''creating  a custom tool is a 3 step process
        1) create a defination with your custom input,logic and output.
           the function should have a docstring for llm to understand 
           behaviour of your function.

        2)type hint input and output data.
           eg(a:int :- 'a' input is going to be an integer)

        3)use tool decorator to wrap your function.

        '''

@tool
def adder(a:int ,b:int) -> int:

    """ add's 2 number"""

    return a + b

result = adder.invoke({'a':1,'b':3})

print(
    f"Result : {result}\n"

    f"description: {adder.description}\n"   #description of the tool

    f"name: {adder.name}\n"     #name of the tool

    f"args: {adder.args}\n"     #args of the tool

    f"data passed to LLM: {adder.args_schema.model_json_schema()}\n"   #data passed to LLM

      )




