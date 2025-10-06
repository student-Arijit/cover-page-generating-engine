import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from io import BytesIO
import base64
import os
from PyPDF2 import PdfReader, PdfWriter

st.title("Cover page generating Engine")
univ=st.selectbox("Enter your University/college: ", ("University of Calcutta"))
stream=st.selectbox("Enter Your Stream: ", ("B.Sc", "B.com", "B.A"), index=0)
sem=st.selectbox("Enter your semester: ", ("I", "II", "III", "IV", "V", "VI", "VII", "VIII"), index=3)
roll=st.text_input("Enter Your Roll No.: ")
reg=st.text_input("Enter Your Reg No.: ")
paper_name=st.text_input("Enter Your Paper name: ")
sub=st.text_input("Enter Your Subject: ")
paper_code=st.text_input("Enter Your Paper Code: ")

background_pdf_path = "assets/background1.pdf"  #PDF background

if st.button("Generate PDF"):
    p = st.progress(0)
    # Step 1: Create a new PDF with ReportLab (text overlay)
    packet = BytesIO()
    p.progress(1)
    c = canvas.Canvas(packet, pagesize=A4)
    width, height = A4
    p.progress(3)
    # Add text at custom positions
    c.setFont("Helvetica-Bold", 16)
    p.progress(4)
    darkblue = colors.Color(17/255, 17/255, 132/255)
    c.setFillColor(darkblue)
    c.drawString(400, height - 230, f"{univ}")
    c.drawString(100, height - 100, f"Name: {sem}")
    c.drawString(100, height - 140, f"Score: {stream}")
    c.drawString(50, 190, f"SUBJECT: {sub}")
    c.drawString(30, 147, f"PAPER CODE: {paper_code}")
    c.drawImage("assets/University_of_Calcutta_logo.png", 450, height - 125, width=100, height=90, mask="auto")
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
        label="📄 Download PDF",
        data=final_buffer,
        file_name="result.pdf",
        mime="application/pdf"
    )