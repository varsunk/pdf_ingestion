import os
from dotenv import load_dotenv

from LLM import LLM

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_ID = os.getenv("GEMINI_MODEL_ID")

lm = LLM(api_key=GEMINI_API_KEY, model_id=MODEL_ID)
response = lm._prompt_text(prompt="Who are you?")
print(response)