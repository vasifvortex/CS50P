from fpdf import FPDF
i=input("Enter name: ").strip()
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 45)
pdf.cell(0, 60, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=0, y=70)
pdf.set_font_size(30)
pdf.set_text_color(255,255,255)
pdf.cell(-180, 270, f"{i} took CS50", align="C")
pdf.output("shirtificate.pdf")
