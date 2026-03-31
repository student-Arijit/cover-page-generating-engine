import streamlit as st

class Sidebar:
    def __init__(self):
        col1, col2, col3 = st.sidebar.columns([1,2,1])
        with col2:
            st.image("./assets/images/sidebar.png", width=70)

    def page(self):
        st.sidebar.subheader("Functionalities:")
        option = st.sidebar.selectbox("What you want to generate:", ("Cover Page", "Index", "Assignments"),key="actions")

        return option
    
    def cover_page_sidebar(self):
        vis = st.sidebar.toggle("University Logo Visible", value=True, help="You want the University logo or not you can select")