import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
API_URL = os.getenv("api_url")

request = requests.get(API_URL)
data = request.json()

print(data)
title = data["title"]
date = data["date"]
explanation = data["explanation"]

img_url = data["url"]
image = requests.get(img_url)

with open("apod.jpg", "wb") as file:
    file.write(image.content)

st.header("Astrology Photo of the day")
st.subheader(title)
st.write(date)
st.image("apod.jpg")
st.write(explanation)
