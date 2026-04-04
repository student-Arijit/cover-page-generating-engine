import streamlit as st
from components import *

st.error("app on maintanance")

handler.load_css("assets/style.css")
o = sidebar.Sidebar()
o.main()
o.contact()
o.manage()
o.account()



"""if option == "Cover Page":
    o.cover_page_sidebar()
    st.title("Cover Page Generating Engine:")
    st.subheader("Information Form:")

    form = cover_page_form.Form()
    form.run()
    
    st.subheader("🎨 Choose your designs here:")

    if "cover_page_details" in st.session_state:
        col1, col2, col3 = st.columns(3)

        details = st.session_state["cover_page_details"]
        
        with col1:
            st.image("assets/images/template1.png", caption="Template 1")
            if st.button("Generate PDF", key="template1"):
                t=template.Template()
                t.template1(
                    details["stream"], details["sem"], details["univ"], details["roll"],
                    details["reg"], details["paper_name"], details["paper_code"], details["sub"]
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

        #coliii, coliv = st.columns(2)

        #with coliii:
            #code_date = st.text_input("Enter Code Date:")

       # with coliv:
            #approve_date = st.text_input("Enter Approval Date:")
            
        submit_data = st.form_submit_button("Submit", key="index_submit")

        if submit_data:
            count = st.session_state["count"]
            subdata = [str(count), assignment_name,  page, " "] #code_date, approve_date,
            st.session_state["stack"].append(subdata)
            st.session_state["count"] += 1
            st.badge("Success", color="green")

    if st.button("Get PDF"):
        index.Index(st.session_state["stack"])    

elif option == "Assignments":
    a = Assignments.Assignmentpage()
    a.run()

       
else:
    st.error("404! page not found")"""