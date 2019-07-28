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