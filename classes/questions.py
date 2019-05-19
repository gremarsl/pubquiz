import os
import glob
import csv
import classes.structure as struct

class questions:

    def __init__(self):
        print("init")
        pass

    def readAllCsvFiles(self,directoryToFiles):
        print("start")

        questions=[]
        correctAnswers=[]
        wrongAnswers=[]
        comments=[]
        pictures=[]

        folder=directoryToFiles+'/readin_data/'

        for file in glob.glob(os.path.join(folder, '*.csv')):

            dummy_number = 1
            round_struct = struct.qround(1)

            with open(file) as file:
                csvfile = csv.reader(file)

                for line in csvfile:

                    question=line[0]
                    quest_sruct = struct.question(line[0])
                    linelist=line[1:]
                    for element in linelist:

                        if '*' in element:
                            correctAnswers.append(element[1:])
                            correctAnswers.append(element[1:2])
                        elif '#' in element:
                            comments.append(element[1:])
                        elif '~' in element:
                            pictures.append(element[1:])
                        elif len(element)==0:
                            linelist.remove(element)
                        else:
                            wrongAnswers.append(element)

                    questions.append(question)

                for corr_answer in correctAnswers:
                    quest_sruct.addAnswer(answer=corr_answer, correct=True)

                for wrong_answer in wrongAnswers:
                    quest_sruct.addAnswer(answer=wrong_answer, correct=False)

        return print("reading done")
