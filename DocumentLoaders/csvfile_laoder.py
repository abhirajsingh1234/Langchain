from langchain_community.document_loaders import CSVLoader

loader  = CSVLoader('csv_demo.csv')

data = loader.load()


print(f"type of data object: {type(data)}\n\n")

print(f"length of data object(will be equal to num of rows in csv): {len(data)}\n\n")

for i,row in enumerate(data):
    print(f'row {i}: \nContent : {row.page_content}\nmetadata : {row.metadata}\n\n')