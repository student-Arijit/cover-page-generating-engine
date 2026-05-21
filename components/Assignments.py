import streamlit as st
from components.handler import Handler
from components.cover_page_form import Form
from supabase import create_client
from dataclasses import dataclass
import google.generativeai as genai
from weasyprint import HTML
import os
import base64

@dataclass
class AssignmentGeneratePage(Handler):
    def __init__(self):
        self.load_css("assets/style.css")
    
    def _render_header(self) -> None:
        st.markdown("""
            <div class="page-header">
                <div>
                    <p class="page-title">Assignment Generator</p>
                    <p class="page-sub">Create a project using AI</p>
                </div>
                <div class="badge-div">
                    <span class="badge green">● Active</span>
                    <span class="badge blue">✦ Gemini</span>
                </div>
            </div>
                    """,unsafe_allow_html=True)
    
    def run(self):
        self._render_header()