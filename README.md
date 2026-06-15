# Build Log AI

Build Log AI is an AI-powered developer activity dashboard that turns GitHub commit history into weekly build logs, LinkedIn posts, short-form video hooks, and portfolio notes.

## Problem

Developers often build projects but do not consistently document their progress. GitHub stores commit activity, but raw commit messages are not always easy for recruiters, hiring managers, portfolio viewers, or social media audiences to understand.

Build Log AI solves this by converting technical GitHub activity into clear, human-readable progress updates.

## Target User

This tool is for developers, students, AI builders, and technical professionals who want to turn their project work into proof-of-work content.

## Features

- Enter a GitHub username and repository name
- Select a date range: last 7 days or last 30 days
- Fetch recent GitHub commits
- Parse commit messages, dates, authors, and links
- Group activity by date
- Generate:
  - Weekly developer summary
  - LinkedIn post
  - Short-form video hooks
- Use mock AI mode for local testing without paid API calls
- Export the final build log as Markdown

## Architecture

```text
User Input
   ↓
GitHub API Fetcher
   ↓
Commit Parser
   ↓
Activity Aggregator
   ↓
Prompt Templates
   ↓
AI Summary Generator / Mock AI Generator
   ↓
Streamlit Dashboard
   ↓
Markdown Export

## Tech Stack

- Python
- Streamlit
- GitHub API
- Requests
- Python-dotenv
- OpenAI API
- Pandas
- Pytest
- Markdown

## Project Structure

```text
build-log-ai/
├── app.py
├── src/
│   ├── github_client.py
│   ├── summarizer.py
│   ├── formatter.py
│   ├── database.py
│   └── export.py
├── prompts/
│   ├── linkedin_post.txt
│   ├── weekly_summary.txt
│   └── short_hooks.txt
├── data/
│   └── sample_commits.json
├── tests/
├── .env.example
├── requirements.txt
└── README.md

Setup Instructions
1. Clone the repository
git clone https://github.com/Sulav-17/build-log-ai.git
cd build-log-ai
2. Create a virtual environment
py -m venv .venv
3. Activate the virtual environment

On Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Create a .env file

Create a file named .env in the project root.

For mock mode:

USE_MOCK_AI=true

For real OpenAI API generation:

OPENAI_API_KEY=your_openai_api_key_here
USE_MOCK_AI=false

Do not commit .env.

Running the App
streamlit run app.py
Running Tests
pytest
Mock AI Mode

Mock AI mode lets the app generate demo content without calling the OpenAI API.

Use this during development:

USE_MOCK_AI=true

This is useful because API usage may require billing.

Current Status

Completed:

Project setup
GitHub API commit fetching
Commit parsing and grouping
Activity summary generation
Prompt templates
AI generation layer
Mock AI mode
Markdown export
Streamlit dashboard
Limitations
Private repositories are not supported yet
Pull requests are not included yet
Real AI generation requires OpenAI API billing
Markdown export layout can be improved
No deployed demo yet
Future Improvements
GitHub token support
Pull request support
Resume bullet generation
Portfolio case study generation
Multiple repository support
Streamlit Cloud deployment
Scheduled weekly reports
What I Learned
How to structure a Python project professionally
How to call the GitHub API
How to parse and group JSON data
How to separate UI, formatting, AI, and export logic
How to use prompt templates
How to build with environment variables safely
How to write basic tests with pytest

## Portfolio Description

Built an AI-powered developer activity dashboard that connects to the GitHub API, analyzes recent commit activity, and generates weekly build summaries, LinkedIn posts, short-form video hooks, and Markdown build logs.

The project uses Python, Streamlit, GitHub API, prompt templates, OpenAI API integration, mock AI mode, Markdown export, and pytest-based testing.

## Resume Bullets

- Built an AI-powered developer productivity tool using Python, Streamlit, and the GitHub API to transform commit activity into structured weekly build logs and social content.
- Implemented a modular architecture with API fetching, commit parsing, prompt templates, AI generation, mock mode, Markdown export, and automated tests.
- Designed a local development workflow using environment variables, Git/GitHub version control, and pytest to support safer iteration and maintainable code.

## Demo Checklist

Before recording or sharing this project:

- Run the app locally with `streamlit run app.py`
- Use a public GitHub repository
- Confirm commits are fetched successfully
- Confirm activity summary appears
- Confirm generated content appears
- Confirm Markdown download works
- Confirm tests pass with `pytest`
- Confirm `.env` is not committed
- Push latest code to GitHub

## LinkedIn Post Draft

I finished the MVP for Build Log AI.

The problem I wanted to solve:
GitHub commits show what I worked on, but they are not always easy to turn into portfolio updates or public proof-of-work content.

What I built:
A Streamlit app that connects to the GitHub API, fetches recent commits, groups activity by date, generates developer summaries, creates LinkedIn-style content, suggests short-form video hooks, and exports everything as Markdown.

Tech stack:
Python, Streamlit, GitHub API, OpenAI API integration, python-dotenv, pytest, and Markdown export.

What I learned:
- How to structure a Python app professionally
- How to work with external APIs
- How to separate UI, data fetching, formatting, AI logic, and exports
- Why mock mode is useful when working with paid APIs

Next improvement:
Add GitHub token support and pull request analysis.

#Python #Streamlit #GitHubAPI #AIEngineering #BuildInPublic
