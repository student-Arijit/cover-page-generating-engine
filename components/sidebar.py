import streamlit as st

def Sidebar():
    st.sidebar.subheader("Functionalities:")
    option = st.sidebar.selectbox("What you want to generate:", ("Cover Page", "Index", "Invitation card"))

    return option