from langchain.tools import StructuredTool
from pydantic import Field,BaseModel

class inputs(BaseModel):

    a:int = Field(required=True,Description = "first number")

    b:int = Field(required =True , Description = "Second number")

def multiply(a:int,b:int) -> int:

    """multiply 2 numbers"""

    return a * b

tool = StructuredTool(

    func = multiply,

    name = 'multiply',

    description = "multiply 2 numbers",

    args_schema = inputs

)

print(tool.invoke({'a':1,'b':3}))