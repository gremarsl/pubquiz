
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
    answers = []


    def __init__(self):
        pass
    def addQuestion(self,question):
        self.question=question

    def addAnswer(self, answer, correct):
        self.answers[answer] = correct;

    def setImage(self, image):
        self.image = image

    def getImage(self):
        return self.image

    def setComment(self, comment):
        self.comment = comment

    def getComment(self):
        return self.comment