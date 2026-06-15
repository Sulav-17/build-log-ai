import streamlit as st


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

    generate_button = st.button("Generate Build Log")

    if generate_button:
        if not github_username or not repo_name:
            st.warning("Please enter both a GitHub username and repository name.")
            return

        st.success("Inputs received successfully.")

        st.write("### Selected Repository")
        st.write(f"GitHub Username: `{github_username}`")
        st.write(f"Repository Name: `{repo_name}`")
        st.write(f"Date Range: `{date_range}`")

        st.info("GitHub API fetching will be added in the next milestone.")


if __name__ == "__main__":
    main()