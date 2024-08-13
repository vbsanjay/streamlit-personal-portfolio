import streamlit as st

def social_links():
    st.write("#")
    st.subheader("Connect with me")
    icon_mapping = {
        "GitHub": "fa-brands fa-github",
        "LinkedIn": "fa-brands fa-linkedin",
        "X": "fa-brands fa-x-twitter",
    }
    social_media = {
        "LinkedIn": "http://www.linkedin.com/in/vbsanjay?_l=en_US",
        "GitHub": "https://github.com/vbsanjay/",
        "X": "https://x.com/vbsanjay",
    }
    st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">""", unsafe_allow_html=True)
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        icon = icon_mapping.get(platform, "")
        cols[index].markdown(f'<a href="{link}" target="_blank"><i class="{icon}" style="font-size:24px; margin-right:10px;"></i>{platform}</a>', unsafe_allow_html=True)
