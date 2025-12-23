import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config

from textwrap import dedent
from agents import TravelAgents
from tasks import TripTasks

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks =  TripTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_agent = agents.city_selection_agent()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        
        identify_city_task = tasks.identify_city_task(
            local_tour_guide,
            self.origin,
            self.cities,
            self.interests,
            self.date_range,
        )

        gather_city_info = tasks.gather_city_info_task(
            city_selection_agent,
            self.origin,
            self.interests,
            self.date_range
        )

        plan_itinerary_task = tasks.plan_itinerary_task(
            expert_travel_agent,
            self.origin,
            self.interests,
            self.date_range,    
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_agent, local_tour_guide],
            tasks=[identify_city_task, gather_city_info, plan_itinerary_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""Enter variable 1: """))
    var2 = input(dedent("""Enter variable 2: """))

    custom_crew = CustomCrew(var1, var2)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
