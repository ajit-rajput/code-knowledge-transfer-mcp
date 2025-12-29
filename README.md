# Code Knowledge Transfer MCP

A Model Context Protocol (MCP) server designed to transfer engineering knowledge — not just code explanations — from real-world codebases.

This project focuses on evidence-backed understanding: why code exists, how it evolved, and what is safe or risky to change. It is intentionally conservative, read-only, and optimized for onboarding, handovers, and informed refactoring decisions.

⸻

## Why This Exists

Most AI tools explain what code does.

Engineers joining a project usually need something different:
	•	Why was this designed this way?
	•	What historical constraints shaped it?
	•	What broke here before?
	•	Where is it safe to change things — and where is it dangerous?

code-knowledge-transfer-mcp encodes that missing context using verifiable evidence from:
	•	source code
	•	commit history
	•	issues and discussions

No speculation. No hallucination. Explicit uncertainty when evidence is weak.

⸻

## What This Project Is (and Is Not)

✅ It is
	•	A read-only MCP server
	•	A knowledge transfer and onboarding aid
	•	Evidence-first and conservative by design
	•	Client-agnostic (Claude Desktop, Cursor, Continue.dev, etc.)

❌ It is not
	•	A chatbot
	•	A code generator or refactoring tool
	•	An autonomous agent
	•	A replacement for maintainers or reviewers

⸻

## High-Level Architecture

User Prompt ->
 --> MCP Client (Claude / VS Code extension)
        --> decides when tools are needed
            --> code-knowledge-transfer-mcp (this repo)
                ├── get_file
                ├── get_commits
                └── find_issues
            ↓
  Verifiable evidence from GitHub

## Key design principle:

The MCP server provides facts only. Reasoning happens in the client.

⸻

## Initial Scope
	•	Repository: psf/requests
	•	Focus: Session and request lifecycle
	•	Goal: Enable safe onboarding and change decisions

The design is intentionally repo-agnostic and can be extended to other projects.

⸻

### Example Questions This System Handles Well
	•	“Explain how Requests Sessions work internally”
	•	“Why does the Session abstraction exist in requests?”
	•	“What is safe vs risky to change in Requests Sessions?”
	•	“Where is the historical evidence weak or incomplete?”

These questions reflect real onboarding and handover scenarios.

⸻

## Output Philosophy

The system optimizes for:
	•	Traceability to real evidence
	•	Conservative risk assessment
	•	Explicit uncertainty

## Typical answers:
	•	Reference real files, commits, or issues
	•	Flag high-risk areas more often than safe ones
	•	Avoid confident claims without evidence

This is intentional.

⸻

## Running with Claude Desktop

1. Prerequisites
	•	Python 3.10+
	•	GitHub token (read-only is sufficient)
	•	Claude Desktop (macOS)

2. Install dependencies

python -m venv venv
source venv/bin/activate
pip install -e .

3. Configure Claude Desktop

Create or edit:

~/Library/Application Support/Claude/claude_desktop_config.json

Example configuration:

{
  "mcpServers": {
    "code-knowledge-transfer-mcp": {
      "command": "/absolute/path/to/venv/bin/python",
      "args": ["-m", "ckt_mcp.server"],
      "cwd": "/absolute/path/to/code-knowledge-transfer-mcp"
    }
  }
}

Restart Claude Desktop after saving.

⸻

Recommended Session Setup Prompt

When starting a new Claude chat, use this once:

You are using an MCP server called "code-knowledge-transfer-mcp".

Rules:
- Use MCP tools for all factual claims.
- Do not answer from general knowledge alone.
- Prefer evidence from source code, commits, and issues.
- If evidence is weak or missing, say so explicitly.
- Be conservative about intent and change risk.

Optimize for accurate knowledge transfer, not fluency.


⸻

Development Notes
	•	MCP servers do not hot-reload
	•	Any code change requires restarting the MCP client
	•	The project uses an editable install (pip install -e .) for reliable module resolution

⸻

Design Principles (Non-Negotiable)
	•	Evidence-first
	•	Read-only
	•	Structured reasoning
	•	Conservative risk classification
	•	Explicit uncertainty

If a claim cannot be supported by evidence, the system should say so.

⸻

Why MCP

MCP enforces a hard boundary between:
	•	data access (tools)
	•	reasoning (LLM client)

This makes the system:
	•	auditable
	•	predictable
	•	safer for engineering decision support

⸻
