class quiz:
    rounds=[]
    #def __init__(Self):
        
    def addRound(Self, rnd):
        Self.rounds.append(rnd)

    def dump(Self):
        for rnd in Self.rounds:
            rnd.dump()

class qround:
    questions=[]
    
    #def __init__(Self):
    
    
    def addQuestion(Self, question):
        Self.questions.append(question);
    
    def dump(Self):
        for q in Self.questions:
            q.dump()

class question:
    question=""
    answers={}
    _image=""
    _comment=""
    
    def __init__(Self, q):
        Self.question=q
        
    def addAnswer(Self, answer, correct):
        Self.answers[answer]=correct;
        
    def setImage(Self, image):
        Self._image=image

    def getImage(Self):
        return Self._image
        
    def setComment(Self, comment):
        Self._comment=comment
    
    def getComment(Self):
        return Self._comment
    
    def dump(Self):
        print(Self.question)
        for a in Self.answers:
            print(a)
        
q=quiz()
r=qround()
u=question("Wer erfand Python")
u.addAnswer("Linus Thorvalds", 0)
u.addAnswer("Guido van Rossum", 1)
u.addAnswer("Bill Gates", 0)
u.addAnswer("Monty Python", 0)
r.addQuestion(u)
q.addRound(r)

q.dump()
