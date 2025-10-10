import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from io import BytesIO
import base64
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def cover_page(stream, sem, univ, roll, reg, paper_name, paper_code, sub):
    background_pdf_path = "assets/backgrounds/background2.pdf"

    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    width, height = A4  


    #==============
    c.drawImage("assets/images/University_of_Calcutta_logo.png",140,698,width=140,height=130,mask="auto")
    c.drawString(177,670,f"UNIVERSITY")
    c.drawString(205,655,f"OF")
    c.drawString(177,639,f"CALCUTTA")

    c.setFillColor(colors.darkblue)
    c.drawString(385,600,f"SUBJECT :- ")
    c.drawString(385,570,f"PAPER CODE :- ")

    c.setFillColor(colors.red)
    c.drawString(300,440,f"C.U. ROLL NO :- ")
    c.drawString(300,376,f"C.U. REG NO: - ")
    c.drawString(300,310,f"PAPER NAME :- ")

    c.setFillColor(colors.yellow)
    c.drawString(75,238,f"B.Sc. Honours")
    c.drawString(75,190,f"SEMESTER 4")


    #==============


    c.save()
    packet.seek(0)
    background = PdfReader(background_pdf_path)
    overlay = PdfReader(packet)

    output = PdfWriter()
    background_page = background.pages[0]
    background_page.merge_page(overlay.pages[0])
    output.add_page(background_page)

    # Step 3: Write final PDF to memory
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