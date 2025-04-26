from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnablePassthrough, RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
import os

load_dotenv()

def splitter(text):
    return len(text.split())

llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'),temperature=0.9)

prompt = PromptTemplate(
    
    input_variables = ['topic'],

    template = 

    """

    create a joke on {topic} topic

    """

)

prompt_2 = PromptTemplate(
    
    input_variables = ['joke','length'],
    
    template = 
    
    """
    
    merge {joke} and {length} into a single document. 

    format:
    
    Joke: {joke}
    
    Length: {length}
    
    """
    
)
jokegenerator = prompt | llm | StrOutputParser()

splitter_chain = RunnableLambda(splitter)

merger_chain = prompt_2 | llm | StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'length': splitter_chain
    }
)

final_chain = RunnableSequence(
    
    jokegenerator | parallel_chain | merger_chain
)

print(final_chain.invoke({'topic':'time dilation'}))




