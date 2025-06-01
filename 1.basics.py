from dotenv import load_dotenv
import os
load_dotenv()

# Access variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# from google import genai
from google import generativeai as genai

# client = genai.Client(api_key=GOOGLE_API_KEY)
from langchain_google_genai import ChatGoogleGenerativeAI



# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents="Explain how AI works"
# )
# print(response.text)

genai.configure(api_key=GOOGLE_API_KEY)

llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash-8b')
answer = llm.invoke('Explain  messi in one word')
print(answer)
# model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-flash", etc.

# response = model.generate_content("Explain how AI works in one line")

# print(response.text)
