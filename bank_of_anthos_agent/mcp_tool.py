from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams

toolset = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://mcp.fi.money:8080/mcp/stream"
    )
)