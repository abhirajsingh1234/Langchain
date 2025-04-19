from langchain_openai import ChatOpenAI
from typing import Annotated, TypedDict,Literal
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
model = ChatOpenAI(model = 'gpt-4o', openai_api_key = openai_api_key)

class review(TypedDict):
    summary: Annotated[str, "a breif summary"]   # a summary of what a 'summary' means as per user context
    sentiment: str
    rating: Literal[1,2,3,4,5]   # a rating of what a 'rating' means as per user context

structured_model = model.with_structured_output(review)        #'with_structured_output' only works for openai

result = structured_model.invoke("The movie was great!")

print("type:")
print(type(result))
print(result)

    