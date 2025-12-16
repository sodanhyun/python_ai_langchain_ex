from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.environ.get('ANTHROPIC_API_KEY')

model = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")
result = model.invoke("랭체인이 뭔가요?")
print(result.content)