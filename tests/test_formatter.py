from src.formatter import (
    clean_commit_message,
    create_activity_summary,
    format_commit_date,
    group_commits_by_date,
)


def test_clean_commit_message_removes_extra_spaces():
    message = "   add github client setup   "

    result = clean_commit_message(message)

    assert result == "add github client setup"


def test_clean_commit_message_uses_first_line_only():
    message = "add github client\n\nextra details here"

    result = clean_commit_message(message)

    assert result == "add github client"


def test_format_commit_date_returns_simple_date():
    date_value = "2026-06-14T20:45:12Z"

    result = format_commit_date(date_value)

    assert result == "2026-06-14"


def test_group_commits_by_date_groups_correctly():
    commits = [
        {
            "message": "add app layout",
            "author": "Sulav",
            "date": "2026-06-14T20:45:12Z",
            "sha": "abc123",
            "url": "https://example.com/1",
        },
        {
            "message": "fix button bug",
            "author": "Sulav",
            "date": "2026-06-14T21:10:00Z",
            "sha": "def456",
            "url": "https://example.com/2",
        },
    ]

    result = group_commits_by_date(commits)

    assert "2026-06-14" in result
    assert len(result["2026-06-14"]) == 2


def test_create_activity_summary_returns_markdown():
    commits = [
        {
            "message": "add github fetcher",
            "author": "Sulav",
            "date": "2026-06-14T20:45:12Z",
            "sha": "abc123",
            "url": "https://example.com/1",
        }
    ]

    result = create_activity_summary(commits)

    assert "# Activity Summary" in result
    assert "## 2026-06-14" in result
    assert "- add github fetcher" in result