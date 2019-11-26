import os
import glob
import classes.structure as structure


def skipfirstlines(file):
    next(file)
    next(file)
    next(file)
    next(file)
    pass


class FileReader:

    def __init__(self):
        print("init")
        pass

    def readAllCsvFiles(self,directoryToFiles):
        print("start reading Csv File With questions")

        folder=directoryToFiles+'/pubquizfragen/'

        for file in glob.glob(os.path.join(folder, '*.csv')):

            with open(file) as file:
                # skip first four line (First Line for explanation and syntax)
                skipfirstlines(file)


                num_lines = sum(1 for line in file)

                questions = [structure.question() for i in range(num_lines)]
                #start reading from the first caracter:
                file.seek(0)
                # skip lines (First Line for explanation and syntax )
                skipfirstlines(file)

                questioncounter = 0
                for line in file:

                    linelist=line[1:]
                    linelist= linelist.split(",")

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
