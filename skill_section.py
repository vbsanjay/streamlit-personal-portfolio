import streamlit as st

def skills_section():
    st.write("#")
    st.subheader("Skills")
    skills = [
        "Python", "Java", "Django", "REST APIs", "HTML", "CSS",
        "SQL", "Django ORM", "Git", "GitHub", "LLD", "Design Principles",
        "OOPS", "DSA", "JIRA", "Linux"
    ]
    num_columns = 3
    columns = st.columns(num_columns)
    for i, skill in enumerate(skills):
        col_index = i % num_columns
        with columns[col_index]:
            st.markdown(f'<div class="fake-button">{skill}</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
