import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfWriter, PdfReader
from io import BytesIO
import base64

def cover_page(stream, sem, univ, roll, reg, paper_name, paper_code, sub):
    background_path = "assets/backgrounds/background5.pdf"

    packet = BytesIO()
    c = canvas.Canvas(packet, A4)
    width, height = A4

    #=========================
    c.drawString(100, height - 100, "Hello World")
    #=========================

    c.save()
    packet.seek(0)

    background = PdfReader(background_path)
    overlay = PdfReader(packet)

    output = PdfWriter()
    background_page = background.pages[0]
    background_page.merge_page(overlay.pages[0])
    output.add_page(background_page)

    final_buffer = BytesIO()
    output.write(final_buffer)
    final_buffer.seek(0)

    b64_pdf = base64.b64encode(final_buffer.read()).decode("utf-8")
    pdf_url = f"data:application/pdf;base64,{b64_pdf}"

    # Open in new tab
    script = f"""
        <script>
            const blob = atob("{b64_pdf}");
            const array = new Uint8Array(blob.length);
            for (let i = 0; i < blob.length; i++) {{
                array[i] = blob.charCodeAt(i);
            }}
            const pdfBlob = new Blob([array], {{ type: "application/pdf" }});
            const pdfURL = URL.createObjectURL(pdfBlob);
            window.open(pdfURL);
        </script>
    """

    st.components.v1.html(script, height=0)