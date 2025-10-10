import streamlit as st
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table ,TableStyle
from reportlab.lib import colors
import base64

def Index():
    packet = BytesIO()

    c = canvas.Canvas(packet, pagesize = A4)
    width, height = A4

    c.setFontSize(30)
    c.drawString(250, height - 50, "INDEX")
    data = [
        ["SI No.", "Assignment Name", "Code Date", "Approval Date", "Pg. No.", "Signature"]
    ]

    table = Table(data, colWidths=[50, 150, 100, 100, 70, 70])
    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    table.wrapOn(c, width, height)
    table.drawOn(c, 30, height - 100)

    c.save()
    packet.seek(0)
    
    b64_pdf = base64.b64encode(packet.read()).decode("utf-8")
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