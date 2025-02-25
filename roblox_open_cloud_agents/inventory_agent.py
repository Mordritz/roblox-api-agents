from openai_client import client

from loader import load_agents_json
from agentsjson.core import ToolFormat
from agentsjson.core.models import Flow
from agentsjson.core.models.bundle import Bundle
import agentsjson.core as core

#use local loader
data: Bundle = load_agents_json("roblox", "agents.json")
flows = data.agentsJson.flows
flows_context = core.flows_prompt(flows)

system_prompt = f"""You are an AI assistant that helps users interact with the Roblox Open Cloud API.
You have access to the following API flows:

{flows_context}

Analyze the user's request and use the appropriate API flows to accomplish the task.
You must give your arguments for the tool call as Structued Outputs JSON with keys `parameters` and `requestBody`"""

query = "Get the complete list of inventory items for user with id 9823872"

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ],
    tools = core.flows_tools(flows, format=ToolFormat.OPENAI),
    temperature = 0
)