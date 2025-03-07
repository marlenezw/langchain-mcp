# Create server parameters for stdio connection
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
import os
from dotenv import load_dotenv

load_dotenv()

model = AzureAIChatCompletionsModel(
    endpoint="https://models.inference.ai.azure.com",
    credential=os.environ["GITHUB_TOKEN"],
    model_name="gpt-4o",
    api_version="2024-05-01-preview",
)

server_params = StdioServerParameters(
    command="/usr/local/bin/docker",
    args=["run", "-e", f"GITHUB_PERSONAL_ACCESS_TOKEN={os.environ.get('GITHUB_PERSONAL_ACCESS_TOKEN')}", "-i", "mcp/github"],
    env=None  # You can add environment variables if needed
)

async def run_app(user_question):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": f"{user_question}"})
            print(agent_response)

if __name__ == "__main__":
    user_question = 'Summaize the last 3 commits from langchain-ai/langchain-azure'
    asyncio.run(run_app(user_question=user_question))
