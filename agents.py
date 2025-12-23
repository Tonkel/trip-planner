from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools.search_tool import SearchTools
from tools.calculator_tool import CalculatorTools


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.OpenAIGPT = ChatOpenAI(model_name="gpt-5.1", temperature=0.7)
        self.OpenAIGPT5mini = ChatOpenAI(model_name="gpt-5-mini", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""I am an expert in travel planning and logistics. I have decades of experience in travel planning, logistics and making itineraries for clients."""),
            goal=dedent(f"""
            Create a 7-day travel itinerary with detailed per-day plans, including budget, packing suggestions, and safety tips.
            """),
            tools=[SearchTools.search_internet, CalculatorTools.calculate],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT,
        )

    def city_selection_agent(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""A expert in analyzing travel data to pick ideal destinations."""),
            goal=dedent(f"""Select the best city based on weather, season, prices, and activities."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""A knowledgeable local guide with extensive information about the city, it's attractions and customs."""),
            goal=dedent(f"""provide the best insights about the selected city, including hidden gems, cultural hotspots, and practical travel tips."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT,
        )
