import streamlit as st

def hero_section(profile_pic, pdf_byte):
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)
    with col2:
        st.title("👋🏼 Hello! there, It's Sanjay V B")
        st.write("""
        I’m a software developer with expertise in Python, Django, and SQL, 
        and a solid foundation in data structures and algorithms. I bring a 
        blend of theoretical knowledge and practical project experience.
        """)
        st.download_button(
            label=" 📝 Download Resume",
            data=pdf_byte,
            file_name="Sanjay_Resume_Software_Developer.pdf",
            mime="application/octet-stream"
        )
        st.markdown("[📧 vbsjygiri2040@gmail.com](mailto:vbsjygiri2040@gmail.com)")