
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

