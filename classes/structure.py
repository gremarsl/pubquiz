
class quiz:

    def __init__(Self):
        Self.rounds =[]

    #def __init__(Self):
    """Eine Instanz von Runde hinzufügen
    q=quiz()
    r=qround()
    q.addRound(r)
    """
    def addRound(Self, rnd):
        Self.rounds.append(rnd)

    def dump(Self):
        for rnd in Self.rounds:
            rnd.dump()

class qround:

    def __init__(Self, number):
        Self.questions = []
        Self.number = number
        pass

    def addQuestion(Self, question):
        Self.questions.append(question)

    def dump(Self):
        for q in Self.questions:
            q.dump()

class question:

    correctAnswer =""
    question=""
    comment=""

    wrongAnswers=[]

    def __init__(self):
        pass

    def setQuestion(self,question):
        self.question=question
    def getQuestion(self):
        return self.question

    def setCorrectAnswer(self, answer):
        self.correctAnswer = answer
    def getCorrectAnswer(self):
        return self.correctAnswer

    def setWrongAnswer(self, answer):
        self.wrongAnswers.append(answer)
    def getWrongAnswers(self):
        return self.wrongAnswers

    def setImage(self, image):
        self.image = image
    def getImage(self):
        return self.image

    def setComment(self, comment):
        self.comment = comment
    def getComment(self):
        return self.comment