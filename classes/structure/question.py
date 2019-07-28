class question:
    question = ""
    answers = []
    _image = ""
    _comment = ""

    def __init__(Self, q):
        Self.question = q

    def addAnswer(Self, answer, correct):
        Self.answers[answer] = correct;

    def setImage(Self, image):
        Self._image = image

    def getImage(Self):
        return Self._image

    def setComment(Self, comment):
        Self._comment = comment

    def getComment(Self):
        return Self._comment

    def dump(Self):
        print(Self.question)
        for a in Self.answers:
            print(a)


