import streamlit as st
import pandas
from send_email import send_email


topics_df = pandas.read_csv("topics.csv")
st.set_page_config(layout="wide")
st.header("Contact Me")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address")
    message_topic = st.selectbox("What topic do you wish to discuss?",
                                 placeholder="Select topic", options=topics_df)
    user_message = st.text_area("Your message")
    message_comp = f"""\
Subject: {user_email} wants to contact you!

From: {user_email}
Topic: {message_topic}
Message: {user_message}
"""
    button = st.form_submit_button("Send message")
    if button:
        send_email(message_comp)
        st.info("Thank you for contacting us! "
                "We will get back to you as soon as possible!")
