# Implemente o algoritmo e implemente o programa do jogo galo (https://pt.wikipedia.org/wiki/Jogo_da_velha).

import os, sys, json

leaveInGame = True
playerActive = [0, 'X']
players_info = []
position = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def clear():
    if os.name == 'nt':
        return os.system('cls') # Windows
    else:
        return os.system('clear') # Linux & MacOS

def apresentatiomGame():
    print('''
         ▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄  ▄▄▄▄▄▄    ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄     ▄▄   ▄▄ ▄▄▄▄▄▄ 
        █   █       █       █       █  █      ██      █  █  █ █  █       █   █   █  █ █  █      █
        █   █   ▄   █   ▄▄▄▄█   ▄   █  █  ▄    █  ▄   █  █  █▄█  █    ▄▄▄█   █   █  █▄█  █  ▄   █
     ▄  █   █  █ █  █  █  ▄▄█  █ █  █  █ █ █   █ █▄█  █  █       █   █▄▄▄█   █   █       █ █▄█  █
    █ █▄█   █  █▄█  █  █ █  █  █▄█  █  █ █▄█   █      █  █       █    ▄▄▄█   █▄▄▄█   ▄   █      █
    █       █       █  █▄▄█ █       █  █       █  ▄   █   █     ██   █▄▄▄█       █  █ █  █  ▄   █
    █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄▄▄▄▄██▄█ █▄▄█    █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄█ █▄▄█
    ''')

def printGame():
    print("\n\t\t\t\t╔═══╦═══╦═══╗\t╔═══╦═══╦═══╗")
    print("\t\t\t\t║ {0} ║ {1} ║ {2} ║\t║ 7 ║ 8 ║ 9 ║".format(position[6], position[7], position[8]))
    print("\t\t\t\t╠═══╬═══╬═══║\t╠═══╬═══╬═══║")
    print("\t\t\t\t║ {0} ║ {1} ║ {2} ║\t║ 4 ║ 5 ║ 6 ║".format(position[3], position[4], position[5]))
    print("\t\t\t\t╠═══╬═══╬═══║\t╠═══╬═══╬═══║")
    print("\t\t\t\t║ {0} ║ {1} ║ {2} ║\t║ 1 ║ 2 ║ 3 ║".format(position[0], position[1], position[2]))
    print("\t\t\t\t╚═══╩═══╩═══╝\t╚═══╩═══╩═══╝\n")

def printStructure():
    print('''
    \t\t\t\t\t╔═══╦═══╦═══╗
    \t\t\t\t\t║ 7 ║ 8 ║ 9 ║
    \t\t\t\t\t╠═══╬═══╬═══║
    \t\t\t\t\t║ 4 ║ 5 ║ 6 ║
    \t\t\t\t\t╠═══╬═══╬═══║
    \t\t\t\t\t║ 1 ║ 2 ║ 3 ║
    \t\t\t\t\t╚═══╩═══╩═══╝
   -----------------------------------------------------------------------------------------------  
    ''')

def printDefaultGame():
    print("\t\t\t\t\t╔═══╦═══╦═══╗")
    print("\t\t\t\t\t║ {0} ║ {1} ║ {2} ║".format(position[6], position[7], position[8]))
    print("\t\t\t\t\t╠═══╬═══╬═══║")
    print("\t\t\t\t\t║ {0} ║ {1} ║ {2} ║".format(position[3], position[4], position[5]))
    print("\t\t\t\t\t╠═══╬═══╬═══║")
    print("\t\t\t\t\t║ {0} ║ {1} ║ {2} ║".format(position[0], position[1], position[2]))
    print("\t\t\t\t\t╚═══╩═══╩═══╝")


def changePlayer():
    if playerActive[0] == 0:
        playerActive[0] = 1
        playerActive[1] = 'O'
    else:
        playerActive[0] = 0
        playerActive[1] = 'X'


def checkPositionIsFull():
    for i in position:
        if i == "-":
            return False
    return True

def scoreGame(playerName):
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

