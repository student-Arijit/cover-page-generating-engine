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
    background_pdf_path = "assets/background1.pdf"  #PDF background
    pdfmetrics.registerFont(TTFont('raleway', 'assets/Fonts/raleway.ttf'))
    pdfmetrics.registerFont(TTFont('BAHNSCHRIFT', 'assets/Fonts/BAHNSCHRIFT.ttf'))
    pdfmetrics.registerFont(TTFont('nunitosans', 'assets/Fonts/nunitosans.ttf'))
    pdfmetrics.registerFont(TTFont('trebuc', 'assets/Fonts/trebuc.ttf'))

    p = st.progress(0)
    # Step 1: Create a new PDF with ReportLab (text overlay)
    packet = BytesIO()
    p.progress(1)
    c = canvas.Canvas(packet, pagesize=A4)
    width, height = A4
    p.progress(3)
    # Add text at custom positions
    p.progress(4)
    darkblue = colors.Color(18/255, 14/255, 94/255)
    c.setFillColor(darkblue)

    #Stream
    c.setFont("nunitosans", 25) 
    c.drawString(50, height - 185, stream)

    #Semester
    c.drawString(60, height - 230, f"Semester - {sem}")

    #roll, reg, paper name, UNIV NAME section
    if univ == "University of Calcutta":
        #univ name
        c.setFont("raleway", 30)
        c.drawString(370, height - 230, "UNIVERSITY") 
        c.drawString(430, height - 260, "OF")
        c.drawString(380, height - 290, "CALCUTTA")

        #roll
        c.setFont("BAHNSCHRIFT", 20)
        c.drawString(30, height - 320, "C.U. ROLL NO: - ")
        c.setFillColor(colors.black)
        c.drawString(170, height - 320, roll)

        #reg
        c.setFillColor(darkblue)
        c.drawString(30, height - 370, "C.U. REG. NO: - ")
        c.setFillColor(colors.black)
        c.drawString(170, height - 370, reg)

    #paper name
    c.setFillColor(darkblue)
    c.drawString(30, height - 420, "PAPER NAME: - ")
    c.setFillColor(colors.black)
    if len(paper_name) > 15:
        words = paper_name.split()
        c.drawString(170, height - 420, words[0])
        words.pop(0)
        words = " ".join(words)
        c.drawString(30, height - 440, words)

    else:
        c.drawString(170, height - 420, paper_name)
    c.setFillColor(darkblue)

    c.setFont("trebuc", 20)
    c.drawString(50, 190, f"SUBJECT: {sub}")
    c.drawString(30, 147, f"PAPER CODE: {paper_code}")
    c.drawImage("assets/University_of_Calcutta_logo.png", 380, height - 170, width=150, height=140, mask="auto")
    c.save()
    p.progress(50)
    packet.seek(0)

    # Step 2: Read both background and overlay PDFs
    background = PdfReader(background_pdf_path)
    overlay = PdfReader(packet)

    output = PdfWriter()
    p.progress(70)
    # Merge overlay (text) onto background
    background_page = background.pages[0]
    background_page.merge_page(overlay.pages[0])
    output.add_page(background_page)

    # Step 3: Write final PDF to memory
    final_buffer = BytesIO()
    output.write(final_buffer)
    final_buffer.seek(0)
    p.progress(100)

    st.download_button(
        label = "📄 Download PDF",
        data = final_buffer,
        file_name = f"{roll}.pdf",
        mime = "application/pdf"
    )