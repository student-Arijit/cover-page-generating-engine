import streamlit as st
from components import *

st.title("Cover page generating Engine")
univ=st.selectbox("Enter your University/college: ", ("University of Calcutta"))
stream=st.selectbox("Enter Your Stream: ", ("B.Sc Honours", "B.com", "B.A"), index=0)
sem=st.selectbox("Enter your semester: ", ("I", "II", "III", "IV", "V", "VI", "VII", "VIII"), index=3)
roll=st.text_input("Enter Your Roll No.: ")
reg=st.text_input("Enter Your Reg No.: ")
paper_name=st.text_input("Enter Your Paper name: ")
sub=st.text_input("Enter Your Subject: ")
paper_code=st.text_input("Enter Your Paper Code: ")

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