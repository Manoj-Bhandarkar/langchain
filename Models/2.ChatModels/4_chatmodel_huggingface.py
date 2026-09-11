from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

hf_model = ChatHuggingFace(llm=llm)

result = hf_model.invoke("What is the capital of India")

print(result.content)