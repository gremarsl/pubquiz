import os
import glob
import classes.structure as structure

class FileReader:

    def __init__(self):
        print("init")
        pass

    def readAllCsvFiles(self,directoryToFiles):
        print("start reading Csv File With quesetions")


        folder=directoryToFiles+'/readin_data/'

        for file in glob.glob(os.path.join(folder, '*.csv')):

            with open(file) as file:
                # skip first two line (First Line for explanation and syntax )
                next(file)
                next(file)
                num_lines = sum(1 for line in file)

                questions = [structure.question() for i in range(num_lines)]
                file.seek(0)
                # skip first two line (First Line for explanation and syntax )
                next(file)
                next(file)
                for line in file:

                    linelist=line[1:]
                    linelist= linelist.split(",")

                    questioncounter=0
                    for element in linelist:
                        if '?' in element:
                            questions[questioncounter].setQuestion(element)
                        elif '*' in element:
                            questions[questioncounter].setCorrectAnswer(element)
                        elif '#' in element:
                            questions[questioncounter].setComment(element)
                        elif '~' in element:
                            questions[questioncounter].setImage(element)
                        elif len(element)==0:
                            linelist.remove(element)
                        elif '\n'==element:
                            continue
                        else:
                            questions[questioncounter].setWrongAnswer(element)
                    questioncounter += 1
        print("reading done")
        return questions