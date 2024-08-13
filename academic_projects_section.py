import streamlit as st
from project import projects

def academic_projects_section():
    st.write("#")
    st.subheader("Academic Projects")
    projects()