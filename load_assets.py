from pathlib import Path
import streamlit as st
from PIL import Image

def load_assets(paths):
    with open(paths["css_file"]) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(paths["resume_file"], "rb") as pdf_file:
        pdf_byte = pdf_file.read()
    profile_pic = Image.open(paths["profile_pic"])
    return pdf_byte, profile_pic