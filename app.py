import streamlit as st
from components import *

st.set_page_config(
    "cover-page-generating-engine",
    page_icon = "📘"
)

#Sidebar Functionalities
sidebar.Sidebar()

st.title("Cover Page Generating Engine:")
st.subheader("Information Form:")

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
        if not all([roll, reg, paper_name, sub, paper_code]):
            st.error("⚠️ Please fill all fields before submitting.")
        else:
            # Save all inputs to session state
            st.session_state["form_data"] = {
                "univ": univ,
                "stream": stream,
                "sem": sem,
                "roll": roll,
                "reg": reg,
                "paper_name": paper_name,
                "sub": sub,
                "paper_code": paper_code,
            }
            st.success("Your Form is submitted. Please choose your design below.")
    
st.subheader("🎨 Choose your designs here:")

if "form_data" in st.session_state:
    data = st.session_state["form_data"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/images/template1.png", caption="Template 1")
        if st.button("Generate PDF", key="template1"):
            template1.cover_page(
                data["stream"], data["sem"], data["univ"], data["roll"],
                data["reg"], data["paper_name"], data["paper_code"], data["sub"]
            )

    with col2:
        if st.button("Generate PDF", key="template2"):
            template2.cover_page(
                data["stream"], data["sem"], data["univ"], data["roll"],
                data["reg"], data["paper_name"], data["paper_code"], data["sub"]
            )
else:
    st.info("📝 Please submit the form above to unlock the design section.")