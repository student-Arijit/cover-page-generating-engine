import streamlit as st
from components import *

st.set_page_config(
    "cover-page-generating-engine",
    page_icon = "📘"
)

#Sidebar Functionalities
option = sidebar.Sidebar()

if option == "Cover Page":
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
            submit = st.form_submit_button("Submit", key="cover_page_submit")

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

elif option == "Index":
    st.header("INDEX Generator:")

    if "stack" not in st.session_state:
        st.session_state["stack"] = []
    if "count" not in st.session_state:
        st.session_state["count"] = 1
        
    with st.form("Index form", clear_on_submit=True):
        st.subheader("Enter the Details:")
        coli, colii = st.columns(2)

        with coli:
            assignment_name = st.text_input("Enter Assignment Name:")
        
        with colii:
            page = st.text_input("Enter Page Number:")

        coliii, coliv = st.columns(2)

        with coliii:
            code_date = st.text_input("Enter Code Date:")

        with coliv:
            approve_date = st.text_input("Enter Approval Date:")
            
        submit_data = st.form_submit_button("Submit", key="index_submit")

        if submit_data:
            count = st.session_state["count"]
            subdata = [str(count), assignment_name, code_date, approve_date, page, " "]
            st.session_state["stack"].append(subdata)
            st.session_state["count"] += 1
            st.badge("Success", color="green")

    if st.button("Get PDF"):
        index.Index(st.session_state["stack"])
        
else:
    st.error("404! page not found")