import pandas as pd
import streamlit as st


st.set_page_config(layout="wide")

left, center, right = st.columns([1, 2, 1])
with center:
  st.markdown(
        "<h1 style='text-align: center;'>Skills & Projects</h1>",
        unsafe_allow_html=True,
    )


with st.container(border=True):
    st.subheader("Soft Skills")
    
    # Use numeric scores for st.bar_chart
    data = pd.DataFrame({
        'Skill': ['Communication', 'Teamwork', 'Problem-Solving', 'Adaptability', 'Leadership'],
        'Proficiency Level (%)': [80, 100, 85, 90, 88]
    })

    
    st.bar_chart(
        data.set_index('Skill'), 
        height=600,
        x_label = "Soft Skills",
        y_label="Proficiency level"
        )


st.divider()


st.subheader("Hard Skills")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("### C")
        st.metric(label="Active Developer", value="1 Project", delta="+1")

with col2:
    with st.container(border=True):
        st.markdown("### C++")
        st.metric(label="Active Developer", value="3 Projects", delta="+2")

with col3:
    with st.container(border=True):
        st.markdown("### C#")
        st.metric(label="Active Developer", value="2 Projects", delta="+3")



col4, col5, col6 = st.columns(3)

with col4:
    with st.container(border=True):
        st.markdown("### kotlin")
        st.metric(label="Active Developer", value="2 Projects", delta="+2")

with col5:
    with st.container(border=True):
        st.markdown("### Java")
        st.metric(label="Active Developer", value="3 Projects", delta="+2")

with col6:
    with st.container(border=True):
        st.markdown("### Python")
        st.metric(label="Active Developer", value="5 Projects", delta="+4")


st.divider()

st.header("Projects")


projL, projC, projR = st.columns(3)

with projL:
    with st.container(border=True):
        st.image("util/civic.jpeg", use_container_width=True)
        st.subheader("CivicGuard")
        st.write("CivicGuard is a JavaFX desktop application built to bring order and transparency to disaster response operations in Cebu City. It replaces error-prone, paper-based workflows with a single shared MariaDB database that LGU staff, barangay officials, and the public all draw from in real time.")
        st.write("")
        st.markdown("**Role:** Frontend Developer")
        st.markdown("**Tech Stack:** JavaFX, Java, MariaDB, Scene Builder")
        st.link_button("CivicGuard", "https://github.com/kworuu/CivicGuard")
        
with projC:
    with st.container(border=True):
        st.image("util/equipl.jpeg", use_container_width=True)
        st.subheader("EquipLink")
        st.write("EquipLink is a web-based school laboratory equipment borrowing and inventory management system designed to streamline equipment tracking between students and department administrators.")
        st.write("")
        st.markdown("**Role:** Full Stack Developer")
        st.markdown("**Tech Stack:** HTML, PHP, CSS, JavaScript, MySQL")
        st.link_button("EquipLink", "https://github.com/Erosyonz/EquipLink")

with projR:
    with st.container(border=True):
        st.image("util/saag.jpeg", use_container_width=True)
        st.subheader("SA-AG")
        st.write("SA-AG is a hiking trail discovery and route-sharing platform designed for outdoor enthusiasts to build custom hiking paths, mark notable waypoints along their journeys, and explore trails shared by the community.")
        st.write("")     
        st.markdown("**Role:** Full Stack Developer")
        st.markdown(
            "**Tech Stack:** Python, Django, Tailwind CSS, Leaflet.js, Supabase"
        )
        st.link_button("SA-AG", "https://github.com/Erosyonz/SAAG")