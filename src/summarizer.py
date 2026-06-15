import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


PROMPTS_DIR = Path("prompts")


def load_prompt_template(file_name: str) -> str:
    """
    Load a prompt template from the prompts directory.

    Args:
        file_name: Name of the prompt file.

    Returns:
        Prompt template as a string.
    """
    prompt_path = PROMPTS_DIR / file_name

    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    return prompt_path.read_text(encoding="utf-8")


def fill_prompt_template(template: str, activity_summary: str) -> str:
    """
    Insert the activity summary into a prompt template.
    """
    return template.replace("{activity_summary}", activity_summary)


def get_openai_client() -> OpenAI:
    """
    Create an OpenAI client using the OPENAI_API_KEY environment variable.

    Returns:
        OpenAI client instance.
    """
    load_dotenv(override=True)

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Add it to your .env file."
        )

    return OpenAI(api_key=api_key)


def generate_ai_text(prompt: str, model: str = "gpt-4.1-mini") -> str:
    """
    Generate text from an LLM using a completed prompt.

    Args:
        prompt: Completed prompt string.
        model: OpenAI model name.

    Returns:
        Generated text response.
    """
    client = get_openai_client()

    try:
        response = client.responses.create(
            model=model,
            input=prompt,
        )

        return response.output_text

    except Exception as error:
        raise ValueError(
            "AI generation failed. Check your OpenAI API key, billing, quota, or model access."
        ) from error

def should_use_mock_ai() -> bool:
    """
    Check whether the app should use mock AI outputs instead of calling the API.
    """
    load_dotenv(override=True)
    return os.getenv("USE_MOCK_AI", "false").lower() == "true"


def generate_mock_content_outputs(activity_summary: str) -> dict:
    """
    Generate fake AI outputs for local development without using paid API calls.
    """
    return {
        "weekly_summary": f"""# Weekly Build Summary

## Overview
This week, I worked on Build Log AI and made progress on turning GitHub activity into useful project documentation.

## What I Built
- Fetched commit activity from GitHub
- Converted raw commits into an activity summary
- Added prompt templates for future AI-generated content

## Technical Progress
The app now has a working data flow from GitHub commits to a structured activity summary.

## What I Learned
- How to call an external API
- How to clean and group commit data
- Why prompt templates should be separated from app code

## Challenges
The main challenge was connecting different parts of the app cleanly without mixing UI, formatting, and AI logic.

## Next Steps
- Connect real AI generation
- Add Markdown export
- Improve the dashboard layout

---

Mock mode is ON. No OpenAI API call was made.

Activity used:

{activity_summary}
""",
        "linkedin_post": """This week I made progress on Build Log AI, an app that turns GitHub commits into developer progress updates.

I worked on the GitHub API fetcher, commit formatting, activity summaries, and prompt templates.

The biggest lesson so far is that AI apps need a clean data pipeline before the AI layer is useful. Raw commits are messy, so the app first needs to clean and organize them before generating content.

Next step: connect real AI generation and add Markdown export.

#Python #Streamlit #GitHubAPI #AIEngineering #BuildInPublic""",
        "short_hooks": """1. Hook:
   I built a tool that turns GitHub commits into weekly updates.
   Video idea:
   Show the app fetching commits and creating a summary.
   Visual:
   Screen recording of the Streamlit app.

2. Hook:
   Raw GitHub commits are hard to read, so I cleaned them with Python.
   Video idea:
   Show before-and-after commit formatting.
   Visual:
   Split screen of raw commits vs activity summary.

3. Hook:
   Before adding AI, I built the data pipeline first.
   Video idea:
   Explain why clean input matters for AI apps.
   Visual:
   Diagram of GitHub API → parser → summary → AI.

4. Hook:
   I added prompt templates instead of hardcoding prompts.
   Video idea:
   Show the prompts folder and explain why it matters.
   Visual:
   VS Code file tree.

5. Hook:
   This is my first AI builder project.
   Video idea:
   Explain what Build Log AI does and why I’m building it.
   Visual:
   App demo plus GitHub repo.
""",
    }

def generate_content_outputs(activity_summary: str) -> dict:
    """
    Generate all AI content outputs from an activity summary.

    Args:
        activity_summary: Markdown activity summary.

    Returns:
        Dictionary containing generated content.
    """
    if should_use_mock_ai():
        return generate_mock_content_outputs(activity_summary)

    weekly_template = load_prompt_template("weekly_summary.txt")
    linkedin_template = load_prompt_template("linkedin_post.txt")
    hooks_template = load_prompt_template("short_hooks.txt")

    weekly_prompt = fill_prompt_template(weekly_template, activity_summary)
    linkedin_prompt = fill_prompt_template(linkedin_template, activity_summary)
    hooks_prompt = fill_prompt_template(hooks_template, activity_summary)

    return {
        "weekly_summary": generate_ai_text(weekly_prompt),
        "linkedin_post": generate_ai_text(linkedin_prompt),
        "short_hooks": generate_ai_text(hooks_prompt),
    }