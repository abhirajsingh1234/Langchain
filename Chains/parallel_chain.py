from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()

text ="""
Title: Understanding Time Dilation in Physics

Introduction
Time dilation is a fundamental concept in Einstein's theory of relativity. It describes the phenomenon where time passes at different rates for observers in different frames of reference, especially when those frames are moving relative to each other or are under the influence of different gravitational fields.

Special Relativity and Time Dilation
Albert Einstein's Special Theory of Relativity, proposed in 1905, introduced the idea that time is not absolute. According to the theory, the faster an object moves, the slower time passes for it relative to a stationary observer. This effect becomes significant as the object approaches the speed of light.

Mathematical Expression
Time dilation can be mathematically expressed using the Lorentz factor:
 
Where:

t is the time interval measured by the stationary observer

t’ is the time interval experienced by the moving object

v is the velocity of the moving object

c is the speed of light in a vacuum

Real-World Examples

GPS Satellites: Satellites in orbit experience time slightly faster than clocks on Earth due to both gravitational and relative motion effects. Their systems must compensate for time dilation to provide accurate location data.

Muons: These subatomic particles are created when cosmic rays hit Earth's atmosphere. Due to their high velocity, they live longer (from Earth's frame) than expected, allowing them to reach the surface.

Conclusion
Time dilation is not just a theoretical idea; it has been confirmed through numerous experiments and has practical applications in modern technology. Understanding it deepens our grasp of how time and space are interconnected in the universe.


"""

parser = StrOutputParser()

teacher_model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GEMINI_API_KEY'))

quiz_model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',api_key = os.getenv('GOOGLE_API_KEY'))

prompt1=PromptTemplate(
  
    input_variables = ['topic'],

    template = 
    
    """
    generate simple notes on "{topic}" with simple and concise language.

    make it easy to understand for freshers.
    
    """
)

prompt2=PromptTemplate(
    
    input_variables = ['topic'],
    
    template = 
    
    """
    generate simple 5 quiz on "{topic}" with 4 options.

    questions should be to check if basic understanding of topic is clear.
    
    
    
    """
)

prompt3=PromptTemplate(
    
    input_variables = ['notes','quiz'],

    template = 
    
    """
    Combine the notes and quiz into a single document.\n notes: {notes} \n quiz: {quiz}
    
    """
)

parallel_chain = RunnableParallel({

    'notes': prompt1 | teacher_model | parser,

    'quiz': prompt2 | quiz_model | parser,

})

''' this ^ parallel chain will run 2 chains parallely using RunnableParallel and both chains will take 'topic' as input.
    output from both chains will be stored in the dictionary with keys 'notes' and 'quiz' and will be passed to merge_chain.
    as merge_chain will take both 'notes' and 'quiz' as input and generate final report with notes and quiz.
'''

merge_chain = prompt3 | teacher_model | parser

final_chain = parallel_chain | merge_chain

result = final_chain.invoke({'topic':text})

#
# print(f"\n\n\n{result}\n\n\n")

final_chain.get_graph().print_ascii()

