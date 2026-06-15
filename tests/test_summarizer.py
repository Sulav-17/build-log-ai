from src.summarizer import fill_prompt_template, load_prompt_template


def test_load_prompt_template_reads_file():
    template = load_prompt_template("weekly_summary.txt")

    assert "weekly developer summary" in template.lower()
    assert "{activity_summary}" in template


def test_fill_prompt_template_replaces_activity_summary():
    template = "Summarize this activity:\n\n{activity_summary}"
    activity_summary = "# Activity Summary\n\n- add GitHub fetcher"

    result = fill_prompt_template(template, activity_summary)

    assert "{activity_summary}" not in result
    assert "# Activity Summary" in result
    assert "- add GitHub fetcher" in result