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
    background_pdf_path = "assets/backgrounds/background7.pdf"
    pdfmetrics.registerFont(TTFont('BAHNSCHRIFT', 'assets/Fonts/BAHNSCHRIFT.ttf'))
    pdfmetrics.registerFont(TTFont('calibri', 'assets/Fonts/calibri.ttf'))
    pdfmetrics.registerFont(TTFont('nunitosans', 'assets/Fonts/nunitosans.ttf'))
    pdfmetrics.registerFont(TTFont('raleway', 'assets/Fonts/raleway.ttf'))
    darkblue = colors.Color(9/255, 31/255, 110/255)
    deepblue = colors.Color(17/255, 33/255, 89/255)

    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    width, height = A4  

    c.drawImage("assets/images/University_of_Calcutta_logo.png", 230, 635, width=130, height=130, mask="auto")
    
    c.setFont("raleway", 25)
    c.setFillColor(colors.black)
    c.drawString(130, 609, "UNIVERSITY OF CALCUTTA")

    #roll, reg & paper name
    c.setFont("BAHNSCHRIFT", 20)
    c.drawString(125, 430, "SUBJECT :- ")
    c.drawString(230, 430, sub)
    c.drawString(125, 370, "PAPER CODE :- ")
    c.drawString(263, 370, paper_code)
    c.drawString(125, 310, "C.U. ROLL NO :- ")
    c.drawString(265, 310, roll)
    c.drawString(125, 250, "C.U. REG NO: - ")
    c.drawString(265, 250, reg)
    c.setFont("calibri", 23)
    c.drawString(120, 150, "Paper :- ")
    c.drawString(204, 150, paper_name)

    c.setFont("BAHNSCHRIFT", 20)
    c.drawString(235, 569, stream)
    c.drawString(237, 529, f"SEMESTER {sem}")

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

    st.download_button(
        label = "📄 Download PDF",
        data = final_buffer,
        file_name = f"{roll}.pdf",
        mime = "application/pdf"
    )