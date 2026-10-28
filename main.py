import streamlit as st
st.set_page_config(layout="wide")

home = st.Page("views/home.py", title="Dela Pena - F2", default=True)
skillP = st.Page("views/skills.py", title="Skills & Projects")
contact = st.Page("views/contact.py", title="Contact Me")

pg = st.navigation(
    [home, skillP, contact], position="top"
)

pg.run()
