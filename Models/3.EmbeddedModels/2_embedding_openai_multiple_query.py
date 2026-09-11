from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings_openai = OpenAIEmbeddings(model='text-embedding-3-large', dimension=32)

documents = [
    "Delhi is the capital of India",
    "Kolkata is capital of West Bengal",
    "Paris is capital of France"
]

result = embeddings_openai.embed_documents(documents)

print(str(result))
