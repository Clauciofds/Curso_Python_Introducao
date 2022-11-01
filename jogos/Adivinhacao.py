import random

def jogar():

    print(33*"*")
    print("Bem vindo ao jogo de adivinhação!")
    print(33*"*")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("\nQual o nível de dificuldade?")
    nivel = int(input("(1) Fácil - (2) Médio - (3) Difícil \nDigite sua Opção: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for Rodada in range(1, total_de_tentativas + 1):
        print("Rodada {}/{}". format(Rodada, total_de_tentativas))
        chute_str = int(input("Digite um número entre 1 - 100: "))
        print("Você digitou: ", chute_str)

        print("0% {} {}%". format((round((Rodada/total_de_tentativas)*20))*"|", (round((Rodada/total_de_tentativas)*100))),"\n")

        acertou = (chute_str == numero_secreto)
        maior   = (chute_str > numero_secreto)
        menor   = (chute_str < numero_secreto)

        if(chute_str < 1 or chute_str > 100):
            print("Você deve digitar um númerio entre 1 e 100")
            continue
        elif(acertou):
            print("Parabéns. Você fez {} pontos". format(pontos))
            print("Voce acertou!")
            break
        elif(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.","\n")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.","\n")

        pontos = pontos - (abs(numero_secreto - chute_str))

    print("Fim do jogo.")

if(__name__== "__main__"):
    jogar()