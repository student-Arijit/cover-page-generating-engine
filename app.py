import streamlit as st
from components import *

st.set_page_config(
    "cover-page-generating-engine",
    page_icon = "📘"
)
st.title("Cover Page Generating Engine:")
st.subheader("Information Form:")

st.error("developers are working, no functionality happens sorry😔")

with st.form("About Form", clear_on_submit = False):
    st.subheader("Student About:")

    col1, col2 = st.columns(2)

    with col1:
        univ=st.selectbox("Enter your University/college: ", ("University of Calcutta"))
        stream=st.selectbox("Enter Your Stream: ", ("B.Sc Honours", "B.com", "B.A"), index=0)

    with col2:
        sem=st.selectbox("Enter your semester: ", ("I", "II", "III", "IV", "V", "VI", "VII", "VIII"), index=3)
        roll=st.text_input("Enter Your Roll No.: ")
        reg=st.text_input("Enter Your Reg No.: ")

    st.subheader("Paper Details:")
    paper_name=st.text_input("Enter Your Paper name: ")
    sub=st.text_input("Enter Your Subject: ")
    paper_code=st.text_input("Enter Your Paper Code: ")

    col1, col2, col3 = st.columns([1, 0.5, 1])

    with col2:
        submit = st.form_submit_button("Submit")

    if submit:
        st.success("Your Form submitted. Please, choose your design and download.")    

st.subheader("Choose your designs here:")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/images/template1.png")
    if st.button("Generate PDF", key = "template1"):
        template1.cover_page(stream, sem, univ, roll, reg, paper_name, paper_code, sub)

with col2:
    if st.button("Generate PDF", key = "template2"):
        template2.cover_page(stream, sem, univ, roll, reg, paper_name, paper_code, sub)

with col3:
    st.write("working")