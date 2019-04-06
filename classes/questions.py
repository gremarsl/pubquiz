import os
import glob
import csv
import classes.structure as struct

class questions:

    def __init__(self):
        pass

    def readAllCsvFiles(self):
        questions=[]
        correctAnswers=[]
        wrongAnswers=[]
        comments=[]

        dir = os.path.dirname(__file__)



        for file in glob.glob(dir, "*.csv"):


            dummy_number = 1
            round_struct = struct.qround(1)


            with open(file) as file:
                csvfile = csv.reader(file)

                for line in file:

                    question, answer, answer = line.split(',')
                    questions.append(question)
                    correctAnswers.append()
                    wrongAnswers.append()

                    ## added by Samuel
                    quest_sruct = struct.question(question)

                    for corr_answer in correctAnswers:
                        quest_sruct.addAnswer(answer=corr_answer, correct=true)

                    for wrong_answer in wrongAnswers:
                        quest_sruct.addAnswer(answer=wrong_answer, correct=false)


                    #TODO implement if comment is added
                    if():
                        dummy_comment = 'xy'

                    else:
                        print("no comment")



        return print("reading done")

'''
q.append("Wie heißt Yoda’s Spezies?")
q.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
questions.append("Wie heißt Yoda’s Spezies?")
'''