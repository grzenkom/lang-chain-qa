from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
 
text = "Explain the concept of machine learning in one paragraph"
print(llm(text))
