"""
Formatting utilities for Build Log AI.

This module will contain helper functions for cleaning commit messages
and formatting generated summaries.
"""


def clean_commit_message(message: str) -> str:
    """
    Remove extra spaces from a commit message.

    Args:
        message: Raw commit message from GitHub.

    Returns:
        Cleaned commit message.
    """
    return message.strip()