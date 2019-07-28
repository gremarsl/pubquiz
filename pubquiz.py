import os
from classes.layout import Layout
from classes.FileReader import FileReader
from pptx import Presentation

FileReader = FileReader()
directoryToFile = os.path.dirname(__file__)
print(directoryToFile)
questions = FileReader.readAllCsvFiles(directoryToFile)
#save file

pres= Presentation()
pres.save('pubquiz.pptx')

