import os
import glob
import csv

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

            with open(file) as file:
                csvfile = csv.reader(file)

                for line in file:

                    question, answer, answer = line.split(',')
                    questions.append(question)
                    correctAnswers.append()
                    wrongAnswers.append()

                    #TODO implement if comment is added
                    if():
                        comments
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