import os
import glob

class questions:

    def readAllCsvFiles(self):

        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, 'readin_data/file.csv')

        for file in glob.glob("*.csv"):

            with open(file) as file:
                for line in file:
                    
                    question, answer, answer = line.split(',')


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