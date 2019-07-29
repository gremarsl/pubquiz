import os
from classes.layout import Layout
from classes.FileReader import FileReader
from pptx import Presentation

FileReader = FileReader()
directoryToFile = os.path.dirname(__file__)
print(directoryToFile)
questions=FileReader.readAllCsvFiles(directoryToFile)

presentation=Presentation()
layout=Layout()

titleSlide=layout.getTitleSlide()

blank_slide_layout = presentation.slide_layouts[6]
print(type(blank_slide_layout))
print(type(titleSlide))

presentation.save('pubquiz.pptx')

