import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from io import BytesIO
import base64
import os

st.title("Cover page generating Engine")
univ=st.selectbox("Enter your University/college: ", ("University of Calcutta"))
stream=st.selectbox("Enter Your Stream: ", ("B.Sc", "B.com", "B.A"), index=0)
sem=st.selectbox("Enter your semester: ", ("I", "II", "III", "IV", "V", "VI", "VII", "VIII"), index=3)
roll=st.text_input("Enter Your Roll No.: ")
reg=st.text_input("Enter Your Reg No.: ")
paper_name=st.text_input("Enter Your Paper name: ")
sub=st.text_input("Enter Your Subject: ")
paper_code=st.text_input("Enter Your Paper Code: ")

background_image_path = "bg.png"

if st.button("Generate PDF"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Draw background image covering full page
    c.drawImage(background_image_path, 0, 0, width=width, height=height)

    # Add text at custom positions
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 100, f"Name: {sem}")
    c.drawString(100, height - 140, f"Score: {stream}")

    c.showPage()
    c.save()

    buffer.seek(0)

    b64_pdf = base64.b64encode(buffer.read()).decode("utf-8")

    # Create a JavaScript snippet to open PDF in a new tab
    pdf_url = f'data:application/pdf;base64,{b64_pdf}'
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