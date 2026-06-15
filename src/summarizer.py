from pathlib import Path


PROMPTS_DIR = Path("prompts")


def load_prompt_template(file_name: str) -> str:
    """
    Load a prompt template from the prompts directory.

    Args:
        file_name: Name of the prompt file.

    Returns:
        Prompt template as a string.

    Raises:
        FileNotFoundError: If the prompt file does not exist.
    """
    prompt_path = PROMPTS_DIR / file_name

    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    return prompt_path.read_text(encoding="utf-8")


def fill_prompt_template(template: str, activity_summary: str) -> str:
    """
    Insert the activity summary into a prompt template.

    Args:
        template: Prompt template containing {activity_summary}.
        activity_summary: Markdown activity summary.

    Returns:
        Completed prompt string.
    """
    return template.replace("{activity_summary}", activity_summary)