from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Define agent 1 backstory here"""),
            goal=dedent(f"""
            Create a 7-day travel itinerary with detailed per-day plans, including budget, packing suggestions, and safety tips.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_agent(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""A expert in analyzing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best city based on weather, season, and prices"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""A expert in analyzing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best city based on weather, season, and prices"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
