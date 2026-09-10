from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model='gpt-4', temperature=0, max_completion_tokens=100)

result = chat_model.invoke("What is capital of india")

print(result.content)