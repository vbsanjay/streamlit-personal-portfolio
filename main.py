from academic_projects_section import academic_projects_section
from achievements_section import achievements_section
from education_section import education_section
from experience_section import experience_section
from get_path import get_paths
from hero_section import hero_section
from load_assets import load_assets
from sidebar_navigation import sidebar_navigation
from skill_section import skills_section
from social_links import social_links
import streamlit as st

def main():
    st.set_page_config(page_title="Sanjay's Portfolio", page_icon=":wave:")
    paths = get_paths()
    pdf_byte, profile_pic = load_assets(paths)
    sidebar_navigation()
    hero_section(profile_pic, pdf_byte)
    social_links()
    skills_section()
    academic_projects_section()
    experience_section()
    achievements_section()
    education_section()

if __name__ == "__main__":
    main()