import random

from abc import ABC, abstractmethod
import json

class runnable(ABC):

    @abstractmethod

    def invoke(self, data):

        pass

class naklitemplate(ABC):

    def __init__(self,template,input_variables):

        self.template = template

        self.input_variables = input_variables

    def invoke(self, input_dict):

        return self.template.format(**input_dict)
        
    def format(self,input_dict):

        return self.template.format(**input_dict)

class nakliLLM(runnable):

    def __init__(self):

        self.lists = [' he is good',' is doing fine',' is doing well',' is doing great']

    def invoke(self,input_):

        result = random.choice(self.lists)

        return {"AI":result}

    def generate(self,inputs_dict):

        result = random.choice(self.lists)

        result = result.format(**inputs_dict)

        return {"AI":result}

class naklichain:
    def __init__(self,llm,prompt):

        self.llm = llm

        self.prompt = prompt
       

        self.llm = nakliLLM()

    def run(self,data):

        prompt = self.prompt.format(data)

        return self.llm.invoke(data)['AI']

class naklijsonparser(runnable):
    
    def __init__(self) -> None:
        pass

    def invoke(self, input_dict):
        
        return input_dict

class runnablechain:

    def __init__(self,lists):

        self.lists = lists
    
    def invoke(self, input_dict):

        for i in self.lists:

            response = i.invoke(input_dict)

            input_dict = response

            print(input_dict)
            if isinstance(response,dict):
                if 'AI' in response:
                    input_dict = {'name':input_dict['AI']}

            

        return input_dict


template = naklitemplate(

    template = "how is my brother {name}",

    input_variables = ['name']

)

llm = nakliLLM()

parser = naklijsonparser()

chain = runnablechain([template,llm])

chain2 = runnablechain([template,llm,parser])

final = runnablechain([chain,chain2])

print(final.invoke({"name":"Nakli"}))