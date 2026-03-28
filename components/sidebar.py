import streamlit as st

def Sidebar():
    col1, col2, col3 = st.sidebar.columns([1,2,1])
    with col2:
        st.image("./assets/images/sidebar.png", width=70)
    st.sidebar.subheader("Functionalities:")
    option = st.sidebar.selectbox("What you want to generate:", ("Cover Page", "Index", "Assignments"),key="actions")

    return option