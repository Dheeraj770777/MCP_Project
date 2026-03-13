import asyncio
from mcp.client.stdio import StdioServerParameters, stdio_client
from mcp import ClientSession

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "get_sales",
                {"date": "2026-03-13"}
            )

            print("Dashboard View")
            if result.content:
                for item in result.content:
                    print(getattr(item, "text", item))
            else:
                print(result)

asyncio.run(main())