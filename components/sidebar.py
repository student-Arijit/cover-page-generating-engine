from components import icons
import streamlit as st
from streamlit_oauth import OAuth2Component
import requests
import base64
import json

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
        CLIENT_ID = st.secrets["CLIENT_ID"]
        CLIENT_SECRET = st.secrets["CLIENT_SECRET"]
        REDIRECT_URI  = "https://cover-page-generating-engine-wkwnu5xgwg9rgus8eyd2da.streamlit.app/"
        AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
        TOKEN_URL     = "https://oauth2.googleapis.com/token"
        REVOKE_URL    = "https://oauth2.googleapis.com/revoke"

        if "token" not in st.session_state:
            st.session_state.token = None
        if "user" not in st.session_state:
            st.session_state.user = None

        oauth = OAuth2Component(
            CLIENT_ID, CLIENT_SECRET,
            AUTHORIZE_URL, TOKEN_URL,
            TOKEN_URL, REVOKE_URL
        )

        if st.session_state.token is None:
            st.sidebar.markdown("""
                <div class="sidebar-profile">
                    <div class="profile-avatar">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640" width="60">
                            <path d="M463 448.2C440.9 409.8 399.4 384 352 384L288 384C240.6 384
                                    199.1 409.8 177 448.2C212.2 487.4 263.2 512 320 512C376.8 512
                                    427.8 487.3 463 448.2zM64 320C64 178.6 178.6 64 320 64C461.4
                                    64 576 178.6 576 320C576 461.4 461.4 576 320 576C178.6 576 64
                                    461.4 64 320zM320 336C359.8 336 392 303.8 392 264C392 224.2
                                    359.8 192 320 192C280.2 192 248 224.2 248 264C248 303.8 280.2
                                    336 320 336z"/>
                        </svg>
                    </div>
                    <div class="profile-info">
                        <span class="profile-name">Guest</span>
                        <span class="profile-role">Not signed in</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            result = oauth.authorize_button(
                "Login with Google",
                redirect_uri=REDIRECT_URI,
                scope="openid email profile"
            )

            if result and "token" in result:
                token = result["token"]
                st.session_state.token = token

                # ✅ SAFE decode
                try:
                    id_token = token.get("id_token")

                    if id_token:
                        payload = id_token.split(".")[1]
                        payload += "=" * (4 - len(payload) % 4)
                        user = json.loads(base64.urlsafe_b64decode(payload))
                        st.session_state.user = user

                except Exception as e:
                    st.error("Login failed")

                st.rerun()

        else:
            user = st.session_state.user
            if user:
                st.sidebar.markdown(f"""
                <div class="sidebar-profile">
                    <div class="profile-avatar">
                        <img src="{user.get("picture", "")}" width="60" style="border-radius:50%;">
                    </div>
                    <div class="profile-info">
                        <span class="profile-name">{user.get("name", "N/A")}</span>
                        <span class="profile-role">{user.get("email", "N/A")}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("User info not available")
                
            if st.button("Logout"):
                st.session_state.token = None
                st.session_state.user = None
                st.rerun()   
