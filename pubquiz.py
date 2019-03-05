from pptx import Presentation
from pptx.util import Inches, Pt

#insert picture 
#you can find the file to store locally in the trunk
img_path = 'pubquiz.png'

#create presentation object 
prs = Presentation()
#layout settings
blank_slide_layout = prs.slide_layouts[6]

questions=list()
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")




#scaling
left = Inches(1)
top = Inches(1)
top1 = Inches(1.5)
width = Inches(8)
height = Inches(5.5)
#add picture

#first slide 
first = prs.slides.add_slide(blank_slide_layout)
pic = first.shapes.add_picture(img_path, Inches(1), Inches(1.5),Inches(8),Inches(5.5))
first.shapes.add_textbox(left, top, width, height).text_frame.text="Willkommen zum Pubquiz der SOG LG_Stuttgart"
#second slide - about us
second = prs.slides.add_slide(blank_slide_layout)
pic = second.shapes.add_picture(img_path, Inches(1), Inches(1.5),Inches(8),Inches(5.5))
second.shapes.add_textbox(left, top, width, height).text_frame.text="AboutUs"
#third slide - rules
third = prs.slides.add_slide(blank_slide_layout)
pic = third.shapes.add_picture(img_path, Inches(1), Inches(1.5),Inches(8),Inches(5.5))
third.shapes.add_textbox(left, top, width, height).text_frame.text="Rules"
#second slide - about us

questionCounter=1
for question in questions:
    
    slide = prs.slides.add_slide(blank_slide_layout)
    left = Inches(1)
    top = Inches(1)
    top1 = Inches(1.5)
    width = Inches(8)
    height = Inches(5.5)
    
    #add textbox
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.text = ""

    frage = tf.add_paragraph()
    frage.text = "Frage" + str(questionCounter)
    frage.font.size = Pt(32)
    frage.font.bold = True
    questionTextBox = tf.add_paragraph()
    questionTextBox.text = question + str(questionCounter)

    answer = tf.add_paragraph()
    answer.text = "ANSWER"

                           
    answer.text = "answer"
    answer.font.size = Pt(32)
    answer.font.bold = True
    questionCounter+=1


#save file
prs.save('pubquiz_LG_Stuttgart.pptx')
