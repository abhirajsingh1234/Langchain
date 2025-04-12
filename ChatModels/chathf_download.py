from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_models_cache'
llm=HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_output_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke('how are you')

print(result.content)