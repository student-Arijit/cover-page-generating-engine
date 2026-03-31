import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from io import BytesIO
import base64
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import time

class Template:
    def __init__(self):
        pdfmetrics.registerFont(TTFont('raleway', 'assets/Fonts/raleway.ttf'))
        pdfmetrics.registerFont(TTFont('BAHNSCHRIFT', 'assets/Fonts/BAHNSCHRIFT.ttf'))
        pdfmetrics.registerFont(TTFont('nunitosans', 'assets/Fonts/nunitosans.ttf'))
        pdfmetrics.registerFont(TTFont('trebuc', 'assets/Fonts/trebuc.ttf'))

    def template1(self, stream, sem, univ, roll, reg, paper_name, paper_code, sub):
        with st.spinner("Wait for it..."):
            packet = BytesIO()
            c = canvas.Canvas(packet, pagesize=A4)
            width, height = A4

            darkblue = colors.Color(18/255, 14/255, 94/255)
            c.setFillColor(darkblue)

        # Stream
            c.setFont("nunitosans", 25)
            c.drawString(50, height - 185, stream)

        # Semester
            c.drawString(60, height - 230, f"Semester - {sem}")

        # Roll, reg, paper name, univ name section
            if univ == "University of Calcutta":
            # Univ name
                c.setFont("raleway", 30)
                c.drawString(370, height - 230, "UNIVERSITY")
                c.drawString(430, height - 260, "OF")
                c.drawString(380, height - 290, "CALCUTTA")

            # Roll
                c.setFont("BAHNSCHRIFT", 20)
                c.drawString(30, height - 320, "C.U. ROLL NO: - ")
                c.setFillColor(colors.black)
                c.drawString(170, height - 320, roll)

            # Reg
                c.setFillColor(darkblue)
                c.drawString(30, height - 370, "C.U. REG. NO: - ")
                c.setFillColor(colors.black)
                c.drawString(170, height - 370, reg)

        # Paper name
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
            c.drawImage(
                "assets/images/University_of_Calcutta_logo.png",
                380, height - 170,
                width=150, height=140,
                mask="auto"
            )
            c.save()

            packet.seek(0)
            overlay = PdfReader(packet)
            output = PdfWriter()

            base_pdf = PdfReader(open("assets/backgrounds/background1.pdf", "rb"))
            page = base_pdf.pages[0]
            page.merge_page(overlay.pages[0])
            output.add_page(page)

            final_buffer = BytesIO()
            output.write(final_buffer)
            final_buffer.seek(0)

        st.download_button(
            label="📄 Download PDF",
            data=final_buffer,
            file_name=f"{roll}.pdf",
            mime="application/pdf"
        )