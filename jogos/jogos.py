import forca
import Adivinhacao

def escolher_jogo():
    "\n"
    print(33*"*")
    print("Escolha seu Jogo")
    print(33*"*")

    print("(1) Forca ou (2)Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando Forca\n")
        forca.jogar()

    elif(jogo == 2):
        print("Jogando Adivinhação\n")
        Adivinhacao.jogar()

    print("\nEscolha outro Jogo")

if(__name__ == "__main__"):
    escolher_jogo()