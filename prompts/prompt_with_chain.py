from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import JsonOutputParser

question = ["""Name: Rahul Sharma
ID Number: 1234 5678 9012
DOB: 15/08/1990
Gender: Male
Address: 123, Nehru Nagar, Andheri East, Mumbai, Maharashtra - 400069
Father's Name: Ramesh Sharma
Mobile Number: 9876543210
Enrollment ID: 1234/56789/12345
Issue Date: 12/06/2018""","""rahul  sharma  
DOB:15/08/1990   Gender: M  
123   nehru nagar  
Andheri   East,   mumbai  
Maharashtra -400069  

ID No. :   1234   5678 9012  
Mob:  9876543210  
Father's name : Ramesh     sharma  

Enrolment ID 1234/56789/12345  
Issued on: 12 -06 -2018""",
"""
rahul  sharma\n
DOB:15/08/1990   Gender: M\n
123   nehru nagar\n
Andheri   East,\n
mumbai   Maharashtra -400069\n
\n
ID No. :   1234   5678 9012\n
Mob:  9876543210\n
Father's name : Ramesh     sharma\n
\n
Enrolment ID 1234/56789/12345\n
Issued on: 12 -06 -2018\n
""",
"""
rAhul    sharma  
dob : 15/08/1990   Gender:M  

Add: 123 / nehru   nagar / andheri
east,mumbai- 400069 , maha rashtra  

ID number : 1234  5678    9012
enrol_ID :1234 / 56789 / 12345
Mob No: +91  98765 43210

issued:12 -06 - 2018

father name:Ramesh  sharma  

--- *** ---

valid only if signed.
doc ref : #IN09876
signature: ____  
""",
 """
Name:  priya   r.   mehta  
Father's Name :  Ramesh  K. Mehta

DOB : 12/06/1989  
Pan NO : BZTPM2345K

Address: 27/B,  3rd flr  
sai shraddha apt\n
kandivali(w)  mumbai -400067  
issued : 21   July 2016

sig: ___  
INCOME TAX DEPT  
govt. of india  
ref : IN-PAN-0029-MH  
""",
"Name: priya r. mehta\nFather's Name : Ramesh K. Mehta\nDOB : 12/06/1989\nPan NO : BZTPM2345K\nAddress: 27/B, 3rd flr sai shraddha apt\nkandivali(w) mumbai -400067\nissued : 21 July 2016\nsig: ___\nINCOME TAX DEPT\ngovt. of india\nref : IN-PAN-0029-MH"]


parser = JsonOutputParser()

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=os.getenv('GEMINI_API_KEY'))

# way of writing prompts
list = ['AAdhar', 'Voter ID', 'PAN', 'electricity bill']

string_list = ', '.join(list)

template = PromptTemplate(
    input_variables=["question"],
    partial_variables={'list': string_list},
    template="""
                SYSTEM ROLE: You are an expert legal advisor specialized in Indian government documents.

                TASK: Based on the user's question, identify which Indian document is being referred to.
                      Respond with only one word — the name of the document.

                AVAILABLE DOCUMENTS: {list}

                **Question:** {question}

                Respond in the following JSON format:
                {{
                    "document": "..."
                }}
"""
)


chain = template | model | parser

response=chain.invoke({
    "question": question[5],
})

print(response)