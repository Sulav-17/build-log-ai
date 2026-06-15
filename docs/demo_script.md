# Build Log AI Demo Script

## 0:00 — Final Result

In this demo, I’m showing Build Log AI, a tool I built to turn GitHub commit activity into weekly developer summaries, LinkedIn posts, short-form video ideas, and Markdown build logs.

The goal of this project is to make it easier to document what I’m building and turn my GitHub activity into proof-of-work content.

## 0:20 — Problem

When I work on projects, GitHub tracks all of my commits, but raw commit messages are not always easy to explain to other people.

For example, a commit like `add github client` is useful for version control, but it does not clearly explain the project progress to someone viewing my portfolio.

So I wanted to build a tool that reads GitHub activity and turns it into clean, human-readable updates.

## 0:45 — How It Works

The app follows a simple flow.

First, the user enters a GitHub username, repository name, and date range.

Then the app calls the GitHub API and fetches recent commits.

After that, it cleans the commit messages, formats the dates, and groups the activity by day.

Then the app generates content outputs using either real AI generation or mock AI mode.

Finally, the user can download everything as a Markdown file.

## 1:30 — App Demo

Here is the Streamlit app.

I enter the GitHub username and repository name.

Then I choose the date range, such as the last 30 days.

When I click the fetch button, the app pulls recent commits from GitHub.

Now I can see the activity summary grouped by date.

Below that, the app shows generated content outputs:

- Weekly summary
- LinkedIn post
- Short-form video hooks

There is also a download button that exports the full build log as a Markdown file.

The raw commits are still available in an expandable section for transparency.

## 2:30 — Code Structure

The project is organized into separate modules.

`github_client.py` handles the GitHub API calls.

`formatter.py` cleans commit messages and groups activity.

`summarizer.py` handles AI generation and mock AI mode.

`export.py` creates the Markdown export.

`app.py` connects everything inside the Streamlit interface.

This structure keeps the app easier to maintain and test.

## 3:15 — What I Learned

This project helped me practice Python project structure, API calls, JSON parsing, environment variables, Streamlit, prompt templates, mock AI mode, Markdown export, and pytest.

The biggest lesson was that AI apps need a clean data pipeline before the AI layer becomes useful.

## 3:45 — Next Improvements

The next improvements I would add are GitHub token support, pull request analysis, multiple repository support, and deployment to Streamlit Cloud.

Overall, this project gives me a reusable tool for documenting future builds and turning project work into portfolio content.