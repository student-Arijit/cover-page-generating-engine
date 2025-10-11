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
    background_pdf_path = "assets/backgrounds/background3.pdf"
    pdfmetrics.registerFont(TTFont('BAHNSCHRIFT', 'assets/Fonts/BAHNSCHRIFT.ttf'))
    pdfmetrics.registerFont(TTFont('calibri', 'assets/Fonts/calibri.ttf'))
    pdfmetrics.registerFont(TTFont('nunitosans', 'assets/Fonts/nunitosans.ttf'))
    pdfmetrics.registerFont(TTFont('raleway', 'assets/Fonts/raleway.ttf'))
    darkblue = colors.Color(9/255, 31/255, 110/255)
    deepblue = colors.Color(17/255, 33/255, 89/255)

    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    width, height = A4  

    c.drawImage("assets/images/University_of_Calcutta_logo.png", 226, 698, width=140, height=130, mask="auto")
    
    
    c.setFont("raleway", 32)
    c.setFillColor(colors.white)
    c.drawString(70, 650, "UNIVERSITY")
    c.drawString(280, 650, "OF")
    c.drawString(340, 650, "CALCUTTA")

    c.setFillColor(colors.white)
    c.setFont("calibri", 22)
    c.drawString(100, 510, "SUBJECT :- ")
    c.setFillColor(darkblue)
    c.drawString(205, 510, sub)
    c.setFillColor(colors.white)
    c.drawString(100, 480, "PAPER CODE :- ")
    c.setFillColor(darkblue)
    c.drawString(240, 480, paper_code)

    #roll, reg & paper name
    c.setFillColor(colors.white)
    c.setFont("BAHNSCHRIFT", 18)
    c.drawString(100, 430, "C.U. ROLL NO :- ")
    c.setFillColor(colors.black)
    c.drawString(230, 430, roll)
    c.setFillColor(colors.white)
    c.drawString(100, 376, "C.U. REG NO: - ")
    c.setFillColor(colors.black)
    c.drawString(230, 376, reg)
    c.setFillColor(colors.white)
    c.drawString(100, 320, "PAPER NAME :- ")
    c.setFillColor(colors.black)

    
    if len(paper_name) > 15:
        words = paper_name.split()
        c.drawString(430, 320, words[0])
        words.pop(0)
        new = " ".join(words)
        c.drawString(300, 300, new)
    else:
        c.drawString(430, 320, paper_name)

    c.setFillColor(colors.darkblue)
    c.setFont("BAHNSCHRIFT", 20)
    c.drawString(100,570, stream)
    c.setFillColor(colors.white)
    c.drawString(100,540, f"SEMESTER :- {sem}")

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