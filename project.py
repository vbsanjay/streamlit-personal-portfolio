import streamlit as st
import requests

# function to fetch project from my git hub
def projects():
    GITHUB_USERNAME = 'vbsanjay'
    project_list = ['Python-Django-DevSearch', 'streamlit-personal-portfolio']
    url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos'

    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            if repo['name'] in project_list:
                topic_string = ""
                with st.expander(f"🔥 {repo['name']}"):
                    st.link_button("Check code here",repo['html_url'])
                    st.write(repo["description"])
                    for topic in repo['topics']:
                        topic_string += f"#{topic}  "
                    st.info(topic_string)
    else:
        print(f"Failed to retrieve repositories: {response.status_code}")