from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import Language

text="""

# auto_generated_classes.py

for i in range(1, 601):  # 1 to 600
    class_name = f"Class{i:03}"  # Class001, Class002, etc.
    print(f"class {class_name}:")
    print(f"    def __init__(self):")
    print(f"        print('Initializing {class_name}')\n")
    
    # Add a few simple methods
    for j in range(1, 4):  # 3 methods per class
        method_name = f"method{j}"
        print(f"    def {method_name}(self):")
        print(f"        print('{class_name} - {method_name} called')\n")

    class Class001:
    def __init__(self):
        print('Initializing Class001')

    def method1(self):
        print('Class001 - method1 called')

    def method2(self):
        print('Class001 - method2 called')

    def method3(self):
        print('Class001 - method3 called')

class Class002:
    def __init__(self):
        print('Initializing Class002')

    def method1(self):
        print('Class002 - method1 called')

    def method2(self):
        print('Class002 - method2 called')

    def method3(self):
        print('Class002 - method3 called')

# and so on... until Class600


"""

splitter_obj = RecursiveCharacterTextSplitter.from_language(

    language = Language.PYTHON,
    chunk_size = 150,
    chunk_overlap = 20
)

result = splitter_obj.split_text(text)


for i in result:
    print(i)
    print("\n\n")

