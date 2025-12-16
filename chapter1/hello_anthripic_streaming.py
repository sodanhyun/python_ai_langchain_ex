import os
from dotenv import load_dotenv
import anthropic
import rich

load_dotenv()

api_key = os.environ.get('ANTHROPIC_API_KEY')

client = anthropic.Anthropic(api_key=api_key)

prompt = "anthropic 발음은 앤트로픽이 맞나요? 앤쓰로픽이 맞나요?"
with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}],
    model="claude-3-5-haiku-20241022",
) as stream:
    for event in stream:
        if event.type == "text":
            print(event.text, end="")
    print()
    rich.print(stream.get_final_message())