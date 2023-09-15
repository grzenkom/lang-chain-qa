import os
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


HF_TOKEN = os.getenv("HF_TOKEN")

peft_model_id = "szymonrucinski/krakowiak-7b"
peft_config = PeftConfig.from_pretrained(peft_model_id)

base_model_id = peft_config.base_model_name_or_path
base_model = AutoModelForCausalLM.from_pretrained(base_model_id, token=HF_TOKEN)
base_tokenizer = AutoTokenizer.from_pretrained(base_model_id, token=HF_TOKEN)

peft_model = PeftModel.from_pretrained(base_model, peft_model_id)

pipeline = pipeline(task="text-generation", model=peft_model, tokenizer=base_tokenizer, device_map="auto")

prompt = """
Udziel krótkiej odpowiedzi na pytanie, w sposób zrozumiały dla 10-latka.
Pytanie: {question}
"""
print(pipeline(prompt.format(question="Co to jest fotosynteza?")))


# Notes about attempts to use`load_in_8bit`:
#
# 1. `transformers`` had to be downgraded to 4.30.2, because of "ImportError: Using `load_in_8bit=True`
#   requires Accelerate and the latest version of bitsandbytes", https://stackoverflow.com/q/76924239/95
# 2. With GPU: "torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 86.00 MiB (GPU 0;
#    3.81 GiB total capacity; 3.12 GiB already allocated; 28.38 MiB free; 3.36 GiB reserved in total
#    by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation."
# 2. With no GPU (CUDA_VISIBLE_DEVICES=""):  "RuntimeError: No GPU found. A GPU is needed for quantization."
