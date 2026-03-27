import streamlit as st

class Assignmentpage:
    def __init__(self):
        st.set_page_config(layout="wide")
        st.set_page_config(page_title="Assignments")
        self.actions = [
            "1st sem",
            "2nd sem",
            "3rd sem",
            "4th sem",
            "5th sem", 
            "6th sem",
            "7th sem",
            "8th sem"
        ]
    
    def render_sidebar(self):
        st.sidebar.header("🧭 Navigation")
        self.option = st.sidebar.selectbox("Select Subject", ["Computer Science", "Maths", "Electronics", "Physics"])
        st.sidebar.header("Quick Stat")
        st.sidebar.write("Total Assignment: 1")

    def computer_science(self):
        st.subheader("Computer Science Assignments:")
        col1, col2 = st.columns([1, 2])
        with col1:
            with st.container(border=True):
                st.subheader("Semester")
                self.cs_sem = st.pills(
                    "",
                    self.actions,
                    selection_mode="single")
        with col2:
            with st.container(border=True):
                match self.cs_sem:
                    case "1st sem":
                        st.write("1st sem Computer Science Assignment")

                    case "2nd sem":
                        st.write("2nd sem Computer Science Assignment")

                    case "3rd sem":
                        st.write("3rd sem Computer Science Assignment")

                    case "4th sem":
                        st.write("4th sem Computer Science Assignment")
                        
                        st.write("DSCC-5: Computational Mathematics")
                        col3, col4 = st.columns([0.5,2], gap="small")
                        with col3:
                            st.image("./assets/images/comp_math.png", width=100)
                        with col4:
                            st.download_button(
                                label="📄 Download Project",
                                data=open("./assets/asgn_pdfs/Computational_Math.pdf", "rb").read(),
                                file_name = "DSCC-5.pdf",
                                mime = "application/pdf")
                            
                    case "5th sem":
                        st.write("5th sem Computer Science Assignment")

                    case "6th sem": 
                        st.write("6th sem Computer Science Assignment")

                    case "7th sem":                        
                        st.write("7th sem Computer Science Assignment")

                    case "8th sem":                        
                        st.write("8th sem Computer Science Assignment")
                    
                    case _:
                        st.write("Select a semester to view assignments.")


    def run(self):
        self.render_sidebar()
        self.computer_science()

a = Assignmentpage()
a.run()