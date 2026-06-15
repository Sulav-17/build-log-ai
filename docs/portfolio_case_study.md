# Build Log AI — Portfolio Case Study

## Problem

Developers often work on projects consistently but do not document their progress well.

GitHub stores commit history, but raw commit messages are not easy for recruiters, hiring managers, or portfolio viewers to understand. A commit message like `add github client` makes sense to the developer, but it does not clearly explain the value of the work.

Build Log AI solves this by turning GitHub commit activity into clear weekly build logs and content outputs.

## Solution

Build Log AI is a Streamlit application that connects to the GitHub API, fetches recent commits, organizes the activity by date, and generates structured project documentation.

The app helps developers turn their project work into:

- Weekly build summaries
- LinkedIn posts
- Short-form video hooks
- Markdown build logs
- Portfolio notes

The tool is designed to support a build-in-public workflow and make project progress easier to communicate.

## Tech Stack

- Python
- Streamlit
- GitHub API
- Requests
- Python-dotenv
- OpenAI API integration
- Mock AI mode
- Pytest
- Markdown export
- Git and GitHub

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

Key Features
GitHub Commit Fetching

The app lets the user enter a GitHub username, repository name, and date range. It then fetches recent commits from the GitHub API.

Commit Parsing and Grouping

Raw GitHub JSON is cleaned and converted into structured commit data. Commits are grouped by date to create a readable activity summary.

AI-Generated Content

The app uses prompt templates to generate developer-focused content, including a weekly summary, LinkedIn post, and short-form video hooks.

Mock AI Mode

Mock AI mode allows the app to generate demo content without making paid API calls. This is useful for local development, testing, and demos.

Markdown Export

The final output can be downloaded as a Markdown file, making it easy to save progress updates, reuse content, or add notes to a portfolio.

Testing

The project includes pytest tests for formatting, prompt loading, and Markdown export logic.

Challenges

One challenge was making sure the app stayed modular instead of putting all logic into the Streamlit file.

Another challenge was handling API-related errors properly. The project needed to handle:

Invalid GitHub repositories
Missing API keys
OpenAI API quota errors
Local environment setup issues

A third challenge was learning how to keep real API keys safe by using .env and .gitignore.

Results

The final MVP is a working developer productivity tool that can:

Fetch real GitHub commits
Group activity by date
Generate build-log style content
Export Markdown files
Run locally with mock AI mode
Maintain a clean project structure
Pass automated tests

The project is now portfolio-ready as an example of AI application development, API integration, data formatting, and Streamlit-based product building.

Future Improvements

Future improvements include:

GitHub token support for private repos
Pull request fetching
Multiple repository support
Resume bullet generation
Portfolio case study generation
Streamlit Cloud deployment
Scheduled weekly reports
Summary

Build Log AI demonstrates how AI can be used to improve a real developer workflow.

Instead of building a generic chatbot, this project uses AI as part of a specific system: turning GitHub activity into useful project documentation and proof-of-work content.