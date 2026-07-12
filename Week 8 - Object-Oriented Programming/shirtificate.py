from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# Title
pdf.set_font("Helvetica", "B", 24)
pdf.cell(0, 20, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

# Shirt image
pdf.image("shirtificate.png", x=15, y=60, w=180)

# Name on shirt
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 140)
pdf.cell(210, 10, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
