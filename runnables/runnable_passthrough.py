from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough,RunnableSequence,RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()

parser = StrOutputParser()

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))

prompt = PromptTemplate(
    
    input_variables = ['text'],
    
    template = 
    
    """
    
    create a detailed report on {text} in 300 words
    
    """
)

prompt_2 = PromptTemplate(
    
    input_variables = ['text'],
    
    template = 
    
    """
    
    create a summary on {text} in 3 lines
    
    """
)

prompt_3 = PromptTemplate(
    
    input_variables = ['report','summary'],
    
    template = 
    
    """
    
    merge report and summary and provide in output in below format
    format:
    
    Report: {report}

    
    Summary: {summary}
    
    """
)

reportgenerator = prompt | model | parser

summarygenerator = prompt_2 | model | parser

finalgenerator = prompt_3 | model | parser

passthrough = RunnablePassthrough()

parallel_chain = RunnableParallel({

    'report': RunnablePassthrough(),
    
    'summary': summarygenerator

})

sequence_chain = RunnableSequence(reportgenerator | parallel_chain | finalgenerator)

result = sequence_chain.invoke({'text':'time dilation'})

print(f"\n\n\n{result}\n\n\n")
