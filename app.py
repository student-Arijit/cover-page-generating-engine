import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
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

background_pdf_path = "testdoc.pdf"  # Your PDF background

if st.button("Generate PDF"):
    # Step 1: Create a new PDF with ReportLab (text overlay)
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    width, height = A4

    # Add text at custom positions
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 100, f"Name: {sem}")
    c.drawString(100, height - 140, f"Score: {stream}")
    c.save()

    packet.seek(0)

    # Step 2: Read both background and overlay PDFs
    background = PdfReader(background_pdf_path)
    overlay = PdfReader(packet)

    output = PdfWriter()

    # Merge overlay (text) onto background
    background_page = background.pages[0]
    background_page.merge_page(overlay.pages[0])
    output.add_page(background_page)

    # Step 3: Write final PDF to memory
    final_buffer = BytesIO()
    output.write(final_buffer)
    final_buffer.seek(0)

    # Step 4: Encode to Base64 for opening in browser
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