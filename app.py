import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from io import BytesIO

st.title("Cover page generating Engine")
stream=st.selectbox("Enter Your Stream: ", ("B.Sc", "B.com", "B.A"), index=0)
sem=st.selectbox("Enter your semester: ", ("I", "II", "III", "IV", "V", "VI", "VII", "VIII"), index=3)
roll=st.text_input("Enter Your Roll No.: ")
reg=st.text_input("Enter Your Reg No.: ")
paper_name=st.text_input("Enter Your Paper name: ")
sub=st.text_input("Enter Your Subject: ")
paper_code=st.text_input("Enter Your Paper Code: ")

background_image_path = "bg.png"  # Ensure this image is in your working folder

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

    st.download_button(
        label="📥 Download PDF",
        data=buffer,
        file_name="custom_report.pdf",
        mime="application/pdf"
    )