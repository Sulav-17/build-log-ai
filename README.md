# Build Log AI

Build Log AI is an AI-powered developer activity dashboard that turns GitHub commit history into weekly build logs, LinkedIn posts, YouTube progress updates, TikTok / Shorts hooks, and portfolio notes.

## Problem

Developers often build projects but do not consistently document their progress. GitHub stores commit activity, but raw commit messages are not always easy for recruiters, hiring managers, or portfolio viewers to understand.

Build Log AI solves this by converting technical GitHub activity into clear, human readable progress updates.

## Target User

This tool is for developers, students, AI builders, and technical professionals who want to turn their project work into proof-of-work content.

## Solution

The app connects to a GitHub repository, fetches recent commits, organizes the activity, and uses AI to generate polished summaries and content outputs.

## MVP Features

- Enter a GitHub username and repository name
- Select a date range: last 7 days or last 30 days
- Fetch recent GitHub commits
- Parse commit messages, dates, authors, and links
- Group activity into a weekly development summary
- Generate:
  - Weekly developer summary
  - LinkedIn post
  - YouTube progress update
  - 5 TikTok / Shorts hooks
  - Portfolio notes
- Export the final output as Markdown

## Not Included in MVP

- Multiple repository support
- Resume bullet generation
- Portfolio case study generation
- Scheduled email reports
- User accounts
- Payments
- Advanced agent workflows

These may be added later after the core MVP works.

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
AI Summary Generator
   ↓
Streamlit Dashboard
   ↓
Markdown Export