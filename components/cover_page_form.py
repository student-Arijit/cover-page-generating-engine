import streamlit as st

class Form:
    def __init__(self):
        st.set_page_config("Cover page Generator")
    
    def student(self):
        st.caption("STUDENT INFO")
        val = {}

        c1, c2 = st.columns(2)
        with c1:
            univ   = st.selectbox("University / College", ["University of Calcutta"])
            val["univ"] = univ
        with c2:
            stream = st.selectbox("Stream", ["B.Sc Honours", "B.Com", "B.A"])
            val["stream"] = stream

        c3, c4, c5 = st.columns(3)
        with c3:
            sem  = st.selectbox("Semester", ["I","II","III","IV","V","VI","VII","VIII"], index=3)
            val["sem"] = sem
        with c4:
            roll = st.text_input("Roll No.", placeholder="e.g. 233423-11-0002")
            val["roll"] = roll
        with c5:
            reg  = st.text_input("Reg. No.", placeholder="e.g. 423-1121-0259-23")
            val["reg"] = reg
        
        return val
        
        
    def paper(self):
        st.caption("PAPER DETAILS")
        val = {}

        c1, c2, c3 = st.columns(3)
        with c1:
            paper_name = st.text_input("Paper Name", placeholder="e.g. Java Programming", key="1")
            val["paper_name"] = paper_name
        with c2:
            sub = st.text_input("Core Subject", placeholder="e.g. C.M.S.M", key="2")
            val["sub"] = sub
        with c3:
            paper_code = st.text_input("Paper Name", placeholder="e.g. DSCC-8", key="3")
            val["pape_code"] = paper_code
        
        return val

    def run(self):
        with st.form("Cover Page Details", clear_on_submit=False):
            student = self.student()
            p = self.paper()
            st.divider()
            c1, c2, c3 = st.columns(3)
            with c3:
                st.form_submit_button("Submit", use_container_width=True)

f = Form()
f.run()