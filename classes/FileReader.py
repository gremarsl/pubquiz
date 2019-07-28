import os
import glob

import classes.structure as struct

class FileReader:

    def __init__(self):
        print("init")
        pass

    def readAllCsvFiles(self,directoryToFiles):
        print("start reading Csv File With quesetions")
        questions=[]
        correctAnswers=[]
        wrongAnswers=[]
        comments=[]
        pictures=[]

        folder=directoryToFiles+'/readin_data/'

        for file in glob.glob(os.path.join(folder, '*.csv')):

            round_struct = struct.qround(1)

            with open(file) as file:
                # skip first line (First Line for explanation and syntax )
                next(file)
                #skipt second line
                next(file)
                for line in file:
                    question=line[0]
                    quest_sruct = struct.question(line[0])
                    linelist=line[1:]
                    linelist= linelist.split(",")
                    for element in linelist:
                        if '?' in element:
                            questions.append(question)
                        elif '*' in element:
                            correctAnswers.append(element[1:])
                        elif '#' in element:
                            comments.append(element[1:])
                        elif '~' in element:
                            pictures.append(element[1:])
                        elif len(element)==0:
                            linelist.remove(element)
                        elif '\n'==element:
                            continue
                        else:
                            wrongAnswers.append(element)
                '''
                for corr_answer in correctAnswers:
                    quest_sruct.addAnswer(answer=corr_answer, correct=True)

                for wrong_answer in wrongAnswers:
                    quest_sruct.addAnswer(answer=wrong_answer, correct=False)
                '''
        return print("reading done")