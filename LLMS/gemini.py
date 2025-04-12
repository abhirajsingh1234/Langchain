from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model='text-bison-001')
result = llm.invoke('what is the capital of india')

print(result)


'''llm = GoogleGenerativeAI(model='gemini-1.5-flash', temperature=0.7, top_p=0.9, top_k=40, max_output_tokens=256)'''