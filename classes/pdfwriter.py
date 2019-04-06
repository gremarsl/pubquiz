#!/usr/bin/python3
import structure as struct
from fpdf import FPDF
 

q=struct.quiz()
r=struct.qround(1)
u=struct.question("Wer erfand Python")
u.addAnswer("Linus Thorvalds", 0)
u.addAnswer("Guido van Rossum", 1)
u.addAnswer("Bill Gates", 0)
u.addAnswer("Monty Python", 0)
r.addQuestion(u)
q.addRound(r)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 8, txt="Runde 1", ln=1, align="C")
pdf.cell(200, 20, txt="Lustige Fragen", ln=1, align="C")

pdf.cell(200, 8, txt="Wer erfand Python?", ln=1, align="L")
pdf.cell(200, 8, txt="Linus Thorvalds", ln=1, align="L")
pdf.cell(200, 8, txt="Guido van Rossum", ln=1, align="L")
pdf.cell(200, 8, txt="Linus Bill Gates", ln=1, align="L")
pdf.cell(200, 8, txt="Linus Monty Python", ln=1, align="L")


pdf.output("../handout.pdf")
