# https://www.markhneedham.com/blog/2023/06/23/hugging-face-run-llm-model-locally-laptop/

import json
import os
import torch

from datetime import datetime

from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

#assert len(os.environ["HUGGINGFACEHUB_API_TOKEN"]) > 0

# choose GPU or CPU
# TODO: fix error "CUDA out of memory. Tried to allocate 40.00 MiB (GPU 0; 3.81 GiB total capacity; 3.36 GiB already allocated; 26.38 MiB free; 3.37 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF"
# device = torch.cuda.current_device() if torch.cuda.is_available() else -1
device = -1

# the model will be downloaded on first use, if not cached in ~/.cache/huggingface/hub/

# model_id, task = "lmsys/fastchat-t5-3b-v1.0", "text2text-generation"
# model_id, task = "databricks/dolly-v2-3b, "text-generation"
# model_id, task = "CobraMamba/mamba-gpt-3b-v3", "text-generation"
model_id, task = "openlm-research/open_llama_3b_v2", "text-generation"

model = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task=task,
    model_kwargs={"temperature": 0, "max_length": 1000},
    device=device
)

text_template = """
You are a friendly chatbot assistant that responds conversationally to users' questions.
Keep the answers short, unless specifically asked by the user to elaborate on something.

Question: {question}

Answer:"""

prompt_template = PromptTemplate(template=text_template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt_template, llm=model)

print(f'Start: {datetime.now()}')

print(json.dumps(llm_chain("Who is Sheryl Crow?"), indent=2))
print(json.dumps(llm_chain("What is a crow?"), indent=2))
print(json.dumps(llm_chain("What is nuclear energy, in 20 words or less?"), indent=2))
print(json.dumps(llm_chain("What are pandas?"), indent=2))
print(json.dumps(llm_chain("What is pandas?"), indent=2))
print(json.dumps(llm_chain("How can I use 'tqdm'?"), indent=2))
print(json.dumps(llm_chain("What's the distance from the Earth to the Sun?"), indent=2))
print(json.dumps(llm_chain("Can you land on the Sun?"), indent=2))
print(json.dumps(llm_chain("I have 5 apples and 2 pears. How many vegetables do I have? Explain step by step."), indent=2))

print(f'End: {datetime.now()}')
