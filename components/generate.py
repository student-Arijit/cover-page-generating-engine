import streamlit as st
from components.handler import Handler
from components.cover_page_form import Form
from dataclasses import dataclass
import google.generativeai as genai
from weasyprint import HTML
import os
import base64

@dataclass
class GeneratePage(Handler):
    def __init__(self):
        super().__init__()
        self.load_css("assets/style.css")

    def _render_header(self) -> None:
        st.markdown("""
            <div class="page-header">
                <div>
                    <p class="page-title">Cover Page Generator</p>
                    <p class="page-sub">Create content using AI or quick templates</p>
                </div>
                <div class="badge-div">
                    <span class="badge green">● Active</span>
                    <span class="badge blue">✦ Gemini</span>
                </div>
            </div>
                    """,unsafe_allow_html=True)
    
    @st.cache_data
    def _pdf_by_model(self, prompt):
        GEN_AI_API = st.secrets["GEN_AI_API"]
        genai.configure(api_key=GEN_AI_API)
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        html = response.text
        with open("cover.html", "w", encoding="utf-8") as file:
            file.write(html)
        HTML(string=html).write_pdf("cover.pdf")
        os.remove("cover.html")
    
    def _pdf_display(self, pdf):
        with open(pdf, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f"""
            <iframe
                src="data:application/pdf;base64,{base64_pdf}"
                width="100%"
                height="400"
                style="
                    border:none;
                    border-radius:12px;
                ">
            </iframe>
            """
        st.markdown(pdf_display, unsafe_allow_html=True)

    def _left_section(self):
        with st.container(border=True, key="card"):
            st.markdown("""
            <div>
                <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;">
                <span style="font-weight:600;font-size:14px;">📕 Cover Page Generate by AI</span>
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
                            self.history_db()
                            self._pdf_by_model(prompt)
                            st.success("PDF Generated Successfully!")
                        except Exception as e:
                            st.error(f"Error: {e}")
    def _cover_page(self):        
        with st.container(border=True, key="quick-card"):
            st.markdown("""
            <div>
                <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;">
                <span style="font-weight:600;font-size:14px;">📘 Quick Cover Page Generate</span>
            </div>
                """,unsafe_allow_html=True)
            if st.button("Visit"):
                f= Form()
                f.run()

    def _index_page(self)      :
        with st.container(border=True, key="index-card"):
            st.markdown("""
            <div>
                <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;">
                <span style="font-weight:600;font-size:14px;">📃 Index Generate by AI</span>
            </div>
                """,unsafe_allow_html=True)
            
    def run(self):
        self._render_header()
        left, right = st.columns([1.1, 0.9], gap="small")
        with left:
            self._left_section()
        with right:
            with st.container(border=True, key="preview-card"):
                try:
                    self._pdf_display("cover.pdf")
                except:
                    st.subheader("PDF not Generated")
        self._cover_page()