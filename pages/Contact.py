import streamlit as st
from random_users import get_users

workers = get_users()
st.header("Meet our team")
col1, col2 = st.columns(2)
with col1:
    for worker in workers[::2]:
        st.subheader(worker['name'])
        st.write(worker['place'])
        st.image(f"pictures/{worker['dob']}.jpg")
        st.write(worker['email'])
with col2:
    for worker in workers[1::2]:
        st.subheader(worker['name'])
        st.write(worker['place'])
        st.image(f"pictures/{worker['dob']}.jpg")
        st.write(worker['email'])
