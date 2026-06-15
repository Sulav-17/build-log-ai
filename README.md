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

'''text
