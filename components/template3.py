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
    # Background and fonts
    background_pdf_path = "assets/backgrounds/background3.pdf"
    pdfmetrics.registerFont(TTFont('BAHNSCHRIFT', 'assets/Fonts/BAHNSCHRIFT.ttf'))
    pdfmetrics.registerFont(TTFont('calibri', 'assets/Fonts/calibri.ttf'))
    pdfmetrics.registerFont(TTFont('nunitosans', 'assets/Fonts/nunitosans.ttf'))
    pdfmetrics.registerFont(TTFont('raleway', 'assets/Fonts/raleway.ttf'))
    
    # Colors
    darkblue = colors.Color(9/255, 31/255, 110/255)
    deepblue = colors.Color(17/255, 33/255, 89/255)

    # Canvas setup
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    width, height = A4  

    # University logo
    c.drawImage("assets/images/University_of_Calcutta_logo.png", 228, 694, width=145, height=132, mask="auto")

    # Header text
    c.setFont("raleway", 32)
    c.setFillColor(colors.white)
    c.drawString(70, 650, "UNIVERSITY")
    c.drawString(280, 650, "OF")
    c.drawString(340, 650, "CALCUTTA")

    # Subject and Paper Code
    c.setFillColor(colors.white)
    c.setFont("calibri", 22)
    c.drawString(100, 510, "SUBJECT :- ")
    c.setFillColor(darkblue)
    c.drawString(205, 510, sub)

    c.setFillColor(colors.white)
    c.drawString(100, 470, "PAPER CODE :- ")
    c.setFillColor(darkblue)
    c.drawString(240, 470, paper_code)

    # Roll, Reg
    c.setFillColor(colors.white)
    c.setFont("BAHNSCHRIFT", 18)
    c.drawString(100, 430, "C.U. ROLL NO :- ")
    c.setFillColor(colors.darkblue)
    c.drawString(229, 430, roll)

    c.setFillColor(colors.white)
    c.drawString(100, 376, "C.U. REG NO: - ")
    c.setFillColor(colors.darkblue)
    c.drawString(229, 376, reg)

    # PAPER NAME section (improved alignment + wrapping)
    c.setFillColor(colors.white)
    c.drawString(100, 320, "PAPER NAME :- ")
    c.setFillColor(colors.darkblue)
    text_x = 229  # aligned neatly under label
    text_y = 320

    if len(paper_name) > 25:
        # Wrap long paper names
        c.setFont("BAHNSCHRIFT", 16)
        wrapped = c.beginText(text_x, text_y)
        wrapped.setLeading(20)
        words = paper_name.split()
        line = ""
        for word in words:
            if c.stringWidth(line + word, "BAHNSCHRIFT", 16) < 300:
                line += word + " "
            else:
                wrapped.textLine(line.strip())
                line = word + " "
        if line:
            wrapped.textLine(line.strip())
        c.drawText(wrapped)
    else:
        c.setFont("BAHNSCHRIFT", 18)
        c.drawString(text_x, text_y, paper_name)

    # Stream & Semester
    c.setFillColor(colors.darkblue)
    c.setFont("BAHNSCHRIFT", 20)
    c.drawString(100, 570, stream)
    c.setFillColor(colors.white)
    c.drawString(100, 540, f"SEMESTER :- {sem}")

    # Finalize overlay
    c.save()
    packet.seek(0)

    # Merge background and overlay
    background = PdfReader(background_pdf_path)
    overlay = PdfReader(packet)
    output = PdfWriter()
    background_page = background.pages[0]
    background_page.merge_page(overlay.pages[0])
    output.add_page(background_page)

    # Output final PDF
    final_buffer = BytesIO()
    output.write(final_buffer)
    final_buffer.seek(0)

    b64_pdf = base64.b64encode(final_buffer.read()).decode("utf-8")
    pdf_url = f"data:application/pdf;base64,{b64_pdf}"

    # Open in new browser tab
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
