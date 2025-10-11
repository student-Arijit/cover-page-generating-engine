import streamlit as st
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import base64

def Index(arr):
    packet = BytesIO()
    doc = SimpleDocTemplate(packet, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=10, bottomMargin=30)  
    styles = getSampleStyleSheet()
    elements = []

    # Heading
    elements.append(Paragraph("INDEX", styles['Title']))
    elements.append(Spacer(1, 10))

    # Table data
    data = [["SI No.", "Assignment Name", "Code Date", "Approval Date", "Pg. No.", "Signature"]]
    data.extend(arr)
    centered_style = ParagraphStyle(name="centered", parent=styles['Normal'], alignment=TA_CENTER)
    right_align = ParagraphStyle(
        name= "RightAlign",
        parent= styles["Normal"],
        alignment= 2,
        fontSize= 12
    )

    # Wrap each cell in Paragraph for automatic text wrapping
    wrapped_data = []
    for row in data:
        wrapped_row = [Paragraph(str(cell), centered_style) for cell in row]
        wrapped_data.append(wrapped_row)

    table = Table(wrapped_data, colWidths=[50, 150, 100, 100, 70, 70], repeatRows=1)
    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    elements.append(table)
    elements.append(Spacer(1, 35))

    elements.append(Paragraph("-------------------------------------------", right_align))
    elements.append(Spacer(1, 5))
    elements.append(Paragraph("[Signature of H.O.D]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", right_align))


    doc.build(elements)

    packet.seek(0)

    st.download_button(label="download pdf", data=packet, file_name="index.pdf", mime="application/pdf")