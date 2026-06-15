import streamlit as st

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

    st.title("Build Log AI")
    st.write(
        "Turn GitHub commit activity into weekly build logs, LinkedIn posts, "
        "YouTube updates, TikTok hooks, and portfolio notes."
    )

    st.divider()

    st.subheader("Repository Input")

    github_username = st.text_input("GitHub Username")
    repo_name = st.text_input("Repository Name")

    date_range = st.selectbox(
        "Select activity range",
        options=["Last 7 days", "Last 30 days"],
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
            return

        if not commits:
            st.info("No commits found for this date range.")
            return

        st.success(f"Found {len(commits)} commits.")

        activity_summary = create_activity_summary(commits)


        st.subheader("Activity Summary")
        st.markdown(activity_summary)

        st.subheader("AI Generated Content")

        with st.spinner("Generating AI summaries..."):
            try:
                content_outputs = generate_content_outputs(activity_summary)
            except ValueError as error:
                st.error(str(error))
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