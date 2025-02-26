from environment import OPENAI_API_KEY, ROBLOX_API_KEY

from openai import OpenAI
from agentsjson import ToolFormat, get_tool_prompt, get_tools
from executor import execute #temporary
from agentsjson.core import load_agents_json
from agentsjson.core.models.bundle import Bundle
from agentsjson.core.models.auth import AuthType, BearerAuthConfig

agents_json_url = "https://raw.githubusercontent.com/Mordritz/roblox-api-agents/refs/heads/main/agents_json/roblox/agents.json"

data: Bundle = load_agents_json(agents_json_url)
agentsjson = data.agentsJson
flows_context = get_tool_prompt(agentsjson)

system_prompt = f"""You are an AI assistant that helps users interact with the Roblox Open Cloud API.
You have access to the following API flows:

{flows_context}

Analyze the user's request and use the appropriate API flows to accomplish the task.
You must give your arguments for the tool call as Structued Outputs JSON with keys `parameters` and `requestBody`"""

query = "Get a list of group join requests for the Roblox group with id: 3383949 and accept them."

auth = BearerAuthConfig(type=AuthType.BEARER, token=ROBLOX_API_KEY)

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query},
    ],
    tools=get_tools(agentsjson, format=ToolFormat.OPENAI),
    temperature=0,
)

response = execute(agentsjson, response, format=ToolFormat.OPENAI, auth=auth)

print(response)
