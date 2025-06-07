from fastmcp import FastMCP

mcp = FastMCP(
    name="MCP System Bridge",
    instructions="This server provides tools for managing the system.",
)


@mcp.tool()
async def open_url(url: str) -> None:
    pass


@mcp.tool()
async def copy_to_clipboard(text: str) -> None:
    pass


def main() -> None:
    mcp.run(transport="stdio")
