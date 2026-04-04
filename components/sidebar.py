import streamlit as st
from components import icons

class Sidebar:
    def __init__(self):
        st.sidebar.image("./assets/images/sidebar.png", width=50)
        st.sidebar.markdown("""
                <h3 class="sidebar-header">Student Utility Website</h3>
                <a href="https://www.caluniv.ac.in/"><p class="univ-sidebar">University of Calcutta</p></a>
                <hr class="line">
            """, unsafe_allow_html=True)

    def main(self):
        st.sidebar.space(size=5)
        page = st.query_params.get("page", "home")
        st.sidebar.caption("Main")
        
        st.sidebar.markdown(f"""<div class="main-sidebar">
            <a href="?page=home" target="_self"><div class="hover-div"><p>{icons.icon[1]} Home</p></div>
            <a href="?page=generate" target="_self"><div class="hover-div"><p>{icons.icon[2]} Generate&nbsp;&nbsp;<span class="ai-card">&nbsp;{icons.icon[3]}&nbsp;AI&nbsp;&nbsp;</span></p></div>
            <a href="?page=assignments" target="_self"><div class="hover-div"><p>{icons.icon[4]} Assignments</p></div>
            <a href="?page=vault" target="_self"><div class="hover-div"><p>{icons.icon[9]} Personal Vault</p></div>
            <a href="?page=history" target="_self"><div class="hover-div"><p>{icons.icon[5]} History</p></div>
            </div>
            <br><hr class="line"><br>
                            """, unsafe_allow_html=True)
        return page
    
    def contact(self):
        st.sidebar.caption("Contact & Support")
        st.sidebar.markdown(f"""
            <div><p>{icons.icon[6]} About us</p></div>
            <div><p>{icons.icon[7]} Help</p></div>   
               <br><hr class="line"><br>
                            """, unsafe_allow_html=True)
    
    def manage(self):
        st.sidebar.caption("Manage")
        st.sidebar.markdown(f"""
            <div><p>{icons.icon[8]} Settings</p></div>
                            """, unsafe_allow_html=True)

    def account(self):
        st.sidebar.markdown("""
        <div class="sidebar-profile" id="sf">
            <div class="profile-avatar">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640">
                    <path d="M463 448.2C440.9 409.8 399.4 384 352 384L288 384C240.6 384 199.1 409.8 177 448.2C212.2 487.4 263.2 512 320 512C376.8 512 427.8 487.3 463 448.2zM64 320C64 178.6 178.6 64 320 64C461.4 64 576 178.6 576 320C576 461.4 461.4 576 320 576C178.6 576 64 461.4 64 320zM320 336C359.8 336 392 303.8 392 264C392 224.2 359.8 192 320 192C280.2 192 248 224.2 248 264C248 303.8 280.2 336 320 336z"/>
                </svg>
            </div>
            <div class="profile-info">
                <span class="profile-name">Arijit</span>
                <span class="profile-role">Student</span>
            </div>
        </div>
    """, unsafe_allow_html=True)