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
        pdfmetrics.registerFont(TTFont('calibri', 'assets/Fonts/calibri.ttf'))
        pdfmetrics.registerFont(TTFont('trebuc', 'assets/Fonts/trebuc.ttf'))

        self.darkblue = colors.Color(9/255, 31/255, 110/255)
        self.deepblue = colors.Color(17/255, 33/255, 89/255)

    def template1(self, stream, sem, univ, roll, reg, paper_name, paper_code, sub):
        with st.spinner("Wait for it..."):
            packet = BytesIO()
            c = canvas.Canvas(packet, pagesize=A4)
            width, height = A4

            c.setFillColor(self.darkblue)

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
                c.setFillColor(self.darkblue)
                c.drawString(30, height - 370, "C.U. REG. NO: - ")
                c.setFillColor(colors.black)
                c.drawString(170, height - 370, reg)

        # Paper name
            c.setFillColor(self.darkblue)
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

            c.setFillColor(self.darkblue)
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

    def template2(self, stream, sem, univ, roll, reg, paper_name, paper_code, sub):
        with st.spinner("wait for it..."):
            packet = BytesIO()
            c = canvas.Canvas(packet, pagesize=A4)
            width, height = A4  

            c.drawImage("assets/images/University_of_Calcutta_logo.png", 160, 690, width=140, height=130, mask="auto")
    
            c.setFont("raleway", 32)
            c.setFillColor(self.deepblue)
            c.drawString(147, 650, "UNIVERSITY")
            c.drawString(210, 615, "OF")
            c.drawString(152, 580, "CALCUTTA")

            c.setFillColor(self.darkblue)
            c.setFont("calibri", 22)
            c.drawString(345, 540, "SUBJECT :- ")
            c.drawString(445, 540, sub)
            c.drawString(345, 510, "PAPER CODE :- ")
            c.drawString(480, 510, paper_code)

    #roll, reg & paper name
            c.setFillColor(colors.red)
            c.setFont("BAHNSCHRIFT", 18)
            c.drawString(300, 430, "C.U. ROLL NO :- ")
            c.setFillColor(colors.black)
            c.drawString(430, 430, roll)
            c.setFillColor(colors.red)
            c.drawString(300, 376, "C.U. REG NO: - ")
            c.setFillColor(colors.black)
            c.drawString(420, 376, reg)
            c.setFillColor(colors.red)
            c.drawString(300, 320, "PAPER NAME :- ")
            c.setFillColor(colors.black)
            if len(paper_name) > 15:
                words = paper_name.split()
                c.drawString(430, 320, words[0])
                words.pop(0)
                new = " ".join(words)
                c.drawString(300, 300, new)
            else:
                c.drawString(430, 320, paper_name)

            c.setFillColor(colors.yellow)
            c.setFont("BAHNSCHRIFT", 20)
            c.drawString(45,241, stream)
            c.drawString(75,187, f"SEMESTER   {sem}")

            c.save()
            packet.seek(0)
            background = PdfReader("assets/backgrounds/background2.pdf")
            overlay = PdfReader(packet)

            output = PdfWriter()
            background_page = background.pages[0]
            background_page.merge_page(overlay.pages[0])
            output.add_page(background_page)

    # Step 3: Write final PDF to memory
            final_buffer = BytesIO()
            output.write(final_buffer)
            final_buffer.seek(0)
        
        st.download_button(
            label="📄 Download PDF",
            data=final_buffer,
            file_name=f"{roll}.pdf",
            mime="application/pdf"
        )
    
    def template3(self, stream, sem, univ, roll, reg, paper_name, paper_code, sub):
        with st.spinner("wait for it..."):
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
            c.setFillColor(self.darkblue)
            c.drawString(205, 510, sub)

            c.setFillColor(colors.white)
            c.drawString(100, 470, "PAPER CODE :- ")
            c.setFillColor(self.darkblue)
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
            background = PdfReader("assets/backgrounds/background3.pdf")
            overlay = PdfReader(packet)
            output = PdfWriter()
            background_page = background.pages[0]
            background_page.merge_page(overlay.pages[0])
            output.add_page(background_page)

    # Output final PDF
            final_buffer = BytesIO()
            output.write(final_buffer)
            final_buffer.seek(0)
        
        st.download_button(
            label="📄 Download PDF",
            data=final_buffer,
            file_name=f"{roll}.pdf",
            mime="application/pdf"
        )

    def template4(self, stream, sem, univ, roll, reg, paper_name, paper_code, sub):
        with st.spinner("wait for it..."):
            packet = BytesIO()
            c = canvas.Canvas(packet, pagesize=A4)
            width, height = A4  

    # University logo
            c.drawImage("assets/images/University_of_Calcutta_logo.png", 223, 676, width=149, height=140, mask="auto")

    # Header text
            c.setFont("raleway", 32)
            c.setFillColor(colors.white)
            c.drawString(97, 630, "UNIVERSITY")
            c.drawString(298, 630, "OF")
            c.drawString(353, 630, "CALCUTTA")

    # Subject and Paper Code
            c.setFillColor(colors.white)
            c.setFont("calibri", 22)
            c.drawString(100, 390, "SUBJECT :- ")
            c.setFillColor(colors.aqua)
            c.drawString(205, 390, sub)

            c.setFillColor(colors.white)
            c.drawString(100, 440, "PAPER CODE :- ")
            c.setFillColor(colors.aqua)
            c.drawString(240, 440, paper_code)

        # Roll, Reg
            c.setFillColor(colors.white)
            c.setFont("BAHNSCHRIFT", 18)
            c.drawString(100, 300, "C.U. ROLL NO :- ")
            c.setFillColor(colors.aqua)
            c.drawString(229, 300, roll)

            c.setFillColor(colors.white)
            c.drawString(100, 260, "C.U. REG NO: - ")
            c.setFillColor(colors.aqua)
            c.drawString(220, 260, reg)

    # PAPER NAME section (improved alignment + wrapping)
            c.setFillColor(colors.white)
            c.drawString(65, 63, "PAPER NAME :- ")
    
            text_x = 194  # aligned neatly under label
            text_y = 63
            c.setFillColor(colors.white)
            c.drawString(100,520,"====================")

            c.setFillColor(colors.aqua)
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
            c.setFillColor(colors.aqua)
            c.setFont("BAHNSCHRIFT", 23)
            c.drawString(100, 577, stream)
            c.setFillColor(colors.aqua)
            c.drawString(100, 540, f"SEMESTER :- {sem}")

    # Finalize overlay
            c.save()
            packet.seek(0)

    # Merge background and overlay
            background = PdfReader("assets/backgrounds/background4.pdf")
            overlay = PdfReader(packet)
            output = PdfWriter()
            background_page = background.pages[0]
            background_page.merge_page(overlay.pages[0])
            output.add_page(background_page)

    # Output final PDF
            final_buffer = BytesIO()
            output.write(final_buffer)
            final_buffer.seek(0)
        
        st.download_button(
            label="📄 Download PDF",
            data=final_buffer,
            file_name=f"{roll}.pdf",
            mime="application/pdf"
        )

    def template5(self, stream, sem, univ, roll, reg, paper_name, paper_code, sub):
        with st.spinner("wait for it..."):
            packet = BytesIO()
            c = canvas.Canvas(packet, pagesize=A4)
            width, height = A4  

            # University logo
            c.drawImage("assets/images/University_of_Calcutta_logo.png", 220, 633, width=155, height=154, mask="auto")

            # Header text
            c.setFont("raleway", 32)
            c.setFillColor(colors.darkblue)
            c.drawString(97, 597, "UNIVERSITY")
            c.drawString(298, 597, "OF")
            c.drawString(353, 597, "CALCUTTA")

            # Subject and Paper Code
            c.setFillColor(colors.darkblue)
            c.setFont("calibri", 22)
            c.drawString(100, 390, "SUBJECT :- ")
            c.setFillColor(colors.gold)
            c.drawString(205, 390, sub)

            c.setFillColor(colors.darkblue)
            c.drawString(100, 440, "PAPER CODE :- ")
            c.setFillColor(colors.gold)
            c.drawString(240, 440, paper_code)

            # Roll, Reg
            c.setFillColor(colors.darkblue)
            c.setFont("BAHNSCHRIFT", 18)
            c.drawString(100, 300, "C.U. ROLL NO :- ")
            c.setFillColor(colors.gold)
            c.drawString(229, 300, roll)

            c.setFillColor(colors.darkblue)
            c.drawString(100, 260, "C.U. REG NO: - ")
            c.setFillColor(colors.gold)
            c.drawString(220, 260, reg)

            # PAPER NAME section (improved alignment + wrapping)
            c.setFillColor(colors.darkblue)
            c.drawString(65, 63, "PAPER NAME :- ")
            text_x = 194  # aligned neatly under label
            text_y = 63
            c.setFillColor(colors.gold)

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
            c.setFont("BAHNSCHRIFT", 23)
            c.drawString(100, 577, stream)
            c.setFillColor(colors.gold)
            c.drawString(218, 525, f"SEMESTER :- {sem}")

            # Finalize overlay
            c.save()
            packet.seek(0)

            # Merge background and overlay
            background = PdfReader("assets/backgrounds/background5.pdf")
            overlay = PdfReader(packet)
            output = PdfWriter()
            background_page = background.pages[0]
            background_page.merge_page(overlay.pages[0])
            output.add_page(background_page)

            # Output final PDF
            final_buffer = BytesIO()
            output.write(final_buffer)
            final_buffer.seek(0)
        
        st.download_button(
            label="📄 Download PDF",
            data=final_buffer,
            file_name=f"{roll}.pdf",
            mime="application/pdf"
        )

    def template6(self, stream, sem, univ, roll, reg, paper_name, paper_code, sub):
        with st.spinner("wait for it..."):
            packet = BytesIO()
            c = canvas.Canvas(packet, pagesize=A4)
            width, height = A4  

            c.drawImage("assets/images/University_of_Calcutta_logo.png", 230, 650, width=130, height=130, mask="auto")
            
            c.setFont("raleway", 25)
            c.setFillColor(colors.black)
            c.drawString(130, 621, "UNIVERSITY OF CALCUTTA")

            #roll, reg & paper name
            c.setFont("BAHNSCHRIFT", 20)
            c.drawString(125, 430, "SUBJECT :- ")
            c.drawString(230, 430, sub)
            c.drawString(125, 370, "PAPER CODE :- ")
            c.drawString(263, 370, paper_code)
            c.drawString(125, 310, "C.U. ROLL NO :- ")
            c.drawString(265, 310, roll)
            c.drawString(125, 250, "C.U. REG NO: - ")
            c.drawString(265, 250, reg)
            c.setFont("calibri", 23)
            c.drawString(120, 150, "Paper :- ")
            c.drawString(204, 150, paper_name)

            c.setFont("BAHNSCHRIFT", 20)
            c.drawString(235, 580, stream)
            c.drawString(237, 540, f"SEMESTER {sem}")

            c.save()
            packet.seek(0)
            background = PdfReader("assets/backgrounds/background6.pdf")
            overlay = PdfReader(packet)

            output = PdfWriter()
            background_page = background.pages[0]
            background_page.merge_page(overlay.pages[0])
            output.add_page(background_page)

            # Step 3: Write final PDF to memory
            final_buffer = BytesIO()
            output.write(final_buffer)
            final_buffer.seek(0)
        
        st.download_button(
            label="📄 Download PDF",
            data=final_buffer,
            file_name=f"{roll}.pdf",
            mime="application/pdf"
        )

    def template7(self, stream, sem, univ, roll, reg, paper_name, paper_code, sub):
        with st.spinner("wait for it..."):
            packet = BytesIO()
            c = canvas.Canvas(packet, pagesize=A4)
            width, height = A4  

            c.drawImage("assets/images/University_of_Calcutta_logo.png", 230, 635, width=130, height=130, mask="auto")
            
            c.setFont("raleway", 25)
            c.setFillColor(colors.black)
            c.drawString(130, 609, "UNIVERSITY OF CALCUTTA")

            #roll, reg & paper name
            c.setFont("BAHNSCHRIFT", 20)
            c.drawString(125, 430, "SUBJECT :- ")
            c.drawString(230, 430, sub)
            c.drawString(125, 370, "PAPER CODE :- ")
            c.drawString(263, 370, paper_code)
            c.drawString(125, 310, "C.U. ROLL NO :- ")
            c.drawString(265, 310, roll)
            c.drawString(125, 250, "C.U. REG NO: - ")
            c.drawString(265, 250, reg)
            c.setFont("calibri", 23)
            c.drawString(120, 150, "Paper :- ")
            c.drawString(204, 150, paper_name)

            c.setFont("BAHNSCHRIFT", 20)
            c.drawString(235, 569, stream)
            c.drawString(237, 529, f"SEMESTER {sem}")

            c.save()
            packet.seek(0)
            background = PdfReader("assets/backgrounds/background7.pdf")
            overlay = PdfReader(packet)

            output = PdfWriter()
            background_page = background.pages[0]
            background_page.merge_page(overlay.pages[0])
            output.add_page(background_page)

            # Step 3: Write final PDF to memory
            final_buffer = BytesIO()
            output.write(final_buffer)
            final_buffer.seek(0)

        st.download_button(
            label = "📄 Download PDF",
            data = final_buffer,
            file_name = f"{roll}.pdf",
            mime = "application/pdf"
        )










    #b64_pdf = base64.b64encode(final_buffer.read()).decode("utf-8")
    #pdf_url = f"data:application/pdf;base64,{b64_pdf}"

    # Open in new tab
    #script = f"""
        #<script>
            #const blob = atob("{b64_pdf}");
            #const array = new Uint8Array(blob.length);
            #for (let i = 0; i < blob.length; i++) {{
                #array[i] = blob.charCodeAt(i);
            #}}
            #const pdfBlob = new Blob([array], {{ type: "application/pdf" }});
            #const pdfURL = URL.createObjectURL(pdfBlob);
            #window.open(pdfURL);
        #</script>
    #"""

    #st.components.v1.html(script, height=0)