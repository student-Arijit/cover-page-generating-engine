import streamlit as st
from components.handler import Handler
from dataclasses import dataclass
import google.generativeai as genai
from xhtml2pdf import pisa
import os

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
                    <span class="badge blue">✦ Gemini</span>
                </div>
            </div>
                    """,unsafe_allow_html=True)
        
    def _pdf_by_model(self, prompt):
        GEN_AI_API = st.secrets["GEN_AI_API"]
        genai.configure(api_key=GEN_AI_API)
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        html = response.text
        with open("cover.html", "w", encoding="utf-8") as file:
            file.write(html)
        with open("cover.pdf", "wb") as pdf:
            pisa.CreatePDF(html, dest=pdf)  
        os.remove("cover.html")

    def _left_section(self):
        st.markdown("""
            <div class="card">
                <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;">
                <span style="font-weight:600;font-size:14px;">Generate by AI</span>
                <span class="badge blue">✦ AI</span>
            </div>
                """,unsafe_allow_html=True)

        st.markdown('<p class="label">Prompt</p>', unsafe_allow_html=True)
        prompt = st.text_area(
                label="prompt",
                label_visibility="collapsed",
                placeholder="Describe what you want to generate…",
                height=108,
                key="ai_prompt",
            )

        generate = st.button("Generate PDF")

        if generate:

            if not prompt.strip():
                st.warning("Enter a prompt first.")

            else:
                with st.spinner("Building PDF..."):

                    try:
                        self._pdf_by_model(prompt)

                        st.success("PDF Generated Successfully!")

                        with open("cover.pdf", "rb") as pdf_file:

                            st.download_button(
                                label="Download PDF",
                                data=pdf_file,
                                file_name="cover.pdf",
                                mime="application/pdf"
                            )

                    except Exception as e:
                        st.error(f"Error: {e}")
                

    def run(self):
        self._render_header()
        left, right = st.columns([1.1, 0.9], gap="large")
        with left:
            self._left_section()