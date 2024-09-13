from fpdf import FPDF as fp
import pandas as pd

pdf = fp(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page("output.pdf")
    pdf.set_font(family="times", style="b", size=24)
    pdf.set_text_color(10, 10, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 22, 200, 22)


pdf.output("output.pdf")