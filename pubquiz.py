import os
from classes.layout import Layout
from classes.FileReader import FileReader
from pptx import Presentation

FileReader = FileReader()
directoryToFile = os.path.dirname(__file__)
print(directoryToFile)
questions=FileReader.readAllCsvFiles(directoryToFile)
print(questions[0].getQuestion())
print(questions[1].getQuestion())
print(questions[2].getQuestion())
print(questions[3].getQuestion())
print(questions[4].getQuestion())

#save file

pres= Presentation()
pres.save('pubquiz.pptx')

