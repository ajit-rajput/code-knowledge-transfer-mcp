import base64
import requests
from ckt_mcp.config import GITHUB_API_BASE, GITHUB_TOKEN, REPO

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "code-knowledge-transfer-mcp"
}

def _get(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()


def fetch_file(path: str) -> str:
    clean_path = path.lstrip("/")

    print(f"[MCP] fetch_file: {path} → {clean_path}")

    url = f"{GITHUB_API_BASE}/repos/{REPO}/contents/src/{clean_path}"
    data = _get(url)

    return base64.b64decode(data["content"]).decode("utf-8")

def fetch_commits(path: str, limit: int = 10):
    clean_path = path.lstrip("/")

    url = f"{GITHUB_API_BASE}/repos/{REPO}/commits"
    params = {"path": clean_path, "per_page": limit}
    data = _get(url, params=params)

    return [
        {
            "sha": c["sha"],
            "message": c["commit"]["message"],
            "author": c["commit"]["author"]["name"],
            "date": c["commit"]["author"]["date"],
            "url": c["html_url"],
        }
        for c in data
    ]


def search_issues(query: str, limit: int = 5):
    url = f"{GITHUB_API_BASE}/search/issues"
    q = f"repo:{REPO} {query}"
    params = {"q": q, "per_page": limit}

    data = _get(url, params=params)

    return [
        {
            "title": item["title"],
            "url": item["html_url"],
            "state": item["state"],
        }
        for item in data["items"]
    ]