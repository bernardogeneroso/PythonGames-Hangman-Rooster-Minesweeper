from random import randint
import os
import json

# linha - coluna
mines = []
columnSize = 8

rows = []
rows_user = []

playerName = ""

def prepareGame():
    global columnSize
    global mines

    while True:
        columnSize = int(input("\nTamanho do campo(pares): "))

        if (columnSize % 2) != 1 and columnSize >= 8:
            break
        else:
            print("O valor precisa de ser par, e no minimo 8!")


    # mines
    for i in range(columnSize):
        while True:
            row_random = randint(0, columnSize - 1)
            column_random = randint(0, columnSize - 1)
            random_point = [row_random, column_random]

            if mines in random_point:
                pass
            else:
                mines.append(random_point)
                break

    # Create rows and columns
    for i in range(columnSize):
        rows.append([])
        rows_user.append([])
        for j in range(columnSize):
            if [i, j] in mines:
                rows[i].append([])
                rows[i][j] = "*"
            else:
                rows[i].append([])
                rows[i][j] = 0

            rows_user[i].append([])
            rows_user[i][j] = " "

    # Bombs sum
    for i in mines:
        if i[0] + 1 <= columnSize - 1 and i[1] - 1 >= 0 and rows[i[0] + 1][i[1] - 1] != "*": rows[i[0] + 1][i[1] - 1] += 1
        if i[0] + 1 <= columnSize - 1 and i[1] + 1 <= columnSize - 1 and rows[i[0] + 1][i[1] + 1] != "*": rows[i[0] + 1][i[1] + 1] += 1
        if i[0] + 1 <= columnSize - 1 and rows[i[0] + 1][i[1]] != "*": rows[i[0] + 1][i[1]] += 1

        if i[1] + 1 <= columnSize - 1 and rows[i[0]][i[1] + 1] != "*": rows[i[0]][i[1] + 1] += 1
        if i[1] - 1 >= 0 and rows[i[0]][i[1] - 1] != "*": rows[i[0]][i[1] - 1] += 1

        if i[0] - 1 >= 0 and rows[i[0] - 1][i[1]] != "*": rows[i[0] - 1][i[1]] += 1
        if i[0] - 1 >= 0 and i[1] - 1 >= 0 and rows[i[0] - 1][i[1] - 1] != "*": rows[i[0] - 1][i[1] - 1] += 1
        if i[0] - 1 >= 0 and i[1] + 1 <= columnSize - 1 and rows[i[0] - 1][i[1] + 1] != "*": rows[i[0] - 1][i[1] + 1] += 1


def showGameDone():
    # Show rows
    for i in range(columnSize):
        if i == 0:
            print('\t')
            for z in range(columnSize):
                if z == 0:
                    print('\t╔═══╦', end='')
                elif z == (columnSize - 1):
                    print('═══╗')
                else:
                    print('═══╦', end='')
        for j in range(columnSize):
            if j == 0:
                print('\t║ {0} ║'.format(rows[i][j]), end='')
            elif j == columnSize - 1:
                print(' {0} ║'.format(rows[i][j]))
            else:
                print(' {0} ║'.format(rows[i][j]), end='')
        if i == columnSize - 1:
            for l in range(columnSize):
                if l == 0:
                    print('\t╚═══╩', end='')
                elif l == (columnSize - 1):
                    print('═══╝')
                else:
                    print('═══╩', end='')
        else:
            for n in range(columnSize):
                if n == 0:
                    print('\t╠═══╬', end='')
                elif n == (columnSize - 1):
                    print('═══║')
                else:
                    print('═══╬', end='')


def showGameInProgress():
    # Show rows
    for i in range(columnSize):
        if i == 0:
            print('\t', end='')
            for u in range(columnSize):
                if u >= 10:
                    print('  {0}  '.format(u + 1), end='')
                else:
                    print('   {0}  '.format(u + 1), end='')
            print('\t')
            for z in range(columnSize):
                if z == 0:
                    print('\t╔═════╦', end='')
                elif z == (columnSize - 1):
                    print('═════╗')
                else:
                    print('═════╦', end='')
        for j in range(columnSize):
            if j == 0:
                print('{0}\t║  {1}  ║'.format(i + 1, rows_user[i][j]), end='')
            elif j == columnSize - 1:
                print('  {0}  ║'.format(rows_user[i][j]))
            else:
                print('  {0}  ║'.format(rows_user[i][j]), end='')
        if i == (columnSize - 1):
            for l in range(columnSize):
                if l == 0:
                    print('\t╚═════╩', end='')
                elif l == (columnSize - 1):
                    print('═════╝')
                else:
                    print('═════╩', end='')
        else:
            for n in range(columnSize):
                if n == 0:
                    print('\t╠═════╬', end='')
                elif n == (columnSize - 1):
                    print('═════║')
                else:
                    print('═════╬', end='')

def scoreGame():
    global playerName

    fileNameScores = "scores.json"

    if os.path.exists(fileNameScores):
        if os.stat(fileNameScores).st_size != 0:
            with open(fileNameScores, encoding='utf8') as json_file:
                dataOfScoresDict = json.load(json_file)

            try:
                dataOfScoresDict[playerName] += 1
            except:
                dataOfScoresDict[playerName] = 1
                pass

            with open(fileNameScores, "w", encoding='utf8') as json_file:
                json.dump(dataOfScoresDict, json_file, sort_keys=True)
        else:
            dataOfScoresDict = {}
            dataOfScoresDict[playerName] = 1


            with open(fileNameScores, "w", encoding='utf8') as json_file:
                json.dump(dataOfScoresDict, json_file, sort_keys=True)
    else:
        dataOfScoresDict = {}
        dataOfScoresDict[playerName] = 1

        with open(fileNameScores, "w", encoding='utf8') as json_file:
            json.dump(dataOfScoresDict, json_file, sort_keys=True)

def playrNameCheck():
    while True:
        playerName = input("Nome do jogador: ")

        if playerName != "":
            break
        else:
            print("Precisa de inserir um nome!")

def questionPlayer():
    showGameInProgress()

    while True:
        print('''
            1 - Bandeira
            2 - Jogar
            3 - Deseja sair do jogo
            ''')

        choicePlayer = int(input("Qual das opções deseja: "))

        if 1 <= choicePlayer <= 2:
            break
        elif choicePlayer == 3:
            return 0, 0, 0, True

    while True:
        row_player = int(input("\nLinha: "))
        column_player = int(input("Coluna: "))

        if checkMove(row_player, column_player):
            break

    return choicePlayer, row_player - 1, column_player - 1, False


def checkMove(row, column):
    if 1 <= row <= columnSize and 1 <= column <= columnSize:
        return True
    else:
        return False


def playerMove(row, column):
    if rows[row][column] == "*":
        return False
    else:
        rows_user[row][column] = rows[row][column]
        return True


def playerAddFlag(row, column):
    rows_user[row][column] = "🚩"

def checkGameDown():
    for i in mines:
        if rows_user[i[0]][i[1]] != "🚩":
            return False
    return True


def runGame():
    prepareGame()

    playrNameCheck()

    while True:
        if checkGameDown():
            showGameDone()
            print("\nParabêns completou o jogo")
            scoreGame()
            break

        [choicePlayer, row_player, column_player, leave] = questionPlayer()

        if leave:
            showGameDone()
            print("\nSair do campo de minas")
            break
        elif choicePlayer == 1:
            playerAddFlag(row_player, column_player)
        else:
            if playerMove(row_player, column_player):
                showGameInProgress()
            else:
                showGameDone()
                print("\nBomb explode")
                break