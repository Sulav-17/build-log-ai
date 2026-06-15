from collections import defaultdict
from datetime import datetime


def clean_commit_message(message: str) -> str:
    """
    Clean a raw commit message.

    Args:
        message: Raw commit message from GitHub.

    Returns:
        A cleaned commit message.
    """
    first_line = message.split("\n")[0]
    return first_line.strip()


def format_commit_date(date_value: str) -> str:
    """
    Convert GitHub's datetime format into a simple date string.

    Args:
        date_value: ISO datetime string from GitHub.

    Returns:
        Date string in YYYY-MM-DD format.
    """
    if not date_value:
        return "Unknown date"

    parsed_date = datetime.fromisoformat(date_value.replace("Z", "+00:00"))
    return parsed_date.strftime("%Y-%m-%d")


def group_commits_by_date(commits: list[dict]) -> dict:
    """
    Group commits by commit date.

    Args:
        commits: List of cleaned commit dictionaries.

    Returns:
        Dictionary where each key is a date and each value is a list of commits.
    """
    grouped_commits = defaultdict(list)

    for commit in commits:
        commit_date = format_commit_date(commit.get("date", ""))

        grouped_commits[commit_date].append(
            {
                "message": clean_commit_message(commit.get("message", "")),
                "author": commit.get("author", "Unknown"),
                "sha": commit.get("sha", ""),
                "url": commit.get("url", ""),
            }
        )

    return dict(grouped_commits)


def create_activity_summary(commits: list[dict]) -> str:
    """
    Create a simple Markdown activity summary from commits.

    Args:
        commits: List of cleaned commit dictionaries.

    Returns:
        Markdown-formatted activity summary.
    """
    if not commits:
        return "No commit activity found for this date range."

    grouped_commits = group_commits_by_date(commits)

    summary_lines = ["# Activity Summary", ""]

    for commit_date, date_commits in sorted(grouped_commits.items(), reverse=True):
        summary_lines.append(f"## {commit_date}")

        for commit in date_commits:
            summary_lines.append(f"- {commit['message']}")

        summary_lines.append("")

    return "\n".join(summary_lines)