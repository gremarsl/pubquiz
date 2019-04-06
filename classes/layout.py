from pptx import Presentation
from enum import Enum

# layout file name
fileName_layout = "layout.pptx"

# ENUM used to define where are the layouts in the pptx
class _slideIndex(Enum):
    TITLE_SLIDE = 0
    SOG_AD = 1
    RULES = 2
    ROUND_TITLE = 3
    QUESTION_OPEN = 4
    QUESTION_ALTERNATIVE = 5
    QUESTION_MIDDLE = 6
    QUESTION_MIDDLE_ANSWER = 7
    RESULTS = 7



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

    def getGameRules(self):
        """
        Get the slide with the game rules
        :return: Slide Object
        """
        return self.prs.slides[_slideIndex.RULES]
    def getQuestionOpen(self):
        """
        Get the slide with a layout for open (not multiple choice) question
        :return: Slide Object
        """
        return self.prs.slides[_slideIndex.QUESTION_OPEN]
    def getQuestionMultipleChoices(self):
        """
        Get the slide with a layout for multiple choice questions
        :return: Slide Object
        """
        return self.prs.slides[_slideIndex.QUESTION_ALTERNATIVE]
    def getRoundTitle(self):
        """
        The slide used at the beginning of every round
        :return: Slide Object
        """
        return self.prs.slides[_slideIndex.ROUND_TITLE]
    def getQuestionMiddle(self):
        """
        The slide used in-between the rounds (Zwischenfrage)
        :return: Slide Object
        """
        return self.prs.slides[_slideIndex.QUESTION_MIDDLE]
    def getQuestionMiddleAnswer(self):
        """
        The slide used to show the answer for the in-between questions
        :return: Slide Object
        """
        return self.prs.slides[_slideIndex.QUESTION_MIDDLE_ANSWER]
    def getResults(self):
        """
        The slide used to show the charts with results
        :return: Slide Object
        """
        return self.prs.slides[_slideIndex.RESULTS]