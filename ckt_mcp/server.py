from mcp.server.fastmcp import FastMCP
from ckt_mcp.tools.github import (
    fetch_file,
    fetch_commits,
    search_issues,
)

mcp = FastMCP("code-knowledge-transfer-mcp")


@mcp.tool()
def get_file(path: str) -> str:
    """Fetch raw file contents from the repository"""
    return fetch_file(path)


@mcp.tool()
def get_commits(path: str, limit: int = 10):
    """Fetch commit history for a file"""
    return fetch_commits(path, limit)


@mcp.tool()
def find_issues(query: str, limit: int = 5):
    """Search issues and PRs related to a topic"""
    return search_issues(query, limit)


if __name__ == "__main__":
    mcp.run()