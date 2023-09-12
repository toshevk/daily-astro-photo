import streamlit as st

st.set_page_config(layout="wide")
st.title("Our Team")
st.subheader("Krste Tošev")

column1, column2 = st.columns(2)

with column1:
    st.image("images/photo.jpg", width=400)

with column2:
    content = """
    Hello, I am Krste!\n
    I am a Python programmer, a salesman, and a Booking.com host!\n
    I studied Informatics and Computer Science in Skopje, Macedonia.
    I have worked hundreds of different sales and marketing jobs,
    and I have even worked on films in 3D industry for 3 years!\n
    My passion for programming led me to learn Python and SQL, which is only the beginning!
    Studying informatics never ends, so I enrolled in a course for Python programming,
    and this is the result from that course.\n
    I am also a host on Booking in my house in Gevgelija, Macedonia.
    I love meeting people from everywhere, so please feel free to contact me when you are in
    my lovely country Macedonia, so we can have a coffee and a chat!
    """
    st.info(content)
    st.info("You can check out my projects at https://github.com/toshevk")
