import streamlit as st

from src.export import create_export_file_name, create_markdown_export
from src.github_client import fetch_repo_commits
from src.formatter import create_activity_summary
from src.summarizer import generate_content_outputs



def convert_date_range_to_days(date_range: str) -> int:
    """
    Convert the selected date range text into a number of days.
    """
    if date_range == "Last 30 days":
        return 30

    return 7


def main():
    st.set_page_config(
        page_title="Build Log AI",
        page_icon="🛠️",
        layout="wide",
    )
    with st.sidebar:
        st.header("Build Log AI")
        st.write("AI-powered GitHub activity summarizer.")

        st.subheader("Current Features")
        st.write("- Fetch GitHub commits")
        st.write("- Group activity by date")
        st.write("- Generate AI-style summaries")
        st.write("- Export Markdown build logs")

        st.subheader("Mode")
        st.write(
            "Mock AI mode can be enabled in `.env` with `USE_MOCK_AI=true` "
            "to avoid paid API calls during development."
        )
    st.title("Build Log AI")
    st.write(
        "Build Log AI turns GitHub commit activity into weekly developer summaries, "
        "LinkedIn posts, short-form video hooks, and Markdown build logs."
    )

    st.info(
        "Use this tool to document your projects, create proof-of-work content, "
        "and keep a clean record of what you built."
    )

    st.divider()

    st.subheader("1. Choose a GitHub Repository")

    github_username = st.text_input("GitHub Username")
    repo_name = st.text_input("Repository Name")

    date_range = st.selectbox(
        "Select activity range",
        options=["Last 7 days", "Last 30 days"],
    )
    st.caption(
        "Tip: Use a public repository first. Private repositories will need GitHub token support later."
    )
    generate_button = st.button("Fetch GitHub Commits")

    if generate_button:
        if not github_username or not repo_name:
            st.warning("Please enter both a GitHub username and repository name.")
            return

        days = convert_date_range_to_days(date_range)

        try:
            commits = fetch_repo_commits(
                username=github_username,
                repo_name=repo_name,
                days=days,
            )

        except ValueError as error:
            st.error(str(error))
            st.info(
                "Check that the repository is public, the username is correct, "
                "and the repository name matches GitHub exactly."
            )
            return
        

        if not commits:
            st.info("No commits found for this date range.")
            return

        st.success(f"Found {len(commits)} commits.")

        activity_summary = create_activity_summary(commits)


        st.subheader("2. Activity Summary")
        st.markdown(activity_summary)

        st.subheader("3. AI Generated Content")

        with st.spinner("Generating AI summaries..."):
            try:
                content_outputs = generate_content_outputs(activity_summary)
            except ValueError as error:
                st.error(str(error))
                st.info(
                    "If you do not want to use paid API calls, set "
                    "`USE_MOCK_AI=true` in your `.env` file."
                )
                return

        tab_1, tab_2, tab_3 = st.tabs(
            ["Weekly Summary", "LinkedIn Post", "Short Hooks"]
        )

        with tab_1:
            st.markdown(content_outputs["weekly_summary"])

        with tab_2:
            st.text_area(
                "LinkedIn Post",
                value=content_outputs["linkedin_post"],
                height=300,
            )

        with tab_3:
            st.markdown(content_outputs["short_hooks"])
            
        markdown_export = create_markdown_export(
                github_username=github_username,
                repo_name=repo_name,
                date_range=date_range,
                activity_summary=activity_summary,
                weekly_summary=content_outputs["weekly_summary"],
                linkedin_post=content_outputs["linkedin_post"],
                short_hooks=content_outputs["short_hooks"],
                commits=commits,
        )

        export_file_name = create_export_file_name(
                github_username=github_username,
                repo_name=repo_name,
        )
        st.subheader("4. Export")

        st.download_button(
                label="Download Build Log as Markdown",
                data=markdown_export,
                file_name=export_file_name,
                mime="text/markdown",
        )    

        with st.expander("View raw commits"):
            for commit in commits:
                with st.container(border=True):
                    st.write(f"**Message:** {commit['message']}")
                    st.write(f"**Author:** {commit['author']}")
                    st.write(f"**Date:** {commit['date']}")
                    st.write(f"**SHA:** `{commit['sha']}`")
                    st.write(f"[View commit]({commit['url']})")


if __name__ == "__main__":
    main()