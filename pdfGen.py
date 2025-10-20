from fpdf import FPDF as fpdf
import pandas as pd

pdf = fpdf(orientation='P', unit='mm', format='A4')
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    row = row["Topic"]
    pdf.set_font("Times", size=14, style='B')
    pdf.set_text_color(255, 0, 0)
    pdf.cell(w=0, h=14, txt=row, ln=1, align='L')
    pdf.line(10, 20, 200, 20)

pdf.output("topics.pdf")

