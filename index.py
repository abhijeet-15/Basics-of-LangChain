import os
import json
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

@tool
def get_weather(location: str):
    """Gets the weather of the city {location}"""
    return f"The weather at {location} is 25 degree Celsius."


agent = create_agent(
    model=os.getenv("OPENAI_LLM_MODEL"),
    tools=[get_weather],
    system_prompt="You are a helpful weather assistant that returns the current weather based on a city. Be polite and concise."
)

response = agent.invoke(
    {
        "messages":
        [
            {
                "role": "user",
                "content": "What is the weather in London?"
            }
        ]  
    }
)

for message in response["messages"]:
    message.pretty_print()

llm_answer = response["messages"][-1].content
print(llm_answer)

    