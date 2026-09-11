from langchain_huggingface import HuggingFaceEmbeddings 
from dotenv import load_dotenv
load_dotenv()

embeddings_hf = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

vector = embeddings_hf.embed_query("Delhi is the capital of India")

print(str(vector))
