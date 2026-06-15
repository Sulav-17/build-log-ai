# Lessons Learned — Build Log AI

## What I Built

Build Log AI is a Streamlit app that turns GitHub commit activity into developer progress updates.

The app lets a user enter a GitHub username, repository name, and date range. It then fetches recent commits from the GitHub API, groups the activity by date, generates build-log style content, and exports the result as a Markdown file.

## What Was Hard

The hardest part was connecting multiple parts of the app cleanly without putting everything inside `app.py`.

I had to separate the project into different responsibilities:

- `github_client.py` handles GitHub API calls
- `formatter.py` cleans and groups commit activity
- `summarizer.py` handles AI and mock AI generation
- `export.py` creates Markdown exports
- `app.py` controls the Streamlit user interface

This made the project easier to understand and easier to test.

## Bugs I Ran Into

### Git was not recognized

At the beginning, the `git` command was not available in the VS Code terminal. I fixed this by installing Git for Windows and making sure Git was added to PATH.

### Python was not recognized

Python was also not initially available in the terminal. I installed CPython and made sure the Python command was available from PowerShell.

### Pytest could not import `src`

When running tests, pytest could not find the `src` module. I fixed this by adding a `pytest.ini` file with:

```ini
[pytest]
pythonpath = .


OpenAI API authentication and quota errors

I first used a placeholder API key by mistake. After fixing the key, I hit an API quota/billing error. To avoid blocking development, I added mock AI mode using:

USE_MOCK_AI=true

This allowed the app to keep working without paid API calls during development.

What I Learned About APIs

I learned how to call an external API using Python’s requests library.

The GitHub API returns a large JSON response, so I had to extract only the fields the app needed:

commit message
author
date
SHA
commit URL

I also learned why error handling matters. If a repository is not found, the app should give a useful message instead of crashing.

What I Learned About AI Apps

I learned that AI apps are not just about calling an LLM.

Before the AI layer is useful, the app needs clean input data. That means the project needs:

Reliable data fetching
Clean parsing
Organized activity summaries
Prompt templates
AI generation or mock generation
Exportable output

The quality of the AI output depends heavily on the quality of the structured input.

What I Learned About Project Structure

This project helped me understand why professional software projects separate responsibilities.

Instead of putting everything in one file, I used a modular structure:

src/
├── github_client.py
├── formatter.py
├── summarizer.py
├── database.py
└── export.py

This made the code easier to test, debug, and extend.

What I Would Improve Next

Future improvements I would add:

GitHub token support for private repositories and higher rate limits
Pull request analysis
Resume bullet generation
Portfolio case study generation
Multiple repository support
Streamlit Cloud deployment
Scheduled weekly email reports
Main Takeaway

The biggest lesson from this project is that a useful AI product needs a strong non-AI foundation first.

The GitHub API, data parsing, formatting, prompt templates, error handling, environment variables, and export system all matter before the AI output can be valuable.