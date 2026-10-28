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
    st.session_state.feedbacks = []

st.markdown(
    "<h1 style='text-align: left;'>Feedback & Inquiries</h1>",
    unsafe_allow_html=True,
)
st.write("")

col_form, col_display = st.columns([1, 1], gap="large")

with col_form:
    with st.container(border=True):
        st.subheader("Leave Your Feedback")

        with st.form("feedback_form", clear_on_submit=True):
            # 1. Text Input
            name = st.text_input(
                "Your Name", placeholder="e.g. John Doe (Optional)"
            )

            # 2. Selectbox
            category = st.selectbox(
                "Category",
                ["General Feedback", "Project Collaboration", "Bug Report", "UI/UX Design"],
            )

            # 3. Multiselect (or Radio)
            topics = st.multiselect(
                "What areas caught your interest?",
                ["Full-Stack Web Apps", "Mobile Development", "Database Architecture", "UI Design & Portfolio Layout"]
            )

            # 4. Radio
            contact_preference = st.radio(
                "Preferred Follow-up Method",
                ["Email", "Phone / Text", "No follow-up needed"],
                horizontal=True
            )

            # 5. Slider
            rating = st.slider("Rating", min_value=1, max_value=5, value=5)

            # 6. Text Area
            message = st.text_area(
                "Your Message",
                placeholder="Write your feedback, project inquiry, or suggestions here...",
                height=120,
            )

            # 7. Checkbox
            subscribe = st.checkbox("Subscribe to portfolio update alerts")

            # 8. Button (Form Submit Button)
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
                        "topics": topics,
                        "contact_preference": contact_preference,
                        "message": message.strip(),
                        "subscribe": subscribe,
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
                stars = "★" * item["rating"] + "☆" * (5 - item["rating"])
                with st.container(border=True):
                    st.markdown(
                        f"**{item['name']}** &nbsp;•&nbsp; `{item['category']}` &nbsp;•&nbsp; <small>{item['timestamp']}</small>",
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"**Rating:** {stars}")
                    if item["topics"]:
                        st.markdown(f"**Interests:** {', '.join(item['topics'])}")
                    st.write(item["message"])
                    if item["subscribe"]:
                        st.caption("Subscribed to updates")