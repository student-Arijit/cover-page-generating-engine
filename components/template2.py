import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

def cover_page(stream, sem, univ, roll, reg, paper_name, paper_code, sub):
    p = st.progress(0)

    bg_path = "assets/background2.pdf"
    p.progress(1)

    packet = BytesIO()
    p.progress(2)

    c = canvas.Canvas(packet, A4)
    p.progress(3)

    width, height = A4
    p.progress(4)

    c.drawString(100, 100, "hello world")
