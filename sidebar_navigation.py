import streamlit as st

def sidebar_navigation():
    st.sidebar.title("Sanjay's Portfolio")
    subheadings = {"Connect with me":"connect-with-me", 
                   "Skills": "skills", 
                   "Academic Projects": "academic-projects",
                   "Other Experience": "other-experience",
                   "Achievements": "achievements",
                   "Education": "education"
                   }
    for subheading in subheadings:
        st.sidebar.markdown(f"[{subheading}](#{subheadings[subheading]})")