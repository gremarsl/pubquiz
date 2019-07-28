import os
from pptx import Presentation
from pptx.util import Inches, Pt

#insert picture
from classes.FileReader import FileReader

img_path = 'pubquiz.png'
zickzack='zickzack.png'
logo='logo.png'

#create presentation object 
prs = Presentation()
#layout settings
blank_slide_layout = prs.slide_layouts[6]

numberOfQuestions=10

FileReader = FileReader()
directoryToFile = os.path.dirname(__file__)
print(directoryToFile)
questions = FileReader.readAllCsvFiles(directoryToFile)
#save file
prs.save('pubquiz_LG_Stuttgart.pptx')

