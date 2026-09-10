from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

claude_model = ChatAnthropic(model_name='claude-3-5-sonnet-20241022', temperature=0)

result = claude_model.invoke("What is the capital of india")

print(result)