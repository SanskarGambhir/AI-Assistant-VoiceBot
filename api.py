import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env into environment

api_key = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("How long is burz khalifa")
print(response.text)