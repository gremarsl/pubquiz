# testing our Layout class
from classes.layout import Layout
from pptx import Presentation

# for testing purposes
fileName_output = "layoutTester.pptx"

layout = Layout()

prs = Presentation()

slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)

prs.slides[0] = layout.getGameRules()

prs.save(fileName_output)