import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def Invitation_card(name):
    background_pdf_path = "assets/backgrounds/Farewellprogram.pdf"

    # Load background page
    bg_reader = PdfReader(background_pdf_path)
    bg_page = bg_reader.pages[0]

    width = float(bg_page.mediabox.width)
    height = float(bg_page.mediabox.height)

    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    c.setFont("Helvetica-Bold", 55)
    c.setFillColor(colors.white)

    x = 470  
    y = 320  

    c.drawString(x, y, name)

    c.save()
    packet.seek(0)

    # Merge overlay with background
    overlay_reader = PdfReader(packet)
    overlay_page = overlay_reader.pages[0]
    bg_page.merge_page(overlay_page)

    output = PdfWriter()
    output.add_page(bg_page)

    final_buffer = BytesIO()
    output.write(final_buffer)
    final_buffer.seek(0)

    st.download_button(
        label="📄 Download Invitation Card",
        data=final_buffer,
        file_name=f"Invitation_Card_{name}.pdf",
        mime="application/pdf"
    )
