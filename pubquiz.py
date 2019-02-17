from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()
blank_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_slide_layout)

left = top = width = height = Inches(1)
txBox = slide.shapes.add_textbox(left, top, width, height)
tf = txBox.text_frame

tf.text = "This is text inside a textbox"

p = tf.add_paragraph()
p.text = "HalliHallo"
p.font.bold = True

p = tf.add_paragraph()
p.text = "HalloHalli"
p.font.size = Pt(40)

prs.save('pubquiz_LG_Stuttgart.pptx')