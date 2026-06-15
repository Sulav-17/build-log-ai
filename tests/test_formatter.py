from src.formatter import clean_commit_message


def test_clean_commit_message_removes_extra_spaces():
    message = "   add github client setup   "

    result = clean_commit_message(message)

    assert result == "add github client setup"