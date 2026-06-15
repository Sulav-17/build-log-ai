from src.export import (
    create_export_file_name,
    create_markdown_export,
    format_raw_commits_for_markdown,
)


def test_format_raw_commits_for_markdown_includes_commit_details():
    commits = [
        {
            "message": "add markdown export",
            "sha": "abc123",
            "author": "Sulav",
            "date": "2026-06-14T20:00:00Z",
            "url": "https://example.com/commit",
        }
    ]

    result = format_raw_commits_for_markdown(commits)

    assert "add markdown export" in result
    assert "abc123" in result
    assert "Sulav" in result
    assert "https://example.com/commit" in result


def test_create_markdown_export_includes_all_sections():
    result = create_markdown_export(
        github_username="Sulav-17",
        repo_name="build-log-ai",
        date_range="Last 30 days",
        activity_summary="# Activity Summary",
        weekly_summary="# Weekly Build Summary",
        linkedin_post="LinkedIn content here",
        short_hooks="Hooks content here",
        commits=[],
    )

    assert "# Build Log Export" in result
    assert "## Repository" in result
    assert "## Activity Summary" in result
    assert "## Weekly Build Summary" in result
    assert "## LinkedIn Post" in result
    assert "## Short-Form Video Hooks" in result
    assert "## Raw Commits" in result


def test_create_export_file_name_returns_markdown_file_name():
    result = create_export_file_name("Sulav-17", "Build Log AI")

    assert result == "build-log-sulav-17-build-log-ai.md"