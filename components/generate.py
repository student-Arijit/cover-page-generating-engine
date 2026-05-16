import streamlit as st
from components.handler import Handler
from dataclasses import dataclass

@dataclass
class GeneratePage(Handler):
    def __init__(self):
        self.load_css("assets/style.css")

    def _render_header(self) -> None:
        st.markdown("""
            <div class="page-header">
                <div>
                    <p class="page-title">Generator</p>
                    <p class="page-sub">Create content using AI or quick templates</p>
                </div>
                <div class="badge-div">
                    <span class="badge green">● Active</span>
                    <span class="badge blue">GPT-4o</span>
                </div>
            </div>
                    """,unsafe_allow_html=True)

    def run(self):
        self._render_header()