import streamlit as st

class Assignmentpage:
    def __init__(self):
        st.set_page_config(layout="wide")
        st.set_page_config(page_title="Assignments")
    
    def render_sidebar(self):
        st.sidebar.header("🧭 Navigation")
        self.option = st.sidebar.selectbox("Select Subject", ["Computer Science", "Maths", "Electronics", "Physics"])
        st.sidebar.header("Quick Stat")
        st.sidebar.write("Total Assignment: 1")

    def computer_science(self):
        st.write(f"You selected: {self.option}")
        col1, col2 = st.columns([1, 2])
        with col1:
            with st.container(border=True):
                st.subheader("Semester")
                self.sem = st.pills("Sem:", ["1st sem", "2nd sem", "3rd sem", "4th sem", "5th sem", "6th sem", "7th sem", "8th sem"])
        with col2:
            


    def run(self):
        self.render_sidebar()
        self.computer_science()

a = Assignmentpage()
a.run()