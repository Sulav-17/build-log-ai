from datetime import datetime


def format_raw_commits_for_markdown(commits: list[dict]) -> str:
    """
    Format raw commit data as a Markdown section.

    Args:
        commits: List of commit dictionaries.

    Returns:
        Markdown-formatted commit list.
    """
    if not commits:
        return "No raw commits available."

    lines = []

    for commit in commits:
        message = commit.get("message", "No message")
        sha = commit.get("sha", "")
        author = commit.get("author", "Unknown")
        date = commit.get("date", "")
        url = commit.get("url", "")

        lines.append(f"- **{message}**")
        lines.append(f"  - SHA: `{sha}`")
        lines.append(f"  - Author: {author}")
        lines.append(f"  - Date: {date}")

        if url:
            lines.append(f"  - Link: {url}")

        lines.append("")

    return "\n".join(lines)


def create_markdown_export(
    github_username: str,
    repo_name: str,
    date_range: str,
    activity_summary: str,
    weekly_summary: str,
    linkedin_post: str,
    short_hooks: str,
    commits: list[dict],
) -> str:
    """
    Create a complete Markdown export for a build log.

    Args:
        github_username: GitHub username.
        repo_name: Repository name.
        date_range: Selected activity range.
        activity_summary: Non-AI activity summary.
        weekly_summary: AI-generated weekly summary.
        linkedin_post: AI-generated LinkedIn post.
        short_hooks: AI-generated short-form hooks.
        commits: Raw commit data.

    Returns:
        Complete Markdown content as a string.
    """
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    raw_commits_markdown = format_raw_commits_for_markdown(commits)

    return f"""# Build Log Export

## Repository

- GitHub Username: `{github_username}`
- Repository: `{repo_name}`
- Date Range: {date_range}
- Generated At: {generated_at}

---

## Activity Summary

{activity_summary}

---

## Weekly Build Summary

{weekly_summary}

---

## LinkedIn Post

{linkedin_post}

---

## Short-Form Video Hooks

{short_hooks}

---

## Raw Commits

{raw_commits_markdown}
"""


def create_export_file_name(github_username: str, repo_name: str) -> str:
    """
    Create a safe Markdown file name for the export.

    Args:
        github_username: GitHub username.
        repo_name: Repository name.

    Returns:
        Markdown file name.
    """
    safe_username = github_username.strip().lower().replace(" ", "-")
    safe_repo = repo_name.strip().lower().replace(" ", "-")

    return f"build-log-{safe_username}-{safe_repo}.md"