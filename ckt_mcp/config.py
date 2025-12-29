import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise RuntimeError("GITHUB_TOKEN is required")

REPO_OWNER = "psf"
REPO_NAME = "requests"
REPO = f"{REPO_OWNER}/{REPO_NAME}"

GITHUB_API_BASE = "https://api.github.com"