import streamlit as st
from pathlib import Path
from supabase import create_client
from datetime import datetime
import time

class Handler:
    def __init__(self):
        _SUPABASE_URI = st.secrets["_SUPABASE_URI"]
        _SUPABASE_KEY = st.secrets["_SUPABASE_KEY"]
        self.supabase = create_client(_SUPABASE_URI, _SUPABASE_KEY)

    def _read_file(self, file_path) -> str:
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found {path}")
        
        return path.read_text(encoding="UTF-8")

    def load_css(self, file_path) -> None:
        try:
            css_content = self._read_file(file_path)
            st.markdown(
                f"<style>{css_content}</style>", 
                unsafe_allow_html=True
            )
        
        except FileNotFoundError as e:
            st.error(f"Failed to load CSS File: {e}")
    
    def user_db(self) -> None:
        try:
            id = st.session_state.user["sub"]
            name = st.session_state.user["given_name"]
            email = st.session_state.user["email"]

            if id is None:
                return

            response = (
                self.supabase
                .table("users")
                .select("*")
                .eq("id", id)
                .execute()
            )

            if not response.data:
                data = {
                    "id": id,
                    "name": name,
                    "email": email
                }

                placeholder = st.empty()
                self.supabase.table("users").insert(data).execute()
                placeholder.success("Logged in")
                time.sleep(2)
                placeholder.empty()


        except (AttributeError, TypeError):
            pass
    
    def history_db(self):
        try:    
            user = st.session_state.get("user")
            if not user:
                return
            user_id = user.get("sub")
            data = {
                "id": user_id,
                "created_at": f"{datetime.now()}",
                "url": "cover page created"
            }
            self.supabase.table("history").insert(data).execute()

        except (AttributeError, TypeError):
            pass