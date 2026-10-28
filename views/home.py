import streamlit as st
import os
import base64
import pandas as pd
import pydeck as pdk 
import streamlit.components.v1 as components
import random
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

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


left_space,con,right_space = st.columns([0.5,3,0.5])

with con:
  col1, col2 = st.columns([2,2])

  with col1:
    st.image("util/Me.jpg", width= "stretch")

  with col2: 
    st.title("Alleah Dela Pena")
    st.subheader("BSCS 3")
    st.write("You can think of me as the rainbow after the rain. "
             "The gum stuck on the bottom of your shoe that you can't get off. "
             "The cloud in 'cloud 9'. "
             "Basically, I am optimistic, persistant, and a dreamer."
            )
    if st.button("Play Playlist", key="bio_button"):
            st.session_state["embed_track_url"] = get_random_spotify_track(MY_TRACK_IDS)

    if st.session_state.get("embed_track_url"):
      st.components.v1.iframe(
          st.session_state["embed_track_url"], height=152, scrolling=False
      )



    

st.divider()


locationL, locationR = st.columns([1,1])

def get_image_base64(img_path):
    if os.path.exists(img_path):
        with open(img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return f"data:image/jpeg;base64,{encoded_string}"
    return "" 

with locationR: 
  entoy = get_image_base64("util/entoy.jpg")
  roro = get_image_base64("util/roro.jpeg")
  bantayan = get_image_base64("util/bantayan.jpeg")
  tenk = get_image_base64("util/10k.jpeg")
  sdsis = get_image_base64("util/sdsic.jpeg")
  buagsong = get_image_base64("util/buagson.jpeg")
  df = pd.DataFrame({
      'lat': [10.2467, 10.24531, 10.2455, 10.2565, 10.2622, 10.2489],
      'lon': [123.9381, 123.95433, 123.9503, 123.9325, 123.9469, 123.9394],
      'name': ["Entoy's Bakasi", "Roro's Night Market", "Bantayan Beach", "10 Thousand Roses", "SDSIS", "Buagsong Elementary School"],
      'loc': [entoy, roro, bantayan, tenk, sdsis, buagsong],
  })

  layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[lon, lat]',
    get_radius=50,
    get_fill_color='[200, 20, 0, 160]',
    pickable=True
  )

  view = pdk.ViewState(
    latitude=10.2507,
    longitude=123.9403,
    zoom=13,
    pitch=50
  
  )

  st.pydeck_chart(
        pdk.Deck(
            layers=[layer],
            initial_view_state=view,
            tooltip={"html": "<b>{name}</b><br/><img src='{loc}' width='150'/>"}, 
        )
    )

with locationL:
  st.header("Where Do I Live?")
  st.write("I’ve lived and grown up in a small town called Cordova, known for abundant fisheries and small town beaches where everybody knows who’s who and what’s new. It has its own kind of comfort of having kind of proximity to people who live here. This is where I mostly spend my elementary to high school education:")

  
  st.write("""
  - <span style = "font-size: 18x; font-weight: bold;"> Elementary School </span>: Buagsong Elementary School
  - <span style = "font-size: 18px; font-weight: bold;"> High School </span>: Saint Dominic International School
  - <span style = "font-size: 18px; font-weight: bold;"> Senior High School </span>: University of Cebu - Lapulapu and Mandaue Campus
  """, unsafe_allow_html=True)
  st.header("Places I usually go to:")
  st.write(""" 
  - <span style = "font-size: 18px; font-weight: bold;"> 10k's Parking Lot </span>
  - <span style = "font-size: 18px; font-weight: bold;"> Roro Port Baywalk </span>
  - <span style = "font-size: 18px; font-weight: bold;"> Dakit-Dakit Baywalk </span>
  """, unsafe_allow_html=True)

  st.write("You gotta have your own spot in a place where everyone knows where you are.")

st.divider()

st.markdown(
    "<h2 style='text-align: center; margin-bottom: 15px;'>What I usually do in"
    " my free time?</h2>",
    unsafe_allow_html=True,
)

pinterest_code = """
<div style="width: 100%; display: flex; justify-content: space-between; align-items: flex-start; gap: 20px; font-family: sans-serif; box-sizing: border-box;">
  
  <!-- Board 1 Column -->
  <div style="flex:1;width: 50%; text-align: justify;">
    <a data-pin-do="embedBoard" 
       data-pin-board-width="auto" 
       data-pin-scale-height="380" 
       data-pin-scale-width="80" 
       href="https://ph.pinterest.com/alleahdelapenauc/with-whom/">
    </a>
    <p style="color: #ddd; font-size: 15px; margin-top: 10px; line-height: 1.4;">
      I usually spend my free time with my friends and family. I love to go out and explore new places, try new food, and just have fun.
    </p>
  </div>

  <!-- Board 2 Column -->
  <div style="flex:1;width: 50%; text-align: justify;">
    <a data-pin-do="embedBoard" 
       data-pin-board-width="auto" 
       data-pin-scale-height="380" 
       data-pin-scale-width="80" 
       href="https://ph.pinterest.com/alleahdelapenauc/pretty/">
    </a>
    <p style="color: #ddd; font-size: 14px; margin-top: 10px; line-height: 1.4;">
      Capturing aesthetic moments, scenery, and things that catch my eye! It's mostly 
      about my motorcycle ( <span style="font-style: italic;">kind of narcissistic but I love her, that's my baby Maaden <333 <span>).
    </p>
  </div>

</div>

<script type="text/javascript">
  (function (d) {
    var f = d.getElementsByTagName('SCRIPT')[0],
      p = d.createElement('SCRIPT');
    p.type = 'text/javascript';
    p.async = true;
    p.src = '//assets.pinterest.com/js/pinit.js';
    f.parentNode.insertBefore(p, f);
  })(document);
</script>
"""

components.html(pinterest_code, height=560, scrolling=False)

st.divider()

st.header("Milestones")
st.write("A lot has happened over the years, but these key milestones are the ones I’ll never forget.")

data = {
    "Year": [2005, 2017, 2021, 2023, 2023, 2024, 2026, 2026],
    "Month": ["September", "April", "July", "May", "August", "June", "July", "August"],
    "Milestone": ["Reborn of the GOAT", "Graduated Elementary", "Graduated Junior Highschool", "Graduated Senior Highschool", "Started College", "Passed Ma'am Cathy's subject", "Passed Discrete and DAA", "Started 3rd year"],
}

df = pd.DataFrame(data)


fig = px.line(
    df,
    x="Year",
    y="Month",
    markers=True,  
    text="Milestone",
    category_orders={
        "Month": [  
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
    },
)


fig.update_traces(
    textposition="top center", textfont=dict(size=12), marker=dict(size=10)
)
fig.update_xaxes(range=[2004, 2027])  

st.plotly_chart(fig, use_container_width=True)

