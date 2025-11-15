import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import base64

def Invitation_card(name):
    background_pdf_path = "assets/backgrounds/Farewellprogram.pdf"
    packet = BytesIO()

    c = canvas.Canvas(packet, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 50)
    c.setFillColor(colors.white)
    c.drawString(180, 320, f"{name}")

    c.save()
    packet.seek(0)

    background = PdfReader(background_pdf_path)
    overlay = PdfReader(packet)

    output = PdfWriter()
    background_page = background.pages[0]
    background_page.merge_page(overlay.pages[0])
    output.add_page(background_page)

    final_buffer = BytesIO()
    output.write(final_buffer)
    final_buffer.seek(0)

    st.download_button(
        label = "📄 Download PDF",
        data=final_buffer,
        file_name=f"Invitation_Card_{name}.pdf",
        mime="application/pdf"
    )