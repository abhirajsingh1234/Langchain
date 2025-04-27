from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
hiperinsomniyaa.
my name is abhiraj.
i am a boy.

how are you?.

"""


'''in this splitting type splitter first try to split text on basis of paragraphs'\n\n'.
   if pargraphs are larger than the defined chunk size then it will split chunks
   on basis of lines'\n'.
   then if even lines are larger than the defined chunk size then it will split
   chunks on basis of spaces ' '.
   then if even words are larger than the defined chunk size then it will split
   chunks on basis of characters.
'''

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 15,
    chunk_overlap = 0
    

)

result_list = splitter.split_text(text)

'''
1st line was splitted in 2 on basis of characters which is forth priority.
2nd line was splitted in 2 on basis of spaces which is third priority.
3rd line was splitted in 2 on basis of lines which is second priority.
4th line was splitted in 2 on basis of paragraphs which is first priority.'''

print(result_list)

print(len(result_list))

