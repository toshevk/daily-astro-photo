import streamlit as st
import smtplib
import ssl


USER_NAME = st.secrets["pymail_user"]
PASSWORD = st.secrets["pymail_pass"]


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465

    receiver = "pymail.automate@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(USER_NAME, PASSWORD)
        server.sendmail(USER_NAME, receiver, user_message)


if __name__ == "__main__":
    send_email("Hello from script")
