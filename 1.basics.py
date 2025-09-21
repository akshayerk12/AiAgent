from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain.agents import initialize_agent, tool
from langchain_community.tools import TavilySearchResults
import datetime

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash-8b')
# answer = llm.invoke('Explain  messi in one word')
# print(answer)

@tool
def GetSystemTime(format: str = "%Y-%m-%d %H:%M:%S"):
    """
    The function use to get current date and time.
    """
    currentTime = datetime.datetime.now()
    formatedTime = currentTime.strftime(format)
    return formatedTime

# timeTool = GetSystemTime()
search_tool = TavilySearchResults(search_depth = 'basic')
tools = [search_tool, GetSystemTime]
agent = initialize_agent(tools = tools,
                         llm=llm,
                         agent="zero-shot-react-description",
                         verbose=True,
                         handle_parsing_errors = True)
# agent.invoke("Give me a insta post caption for today's weather in Kerala.")
# print(search_tool)
agent.invoke("When was space X's last launch and how many days before today?")