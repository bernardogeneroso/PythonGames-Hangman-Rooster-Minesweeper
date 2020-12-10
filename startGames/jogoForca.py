# Jogo da forca

import random
import re
import json
import os

words = ["Morango", "Banana", "Abacaxi", "Avaria", "Canela", "Computador", "Leopardo", "Steve", "Jogador"]
word = []
realWord = ""
stateOfGame = 0
validateCharacterInWordBool = True
leaveInGame = True
saveRandomCategory = ""
playerName = ""
fileName = "savedForce.json"

def wordChoice():
    global realWord, saveRandomCategory

    randomOption = random.randint(1, 5)

    with open('categories.json', encoding='utf8') as f:
        data = json.load(f)

    if randomOption == 1:
        randomWord = random.choice(data['animais'])
        print("Categoria: Animais")
        saveRandomCategory = "Animais"
    elif randomOption == 2:
        randomWord = random.choice(data['frutas'])
        print("Categoria: Frutas")
        saveRandomCategory = "Frutas"
    elif randomOption == 3:
        randomWord = random.choice(data['profissoes'])
        print("Categoria: Profissões")
        saveRandomCategory = "Profissões"
    elif randomOption == 4:
        randomWord = random.choice(data['distritos'])
        print("Categoria: Distritos")
        saveRandomCategory = "Distritos"
    else:
        randomWord = random.choice(words)
        print("Categoria: Random")
        saveRandomCategory = "Random"
    realWord = randomWord
    [word.append("_") for x in randomWord]


def showGame(erro=0):
    print("  _______     ")
    print(" |/      |    ")

    if erro == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif erro == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
    elif erro == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    elif erro == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    elif erro == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    elif erro == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    elif erro == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")

    [print(x + " ", end="") for x in word]


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

def validateCharacterInWord(character):
    global stateOfGame

    character = character.lower()
    realWordLower = realWord[0].lower() + realWord[1:]

    if character == realWordLower:
        print("\nParabêns completou o jogo, descobriu a palavra " + realWord)
        scoreGame()
        return False
    elif character in realWordLower:
        positionFind = []

        for j in range(len(realWord)):
            if realWordLower[j] == character:
                positionFind.append([j, realWord[j]])

        for [index, characterInIndex] in positionFind:
            word[index] = characterInIndex
    else:
        stateOfGame += 1

        if stateOfGame == 7:
            showGame(7)
            print("\n\nInfelizmente não completou o jogo, a palavra era " + realWord)
            return False
    if "_" not in word:
        showGame(stateOfGame)
        print("\n\nParabêns completou o jogo, descobriu a palavra " + realWord)
        scoreGame()
        return False
    return True

def playerNameCheck():
    global playerName

    while True:
        playerName = input("Nome do jogador: ")

        if playerName != "":
            break
        else:
            print("Precisa de inserir um nome!")

def runGame():
    global leaveInGame,  validateCharacterInWordBool, stateOfGame, word, realWord, saveRandomCategory, playerName

    if os.path.exists(fileName):
        if os.stat(fileName).st_size != 0:
            print('''
                1 - Continuar o jogo
                2 - Novo jogo
            ''')

            playerChoice = input("Qual opção deseja: ")

            if playerChoice == "1":
                with open(fileName, encoding='utf8') as json_file:
                    dataOfGameDict = json.load(json_file)

                word = dataOfGameDict['word']
                realWord = dataOfGameDict['realWord']
                stateOfGame = dataOfGameDict['stateOfGame']
                validateCharacterInWordBool = dataOfGameDict['validateCharacterInWordBool']
                validateCharacterInWordBool = dataOfGameDict['validateCharacterInWordBool']
                leaveInGame = dataOfGameDict['leaveInGame']
                saveRandomCategory = dataOfGameDict['saveRandomCategory']
                playerName = dataOfGameDict['playerName']
                print("Categoria:", saveRandomCategory)
            else:
                wordChoice()
        else:
            wordChoice()
    else:
        wordChoice()

    playerNameCheck()

    while leaveInGame:
        showGame(stateOfGame)

        while True:
            character = input("\n\nQual é a letra/palavra ou sair: ")

            if character.lower() == "sair":
                dataOfGameDict = {
                  "word": word,
                  "realWord": realWord,
                  "stateOfGame": stateOfGame,
                  "validateCharacterInWordBool": validateCharacterInWordBool,
                  "leaveInGame": leaveInGame,
                  "saveRandomCategory": saveRandomCategory,
                  "playerName": playerName
                }

                with open(fileName, 'w', encoding='utf8') as json_file:
                    json.dump(dataOfGameDict, json_file, sort_keys=True)

                print("\nSair, jogo guardado!")
                leaveInGame = False
                break
            elif re.match("^[a-z A-Z À-ÿ]*$", character):
                validateCharacterInWordBool = validateCharacterInWord(character)
                break
            else:
                print("Só é permitido letras", end="")
        if not validateCharacterInWordBool: break

    word = []
    realWord = ""
    stateOfGame = 0
    validateCharacterInWordBool = True
    leaveInGame = True
    saveRandomCategory = ""
    playerName = ""