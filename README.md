# Overview
This is my first attempt at a travel agent crew, or any crew for that matter. A lot of the credit goes to crewAIInc for insparation on the tools and tasks (I had to reformat a bit, especially reformatting the tools so that they are BaseTools, and will be accepted by crewAIs pydantic model, I don't believe you can pass through Unstructured tools), and, of course, credit goes to Cursor, especially for help debugging. 

# Installation
1. Clone repo
2. Install Poetry if you havent already
3. "Poetry lock" (Updates the poetry.lock file based on your poetry.toml file)"
4. "Poetry Install" Installs dependencies from the lock file into the Venv (creates the venv if it doesnt exist)
5. "poetry shell" (optional)(Activates venv for your current terminal session)

# File Overview

## agents.py
This file contains the definition of custom agents.
To create a Agent, you need to define the following:
1. Role: The role of the agent.
2. Backstory: The backstory of the agent.
3. Goal: The goal of the agent.
4. Tools: The tools that the agent has access to (optional).
5. Allow Delegation: Whether the agent can delegate tasks to other agents(optional).

    [More Details about Agent](https://docs.crewai.com/concepts/agents).

## task.py
This file contains the definition of custom tasks.
To Create a task, you need to define the following :
1. description: A string that describes the task.
2. agent: An agent object that will be assigned to the task.
3. expected_output: The expected output of the task.

    [More Details about Task](https://docs.crewai.com/concepts/tasks).

## crew (main.py)
This is the main file that you will use to run your custom crew.
To create a Crew , you need to define Agent ,Task and following Parameters:
1. Agent: List of agents that you want to include in the crew.
2. Task: List of tasks that you want to include in the crew.
3. verbose: If True, print the output of each task.(default is False).
4. debug: If True, print the debug logs.(default is False).

    [More Details about Crew](https://docs.crewai.com/concepts/crew).
