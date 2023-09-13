from langchain.llms import HuggingFacePipeline


model_id, task = "Voicelab/trurl-2-7b-8bit", "text-generation"

model = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task=task,
    # model_kwargs={
    #     "device_map": "auto",
    #     # {
    #     #     "transformer.word_embeddings": 0,
    #     #     "transformer.word_embeddings_layernorm": 0,
    #     #     "lm_head": "cpu",
    #     #     "transformer.h": 0,
    #     #     "transformer.ln_f": 0,
    #     # },
    #     "quantization_config": BitsAndBytesConfig(llm_int8_enable_fp32_cpu_offload=True)
    # },
)

from langchain import PromptTemplate, LLMChain

template_text = """
{question}
"""
template = PromptTemplate(template=template_text, input_variables=["question"])

llm_chain = LLMChain(llm=model, prompt=template)

print(llm_chain("Who is Sheryl Crow?"))
print(llm_chain("Jakiego koloru jest niebo?"))
print(llm_chain("Kim jest Sheryl Crow?"))

