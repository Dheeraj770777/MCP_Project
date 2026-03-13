from mcp.server.fastmcp import FastMCP
import sqlite3

mcp = FastMCP("Sales Server")

@mcp.tool()
def get_sales(date: str) -> str:
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.execute("SELECT revenue FROM sales WHERE date=?", (date,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return f"Sales on {date}: {row[0]}"
    else:
        return "No data"

if __name__ == "__main__":
    mcp.run()