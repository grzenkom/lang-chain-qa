# https://www.markhneedham.com/blog/2023/06/23/hugging-face-run-llm-model-locally-laptop/


from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

model_id = "lmsys/fastchat-t5-3b-v1.0"
model = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text2text-generation",
    model_kwargs={"temperature": 0, "max_length": 1000},
)

text_template = """
You are a friendly chatbot assistant that responds conversationally to users' questions.
Keep the answers short, unless specifically asked by the user to elaborate on something.

Question: {question}

Answer:"""

prompt_template = PromptTemplate(template=text_template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt_template, llm=model)

question = "What color an apple can be?"
print(llm_chain(question))
