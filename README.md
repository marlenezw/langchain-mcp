# Quick Start with Langchain and the Github MCP Server

This Python code gets you started with the [MCP Github Server](https://github.com/modelcontextprotocol/servers/blob/main/src/github/README.md) and [Langchain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters/tree/main)
This package uses [langchain-azure](https://github.com/langchain-ai/langchain-azure) with [Github Models](https://github.com/marketplace/models/azure-openai/gpt-4o) to prototype with LLMs for free :) 

To run the server locally with docker you should:
1. Install docker
2. Clone the mcp server repo
   ```
   git clone https://github.com/modelcontextprotocol/servers.git
   cd servers
   ```
3. Build the docker image
   ```
   docker build -t mcp/github -f src/github/Dockerfile .
   ```
4. Install the requirements and run the Python script
