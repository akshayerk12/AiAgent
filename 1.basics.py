from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain.agents import initialize_agent
from langchain_community.tools import TavilySearchResults


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash-8b')
# answer = llm.invoke('Explain  messi in one word')
# print(answer)

search_tool = TavilySearchResults(search_depth = 'basic')
tools = [search_tool]
agent = initialize_agent(tools = tools,
                         llm=llm,
                         agent="zero-shot-react-description",
                         verbose=True,
                         handle_parsing_errors = True)
agent.invoke("Give me a insta post caption for todays weather in Banglore")