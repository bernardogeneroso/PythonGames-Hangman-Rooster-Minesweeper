import json, os

fileName = "scores.json"

def scoreRun():
    if os.path.exists(fileName):
        if os.stat(fileName).st_size != 0:
            with open(fileName, encoding='utf8') as json_file:
                dataOfScoresDict = json.load(json_file)

            print('\tPontuções\n')

            for x in dataOfScoresDict:
                print("\t{0} pontuação {1}".format(x, dataOfScoresDict[x]))

    input("\nClique numa tecla para continuar...")