def positionPlayed(key):
    try:
        if key < 0 | key > 9:
            return "Posição inválida";
        keyPosition = key - 1
        actualPositoin = position[keyPosition]
        if actualPositoin == "X" or actualPositoin == "O":
            return "Já se encontra ocupada pelo {0}".format(actualPositoin)
        else:
            position[keyPosition] = playerActive[1]
        return None;
    except:
        return "Posição inválida"


def validateGame():
    leftToRightVertical = [0, 3, 6]
    topToBottomHorizontal = [-3, -2, -1]

    for i in range(0, 3):
        if position[leftToRightVertical[0] + i] == playerActive[1] and position[leftToRightVertical[1] + i] == \
                playerActive[1] and position[leftToRightVertical[2] + i] == playerActive[1]:
            return True
        elif position[topToBottomHorizontal[0] + 3] == playerActive[1] and position[topToBottomHorizontal[1] + 3] == \
                playerActive[1] and position[topToBottomHorizontal[2] + 3] == playerActive[1]:
            return True

    if position[0] == playerActive[1] and position[4] == playerActive[1] and position[8] == playerActive[1]:
        return True
    elif position[2] == playerActive[1] and position[4] == playerActive[1] and position[6] == playerActive[1]:
        return True

    changePlayer()
    return False

def endGame():
    clear()
    print("\n\n\n\n")
    apresentatiomGame()
    printDefaultGame()

    print("\tO jogador {0} ganhou!".format(players_info[playerActive[0]]))
    scoreGame(players_info[playerActive[0]])

    input("\n\n\tPara continuar clique em qualquer tecla...")

def leaveInGameCheck(exit):
    if exit == "S" or exit == "s":
        global leaveInGame
        leaveInGame = False
    else:
        global playerActive
        global position
        playerActive = [0, 'X']
        position = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        players_info.clear()

def playersInfo():
    # Informação dos jogadores
    for i in range(0, 2):
        global playerName
        if i == 0:
            while True:
                try:
                    playerName = input("\tNome do 1º jogador(X): ")
                    if not playerName:
                        raise ValueError('\tOcorreu um erro: Input vazio')
                    break
                except ValueError as e:
                    print(e)
                except KeyboardInterrupt:
                    clear()
                    print("Sair do jogo da velha...")
                    sys.exit(1)
        else:
            while True:
                try:
                    playerName = input("\tNome do 2º jogador(X): ")
                    if not playerName:
                        raise ValueError('\tOcorreu um erro: Input vazio')
                    break
                except ValueError as e:
                    print(e)
                except KeyboardInterrupt:
                    clear()
                    print("Sair do jogo da velha...")
                    sys.exit(1)
        players_info.append(playerName)

def runPlayerInteractive():
    responseGameBool = False

    # Estrutura inicial
    clear()
    apresentatiomGame()
    printStructure()

    # Jogo
    while True:
        for i in range(0, 2):
            while True:
                if checkPositionIsFull(): break
                global player
                while True:
                    try:
                        player = int(input("\t{0} escolhe a posição({1}): ".format(players_info[playerActive[0]], playerActive[1])))
                        break
                    except ValueError:
                        print("\tOcorreu um erro: Input incorrecto")
                    except KeyboardInterrupt:
                        clear()
                        print("Sair do jogo da velha...")
                        sys.exit(1)
                confirmation = positionPlayed(player)
                if confirmation is None:
                    responseGameBool = validateGame()
                    if responseGameBool: break
                    break
                else:
                    print("\tOcorreu um erro:", confirmation)
            if checkPositionIsFull(): break
            if responseGameBool: break
            printGame()
        if checkPositionIsFull(): break
        if responseGameBool: break

    if responseGameBool:
        endGame()
    else:
        clear()
        apresentatiomGame()
        printDefaultGame()
        print("\n\n\t\t\t\t\t  Deu velha!")
        input("\n\n\tPara continuar clique em qualquer tecla...")

####################################################################################################


def runGame():
    while leaveInGame:
        # Limpar a consola
        clear()

        # Apresentação do jogo
        apresentatiomGame()

        # Informações dos jogadores
        playersInfo()

        # LoadGame
        runPlayerInteractive()

        # Sair do jogo
        clear()
        apresentatiomGame()
        leaveInGameCheck(input("\n\n\tDeseja sair do jogo(S/N): "))