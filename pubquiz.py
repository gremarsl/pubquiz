#TEST!
#TESTvismgl
from pptx import Presentation
from pptx.util import Inches, Pt

#insert picture
img_path = 'pubquiz.png'
zickzack='zickzack.png'
logo='logo.png'

#create presentation object 
prs = Presentation()
#layout settings
blank_slide_layout = prs.slide_layouts[6]

numberOfQuestions=10

#create list of questions and append to list
#TODO: create list of variable length (egal ob 10 oder 12 Fragen) - das können wir dann ggf ausbauen,
    #wenn wir ein erstes funktionierendes skript haben
questions=list()
answers=list()

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

#create the answers - can be filled as desired since of type list possible: (for i in range(1,numberOfQuestions):
#TODO: parametrise the numberOfQuestions
answer1=["A) Das ist die erste Auswahlmöglichkeit",
         "B) Das ist die weite Auswahlmöglichkeit",
         "C)Hier könnte die 3. AM stehen",
         "D) usw."]
answer2=["A) Das ist die erste Auswahlmöglichkeit",
         "B) Das ist die weite Auswahlmöglichkeit",
         "C)Hier könnte die 3. AM stehen",
         "D) usw."]
answer3=["A) Das ist die erste Auswahlmöglichkeit",
         "B) Das ist die weite Auswahlmöglichkeit",
         "C)Hier könnte die 3. AM stehen",
         "D) usw."]
answer4=["A) Das ist die erste Auswahlmöglichkeit",
         "B) Das ist die weite Auswahlmöglichkeit",
         "C)Hier könnte die 3. AM stehen",
         "D) usw."]
answer5=["A) Das ist die erste Auswahlmöglichkeit",
         "B) Das ist die weite Auswahlmöglichkeit",
         "C)Hier könnte die 3. AM stehen",
         "D) usw."]
answer6=["A) Das ist die erste Auswahlmöglichkeit",
         "B) Das ist die weite Auswahlmöglichkeit",
         "C)Hier könnte die 3. AM stehen",
         "D) usw."]
answer7=["A) Das ist die erste Auswahlmöglichkeit",
         "B) Das ist die weite Auswahlmöglichkeit",
         "C)Hier könnte die 3. AM stehen",
         "D) usw."]
answer8=["A) Das ist die erste Auswahlmöglichkeit",
         "B) Das ist die weite Auswahlmöglichkeit",
         "C)Hier könnte die 3. AM stehen",
         "D) usw."]
answer9=["A) Das ist die erste Auswahlmöglichkeit",
         "B) Das ist die weite Auswahlmöglichkeit",
         "C)Hier könnte die 3. AM stehen",
         "D) usw."]
answer10=["A) Das ist die erste Auswahlmöglichkeit",
         "B) Das ist die weite Auswahlmöglichkeit",
         "C)Hier könnte die 3. AM stehen",
         "D) usw."]


#TODO: how to structure the answers?
#TODO wollen wir es in einer liste von liste gestalten oder in einem 2D-Array?
#add answers to allAnswers
# möglichkeit, schnell und dynamisch füllen mit for schleife
answers.append(answer1)
answers.append(answer2)
answers.append(answer3)
answers.append(answer4)
answers.append(answer5)
answers.append(answer6)
answers.append(answer7)
answers.append(answer8)
answers.append(answer9)
answers.append(answer10)


#scaling
left = Inches(1)  
top = Inches(1)
width = Inches(8)
height = Inches(5.5)
#add picture

#first slide 
first = prs.slides.add_slide(blank_slide_layout)

# Syntaxerklärung: img_path, Abstand des Bilds vom linken Folienrand, ... zum oberen Folienrand, Breite des Bildes ,Höhe des Bildes
first.shapes.add_picture(img_path, Inches(1), Inches(1.5),Inches(8),Inches(5.5))
first.shapes.add_textbox(left, top, width, height).text_frame.text="Willkommen zum Pubquiz der SOG LG_XXX"
#second slide - about us
second = prs.slides.add_slide(blank_slide_layout)
second.shapes.add_picture(img_path, Inches(1), Inches(1.5),Inches(8),Inches(5.5))
second.shapes.add_textbox(left, top, width, height).text_frame.text="Hier könnt ihr Informationen über SOG zeigen"
#third slide - rules
third = prs.slides.add_slide(blank_slide_layout)
pic = third.shapes.add_picture(img_path, Inches(1), Inches(1.5),Inches(8),Inches(5.5))
third.shapes.add_textbox(left, top, width, height).text_frame.text="Hier könnt ihr Regeln definieren"
#second slide - about us

questionCounter=1
left = Inches(2.5)
top = Inches(1)
width = Inches(8)
height = Inches(5.5)
for i in range(10):
    
    slide = prs.slides.add_slide(blank_slide_layout)
    slide.shapes.add_picture(zickzack,Inches(0), Inches(0),Inches(2),Inches(8))
    slide.shapes.add_picture(logo,Inches(8), Inches(5.5),Inches(2),Inches(1.6))

    #add textbox
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.text = "SOG Pubquiz"

    frage = tf.add_paragraph()
    frage.text = "Frage" + str(questionCounter)
    frage.font.size = Pt(40)
    frage.font.bold = True
    questionTextBox = tf.add_paragraph()
    questionTextBox.size=Pt(40)
    frage.font.bold=True
    questionTextBox.text = questions[i]

    answer = tf.add_paragraph()
    
    #TODO: extract answers and write it into the textbox
    #added test #TODO
    answer.text = str(answers[i])
    answer.font.size = Pt(32)
    answer.font.bold = True
    questionCounter+=1
    i+=1


#save file
prs.save('pubquiz_LG_Stuttgart.pptx')
