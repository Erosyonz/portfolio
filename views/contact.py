import datetime
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    "<h1 style='text-align: left;'>Contact Me</h1>",
    unsafe_allow_html=True,
)
st.write("Feel free to reach out to me through any of the platforms below:")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button(
        "Email Me", 
        "mailto:alleahidelapena@gmail.com", 
        use_container_width=True
    )

with col2:
    st.link_button(
        "Call / Text", 
        "tel:09930064723", 
        use_container_width=True
    )

with col3:
    st.link_button(
        "LinkedIn", 
        "https://ph.linkedin.com/in/alleah-i-dela-pena-832254347", 
        use_container_width=True
    )




if "feedbacks" not in st.session_state:
  st.session_state.feedbacks = [ 
  ]

# Title Section
st.markdown(
    "<h1 style='text-align: left;'>Feedback</h1>",
    unsafe_allow_html=True,
)
st.write("")

col_form, col_display = st.columns([1, 1], gap="large")

with col_form:
  with st.container(border=True):
    st.subheader("Leave Your Feedback")

    with st.form("feedback_form", clear_on_submit=True):
      name = st.text_input(
          "Your Name", placeholder="e.g. John Doe (Optional)"
      )

      category = st.selectbox(
          "Category",
          ["General Feedback", "Bug Report", "Feature Request", "UI/UX Design"],
      )

      rating = st.slider("Rating", min_value=1, max_value=5, value=5)

      message = st.text_area(
          "Your Message",
          placeholder="Write your feedback or suggestions here...",
          height=120,
      )

      submitted = st.form_submit_button(
          "Submit Feedback", use_container_width=True
      )

      if submitted:
        if not message.strip():
          st.error("Please enter a message before submitting.")
        else:
          new_entry = {
              "name": name.strip() if name.strip() else "Anonymous",
              "rating": rating,
              "category": category,
              "message": message.strip(),
              "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
          }
          # Prepend new feedback so latest appears at the top
          st.session_state.feedbacks.insert(0, new_entry)
          st.success("Thank you! Your feedback has been submitted.")
          st.rerun()


with col_display:
  with st.container(border=True):
    st.subheader("Recent Feedback")

    if not st.session_state.feedbacks:
      st.info("No feedback submitted yet. Be the first!")
    else:
      
      avg_rating = sum(f["rating"] for f in st.session_state.feedbacks) / len(
          st.session_state.feedbacks
      )

      m1, m2 = st.columns(2)
      m1.metric("Total Reviews", len(st.session_state.feedbacks))
      m2.metric("Average Rating", f"{avg_rating:.1f} / 5.0")

      st.divider()

      for item in st.session_state.feedbacks:
        stars = "☆" * item["rating"]
        with st.container(border=True):
          st.markdown(
              f"**{item['name']}** &nbsp;•&nbsp; `{item['category']}` &nbsp;•&nbsp; <small>{item['timestamp']}</small>",
              unsafe_allow_html=True,
          )
          st.markdown(f"**Rating:** {stars}")
          st.write(item["message"])