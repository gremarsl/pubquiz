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
