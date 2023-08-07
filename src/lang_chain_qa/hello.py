# https://stackoverflow.com/questions/76137512/langchain-huggingface-cant-evaluate-model-with-two-different-inputs
# https://github.com/hwchase17/langchain/blob/0e763677e4c334af80f2b542cb269f3786d8403f/docs/modules/models/llms/integrations/huggingface_hub.ipynb

from langchain import HuggingFaceHub, LLMChain
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

template = "Question: {question} Answer with as few words as possible."
prompt_template = PromptTemplate(template=template, input_variables=["question"])

# this uses HF servers for inference
# TODO: replace with local model
llm_model = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature":0, "max_length":64})

llm_chain = LLMChain(prompt=prompt_template, llm=llm_model)

question = "What color goose berry is?"
print(llm_chain.run(question))
