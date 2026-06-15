from datetime import datetime, timedelta, timezone

import requests


GITHUB_API_BASE_URL = "https://api.github.com"


def get_since_date(days: int) -> str:
    """
    Return an ISO 8601 date string for GitHub's 'since' query parameter.

    Args:
        days: Number of days to look back.

    Returns:
        ISO formatted datetime string.
    """
    since_date = datetime.now(timezone.utc) - timedelta(days=days)
    return since_date.isoformat()


def fetch_repo_commits(username: str, repo_name: str, days: int = 7) -> list[dict]:
    """
    Fetch recent commits from a GitHub repository.

    Args:
        username: GitHub username or organization name.
        repo_name: GitHub repository name.
        days: Number of days of commit history to fetch.

    Returns:
        A list of cleaned commit dictionaries.

    Raises:
        ValueError: If GitHub returns an error.
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{username}/{repo_name}/commits"

    params = {
        "since": get_since_date(days),
        "per_page": 100,
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 404:
        raise ValueError("Repository not found. Check the username and repository name.")

    if response.status_code == 403:
        raise ValueError("GitHub API rate limit reached. Try again later or use a GitHub token.")

    if response.status_code != 200:
        raise ValueError(f"GitHub API error: {response.status_code}")

    commits = response.json()

    cleaned_commits = []

    for item in commits:
        commit_data = item.get("commit", {})
        author_data = commit_data.get("author", {})

        cleaned_commits.append(
            {
                "sha": item.get("sha", "")[:7],
                "message": commit_data.get("message", ""),
                "author": author_data.get("name", "Unknown"),
                "date": author_data.get("date", ""),
                "url": item.get("html_url", ""),
            }
        )

    return cleaned_commits