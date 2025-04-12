from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")  # Make sure you already pulled it via ollama pull llama
list = ['AAdhar', 'Voter ID', 'PAN', 'electricity bill']
result = llm.invoke("""'
**Personal Information:**

1. Aabaar Number (unique 12-digit number)
2. Forename (given name)
3. Mother's Name
4. Date of Birth (DDMMYYYY format)

**Demographic Information:**

1. Sex (male/female/other)
2. State Code (where the individual was born or resides)
3. District Code (where the individual was born or resides)
4. Block Code (where the individual was born or resides)
5. Locus of Birth (street name and PIN code where the individual was born)'

**Important:** some of the data may be missing or incomplete or incorrect.

**Question:** which document contains these data

**Options:** {list}

output json format: {
    "document": "name of the document"
}
""")
print(result.content)
