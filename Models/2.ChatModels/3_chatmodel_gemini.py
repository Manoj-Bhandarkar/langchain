from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

gemini = ChatGoogleGenerativeAI(model='gemini-3.6-flash')

result = gemini.invoke("What is the capital of india")

print(result.content_blocks)