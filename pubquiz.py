from pptx import Presentation
from pptx.util import Inches, Pt

#insert picture
img_path = 'benefiz.jpg'

#create presentation object 
prs = Presentation()
#layout settings
blank_slide_layout = prs.slide_layouts[6]

#add slide
slide1 = prs.slides.add_slide(blank_slide_layout)
slide2 = prs.slides.add_slide(blank_slide_layout)

#scaling
left = Inches(1)
top = Inches(1)
top1 = Inches(1.5)
width = Inches(8)
height = Inches(5.5)
#add picture
pic = slide1.shapes.add_picture(img_path, left, top1,width,height)
slide1.shapes.add_textbox(left, top, width, height).text_frame.text="Willkommen zum Pubquiz der SOG LG_Stuttgart"

#add textbox
txBox = slide2.shapes.add_textbox(left, top, width, height)
tf = txBox.text_frame
tf.text = "Die LG_Stuttgart ist einfach die Beste ;-)"

p = tf.add_paragraph()
p.text = "HalliHallo"
p.font.bold = True

p = tf.add_paragraph()
p.text = "HalloHalli"
p.font.size = Pt(40)


#save file
prs.save('pubquiz_LG_Stuttgart.pptx')
