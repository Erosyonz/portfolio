import streamlit as st
import os
import pandas as pd
import streamlit.components.v1 as components
import random
import pandas as pd



st.set_page_config(layout="wide")

DATA_FILE = "activity_data.txt"
RESUME_PATH = "util/Resume.pdf"


if "embed_track_url" not in st.session_state:
    st.session_state["embed_track_url"] = None

MY_TRACK_IDS = [
    "2w0UbvgPMhAXxz5qakD9Ms",
    "6VwBbL8CzPiC4QV66ay7oR",
    "1ixNEKbIZTTZ5LIz3rr9jD",
    "1ixNEKbIZTTZ5LIz3rr9jD",
    "2JxPgHghyuG0SKNy8htBWg",
    "0LWIiBYFmOnkqysugp0VKo",
    "236P5yLtfnHgTMxevc0q6F",
]

def get_random_spotify_track(track_ids):
    if track_ids:
        random_track_id = random.choice(track_ids)
        return f"https://open.spotify.com/embed/track/{random_track_id}"
    return None


def load_activity_data():
    """Loads views and likes from file, or sets defaults."""
    data = {"views": 0, "likes": 0}
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                lines = f.read().splitlines()
                if len(lines) >= 2:
                    data["views"] = int(lines[0])
                    data["likes"] = int(lines[1])
        except (ValueError, IndexError):
            pass
    return data

def save_activity_data(views, likes):
    """Saves views and likes to file."""
    with open(DATA_FILE, "w") as f:
        f.write(f"{views}\n{likes}")

if "activity" not in st.session_state:
    st.session_state.activity = load_activity_data()

# Ensure view count increments only once per session
if "view_counted" not in st.session_state:
    st.session_state.view_counted = True
    st.session_state.activity["views"] += 1
    save_activity_data(
        st.session_state.activity["views"], 
        st.session_state.activity["likes"]
    )

if "user_liked" not in st.session_state:
    st.session_state.user_liked = False

activity = st.session_state.activity

home = st.Page("views/home.py", title="About Me", default=True)
skillP = st.Page("views/skills.py", title="Skills & Projects")
contact = st.Page("views/contact.py", title="Contact Me")

pg = st.navigation([home, skillP, contact], position="sidebar")

with st.sidebar:

    tab1, tab2 = st.tabs(["Profile Activity", "Profile Analytics"])

    with tab1:
        st.write("")
        col1, col2 = st.columns(2)

        with col1:
            st.metric(label="Views", value=activity["views"])

        with col2:
            st.metric(label="Likes", value=activity["likes"])

        st.write("")

        if not st.session_state.user_liked:
            if st.button("Like Profile", use_container_width=True):
                activity["likes"] += 1
                st.session_state.user_liked = True
                save_activity_data(activity["views"], activity["likes"])
                st.rerun()
        else:
            if st.button("Unlike Profile", use_container_width=True, type="primary"):
                activity["likes"] = max(0, activity["likes"] - 1)
                st.session_state.user_liked = False
                save_activity_data(activity["views"], activity["likes"])
                st.rerun()

    with tab2:
        st.write("Detailed breakdown of portfolio engagement activity:")

        views = activity["views"]
        likes = activity["likes"]
        engagement_rate = f"{(likes / views * 100):.1f}%" if views > 0 else "0.0%"

        df_table = pd.DataFrame({
            "Metric": ["Profile Views", "Profile Likes", "Engagement Rate"],
            "Count / Value": [views, likes, engagement_rate]
        })

        st.dataframe(
            df_table, 
            use_container_width=True, 
            hide_index=True
        )

    st.divider()

    button_label = (
        "Shuffle Music" if st.session_state.get("embed_track_url") else "Play Music"
    )

    if st.button(button_label, key="bio_button", use_container_width=True):
        st.session_state["embed_track_url"] = get_random_spotify_track(MY_TRACK_IDS)

    if st.session_state.get("embed_track_url"):
        st.components.v1.iframe(
            st.session_state["embed_track_url"], height=152, scrolling=False
        )
        
    if os.path.exists(RESUME_PATH):
        with open(RESUME_PATH, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        
        st.download_button(
            label="Download Resume",
            data=pdf_bytes,
            file_name="Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.warning("Resume file not found.")

    st.markdown(
            "<p style='color: gray; font-size: 0.9rem;'>Alleah Dela Pena | BSCS | F2 |</p>", 
            unsafe_allow_html=True
        )
pg.run()