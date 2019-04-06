from pptx import Presentation
from enum import Enum

# layout file name
fileName_layout = "layout.pptx"

# for testing purposes
fileName_output = "outputTest.pptx"

# ENUM used to define where are the layouts in the pptx
class _slideIndex(Enum):
    TITLE_SLIDE = 0
    SOG_AD = 1
    RULES = 2
    QUESTION_OPEN = 3
    QUESTION_ALTERNATIVE = 4



# the Layout Class
class Layout:
    """
    Used to get the Slides objects used as template
    """

    def __init__(self, pathLayout=fileName_layout):
        # opening the layout
        self.prs = Presentation(fileName_layout)

    def getTitleSlide(self):
        """
        Get the slide used as the Title one, the first
        :return: Slide object
        """
        return self.prs.slides[_slideIndex.TITLE_SLIDE]

    def getSOGadvertisement(self):
        """
        Get the slide used to show what is SOG
        :return: Slide object
        """
        return self.prs.slides[_slideIndex.SOG_AD]
