import os
import glob
import classes.structure as structure

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

            round_struct = structure.qround(1)

            with open(file) as file:
                # skip first line (First Line for explanation and syntax )
                next(file)
                #skipt second line
                next(file)
                num_lines = sum(1 for line in file)

                #FIXME: -2 depend on number of skipped files
                questions = [structure.question() for i in range(num_lines)]
                for line in file:

                    linelist=line[1:]
                    linelist= linelist.split(",")

                    questioncounter=0
                    for element in linelist:
                        questioncounter+=1
                        if '?' in element:
                            questions[questioncounter].addquestion(element)

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