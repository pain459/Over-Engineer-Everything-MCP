# client_test.py
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    server = StdioServerParameters(command=sys.executable, args=["server.py"])
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Tools:", [t.name for t in tools.tools])

            res = await session.call_tool("overengineer", arguments={"idea": "make tea"})
            # Usually the first content block is text
            print("\nResult:\n", res.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())