from fpdf import FPDF as fpdf
import pandas as pd

pdf = fpdf(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    topic = row["Topic"]
    pages = row['Pages']
    pdf.set_font("Times", size=14, style='B')
    pdf.set_text_color(255, 0, 0)
    pdf.cell(w=0, h=14, txt=topic, ln=1, align='L')
    pdf.line(10, 20, 200, 20)

    # Footer
    pdf.ln(265)
    pdf.set_font("Arial", size=10, style='B')
    pdf.set_text_color(200, 200, 200)
    pdf.cell(w=0, h=10, txt=topic, ln=1, align='R')


    for i in range(pages-1):
        pdf.add_page()

        # Footer
        pdf.ln(279)
        pdf.set_font("Arial", size=10, style='B')
        pdf.set_text_color(200, 200, 200)
        pdf.cell(w=0, h=10, txt=topic, ln=1, align='R')
        

pdf.output("Topics.pdf")

