import streamlit as st

def Sidebar():
    col1, col2, col3 = st.sidebar.columns([1,2,1])
    with col2:
        st.image("./assets/images/sidebar.png", width=70)

    st.markdown("""
<style>
/* Target the selectbox */
div[data-baseweb="select"] > div {
    border: 1px solid black !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)
    st.sidebar.subheader("Functionalities:")
    option = st.sidebar.selectbox("What you want to generate:", ("Cover Page", "Index", "Assignments"),key="actions")

    return option