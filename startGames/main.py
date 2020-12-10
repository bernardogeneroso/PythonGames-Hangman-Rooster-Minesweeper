import startGames.jogoGalo as runGameGalo
import startGames.jogoCampoMinas as runGameCampoMinas
import startGames.jogoForca as runGameForca
import startGames.scores as runScores

def choiceGame():
    stay = True

    while stay:
        print('''
        1 - Jogo do Galo
        2 - Jogo de Campo de Minas
        3 - Jogo da Forca
        4 - Pontuações
        5 - Sair
        ''')

        while True:
            try:
                playerChoice = int(input("Qual opção que deseja: "))
                
                if playerChoice == 1:
                    runGameGalo.runGame()
                elif playerChoice == 2:
                    runGameCampoMinas.runGame()
                elif playerChoice == 3:
                    runGameForca.runGame()
                elif playerChoice == 4:
                    runScores.scoreRun()
                elif playerChoice == 5:
                    print("\nAdeus e volte sempre!")
                    stay = False
                break
            except ValueError:
                print("Insira valor númerico")


if __name__ == "__main__":
    choiceGame()
