import streamlit as st

def sidebar_navigation():
    st.sidebar.title("Sanjay's Portfolio")
    subheadings = ["Connect-with-me", "Skills", "Academic-Projects"]
    for subheading in subheadings:
        st.sidebar.markdown(f"[{subheading}](#{subheading.lower()})")