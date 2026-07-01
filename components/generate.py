import streamlit as st
from components.handler import Handler
from components.cover_page_form import Form
from dataclasses import dataclass
import google.generativeai as genai
from weasyprint import HTML
from datetime import date
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
        st.markdown(
            """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500&family=IBM+Plex+Mono:wght@400;500&display=swap');
        
            .block-container { padding-top: 3rem; padding-bottom: 4rem; max-width: 1180px; }
        
            /* ---------- Hero ---------- */
            .bp-tag {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.6rem;
                font-family: 'IBM Plex Mono', monospace;
                font-size: 0.72rem;
                letter-spacing: 0.28em;
                text-transform: uppercase;
                color: #6FB8FF;
                margin-bottom: 1.1rem;
            }
            .bp-tag::before, .bp-tag::after {
                content: "";
                width: 26px; height: 1px;
                background: #2A4A6B;
            }
            .bp-title {
                font-family: 'Space Grotesk', sans-serif;
                font-weight: 700;
                font-size: 3rem;
                text-align: center;
                color: #EAF3FF;
                line-height: 1.18;
                margin: 0;
            }
            .bp-title span { color: #6FB8FF; }
            .bp-sub {
                text-align: center;
                color: #5C7A99;
                font-size: 1rem;
                max-width: 540px;
                margin: 1.1rem auto 0 auto;
                line-height: 1.6;
            }
            .bp-divider {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                margin: 2.6rem 0 2.4rem 0;
                color: #2A4A6B;
                font-family: 'IBM Plex Mono', monospace;
                font-size: 0.68rem;
                letter-spacing: 0.2em;
            }
            .bp-divider .seg { width: 120px; height: 1px; background: repeating-linear-gradient(90deg, #2A4A6B 0 6px, transparent 6px 11px); }
        
            /* ---------- Card ---------- */
            div[data-testid="column"] { padding: 0 0.55rem; }
        
            .bp-card {
                position: relative;
                background: #0E1E33;
                border: 1px solid #1C3754;
                padding: 1.7rem 1.5rem 1.5rem 1.5rem;
                min-height: 320px;
                transition: border-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
            }
            .bp-card:hover {
                border-color: #6FB8FF;
                transform: translateY(-2px);
                box-shadow: 0 0 0 1px rgba(111,184,255,0.15), 0 18px 30px -20px rgba(111,184,255,0.25);
            }
            /* registration crop marks, all four corners */
            .bp-card .crop { position: absolute; width: 10px; height: 10px; }
            .bp-card .crop::before, .bp-card .crop::after { content:""; position:absolute; background:#3D6690; }
            .bp-card .crop::before { width: 10px; height: 1px; top: 0; left: 0; }
            .bp-card .crop::after  { width: 1px; height: 10px; top: 0; left: 0; }
            .bp-card .crop.tl { top: -1px; left: -1px; }
            .bp-card .crop.tr { top: -1px; right: -1px; transform: scaleX(-1); }
            .bp-card .crop.bl { bottom: -1px; left: -1px; transform: scaleY(-1); }
            .bp-card .crop.br { bottom: -1px; right: -1px; transform: scale(-1,-1); }
        
            .bp-fig {
                font-family: 'IBM Plex Mono', monospace;
                font-size: 0.68rem;
                letter-spacing: 0.14em;
                color: #4A739A;
                display: flex;
                justify-content: space-between;
                margin-bottom: 1.2rem;
            }
            .bp-fig .rev { color: #3D6690; }
        
            .bp-icon { margin-bottom: 1.1rem; }
            .bp-icon svg { display: block; }
        
            .bp-title-card {
                font-family: 'Space Grotesk', sans-serif;
                font-weight: 600;
                font-size: 1.32rem;
                color: #EAF3FF;
                margin-bottom: 0.55rem;
            }
        
            .bp-desc {
                color: #7E9CBA;
                font-size: 0.89rem;
                line-height: 1.55;
                margin-bottom: 1.3rem;
                min-height: 64px;
            }
        
            .bp-meta {
                font-family: 'IBM Plex Mono', monospace;
                font-size: 0.65rem;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                color: #E8A33D;
                border: 1px solid rgba(232,163,61,0.35);
                display: inline-block;
                padding: 0.16rem 0.5rem;
                margin-bottom: 1.3rem;
            }
        
            /* ---------- Buttons ---------- */
            .stButton > button, .stLinkButton > a {
                width: 100%;
                background: transparent !important;
                color: #CFE2F5 !important;
                border: 1px solid #2A4A6B !important;
                border-radius: 0 !important;
                padding: 0.6rem 1rem !important;
                font-family: 'IBM Plex Mono', monospace !important;
                font-size: 0.8rem !important;
                letter-spacing: 0.04em;
                transition: all 0.18s ease;
                justify-content: center !important;
            }
            .stButton > button:hover, .stLinkButton > a:hover {
                border-color: #6FB8FF !important;
                color: #6FB8FF !important;
                background: rgba(111,184,255,0.06) !important;
            }
        
            .bp-footer {
                text-align: center;
                color: #2A4A6B;
                font-family: 'IBM Plex Mono', monospace;
                font-size: 0.68rem;
                letter-spacing: 0.16em;
                text-transform: uppercase;
                margin-top: 3rem;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        
        # ----------------------------------------------------------------------------
        # Hero
        # ----------------------------------------------------------------------------
        
        st.markdown('<div class="bp-tag">Document Studio</div>', unsafe_allow_html=True)
        st.markdown(
            '<h1 class="bp-title">Draft the parts<br/>readers see <span>first</span></h1>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="bp-sub">Three instruments for the front matter of a document — '
            'covers and the index — drawn up before you write a word of the body.</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="bp-divider"><span class="seg"></span>SHEET 01 / 03<span class="seg"></span></div>',
            unsafe_allow_html=True,
        )
        
        # ----------------------------------------------------------------------------
        # Line-art icons (blueprint style — stroke only, no fill)
        # ----------------------------------------------------------------------------
        
        ICON_AI_COVER = """
        <svg width="40" height="40" viewBox="0 0 40 40" fill="none">
        <rect x="7" y="5" width="22" height="30" stroke="#6FB8FF" stroke-width="1.2"/>
        <line x1="11" y1="13" x2="25" y2="13" stroke="#3D6690" stroke-width="1"/>
        <line x1="11" y1="17" x2="21" y2="17" stroke="#3D6690" stroke-width="1"/>
        <path d="M31 7l1.3 2.8L35 11l-2.7 1.2L31 15l-1.3-2.8L27 11l2.7-1.2L31 7z" stroke="#E8A33D" stroke-width="1" stroke-linejoin="round"/>
        </svg>
        """
        
        ICON_INSTANT_COVER = """
        <svg width="40" height="40" viewBox="0 0 40 40" fill="none">
        <rect x="7" y="5" width="22" height="30" stroke="#6FB8FF" stroke-width="1.2"/>
        <line x1="11" y1="13" x2="25" y2="13" stroke="#3D6690" stroke-width="1"/>
        <line x1="11" y1="17" x2="21" y2="17" stroke="#3D6690" stroke-width="1"/>
        <path d="M21 22l-7 8h5l-2 7 9-9h-5l2-6z" fill="#0E1E33" stroke="#E8A33D" stroke-width="1" stroke-linejoin="round"/>
        </svg>
        """
        
        ICON_INDEX = """
        <svg width="40" height="40" viewBox="0 0 40 40" fill="none">
        <rect x="6" y="6" width="28" height="28" stroke="#6FB8FF" stroke-width="1.2"/>
        <line x1="11" y1="13" x2="29" y2="13" stroke="#3D6690" stroke-width="1"/>
        <line x1="11" y1="19" x2="29" y2="19" stroke="#3D6690" stroke-width="1"/>
        <line x1="11" y1="25" x2="23" y2="25" stroke="#3D6690" stroke-width="1"/>
        <line x1="11" y1="31" x2="26" y2="31" stroke="#3D6690" stroke-width="1"/>
        </svg>
        """
        
        # ----------------------------------------------------------------------------
        # Cards
        # ----------------------------------------------------------------------------
        
        cards = [
            {
                "fig": "FIG. 01",
                "rev": "REV A",
                "icon": ICON_AI_COVER,
                "meta": "AI Generated",
                "title": "AI Cover Page",
                "desc": "Describe the document and the model drafts a cover — title block, "
                        "author line, and layout composed from scratch.",
                "cta": "Generate with AI",
                "key": "ai_cover",
                "kind": "button",
            },
            {
                "fig": "FIG. 02",
                "rev": "REV A",
                "icon": ICON_INSTANT_COVER,
                "meta": "Instant",
                "title": "Instant Cover Page",
                "desc": "Fill a short form — title, name, course, date — and get a clean, "
                        "print-ready cover page in seconds.",
                "cta": "Create instantly",
                "key": "instant_cover",
                "kind": "button",
            },
            {
                "fig": "FIG. 03",
                "rev": "REV A",
                "icon": ICON_INDEX,
                "meta": "External Tool",
                "title": "Index Generator",
                "desc": "Opens the dedicated index builder — paste your headings and get a "
                        "numbered, page-referenced index, ready to insert.",
                "cta": "Open index builder ↗",
                "key": "index_gen",
                "kind": "link",
            },
        ]
        
        cols = st.columns(3, gap="medium")
        
        for col, card in zip(cols, cards):
            with col:
                st.markdown(
                    f"""
                    <div class="bp-card">
                        <span class="crop tl"></span><span class="crop tr"></span>
                        <span class="crop bl"></span><span class="crop br"></span>
                        <div class="bp-fig"><span>{card['fig']}</span><span class="rev">{card['rev']}</span></div>
                        <div class="bp-icon">{card['icon']}</div>
                        <div class="bp-meta">{card['meta']}</div>
                        <div class="bp-title-card">{card['title']}</div>
                        <div class="bp-desc">{card['desc']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if card["kind"] == "link":
                    st.link_button(card["cta"], "https://glittering-sprinkles-1d0f9c.netlify.app/", use_container_width=True)
                else:
                    st.button(card["cta"], key=card["key"], use_container_width=True)
        
        st.markdown('<div class="bp-footer">Drafting Desk · Cover &amp; Index Tools</div>', unsafe_allow_html=True)
        
        # ----------------------------------------------------------------------------
        # Wire up actions — replace the bodies below with real generation logic
        # ----------------------------------------------------------------------------
        
        if st.session_state.get("ai_cover"):
            st.error("developer on exams")
        
        if st.session_state.get("instant_cover"):
            st.link_button(card["cta"], "https://cover-page.streamlit.app/", use_container_width=True)