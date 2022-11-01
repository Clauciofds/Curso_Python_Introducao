print("Bem vindo ao jogo de adivinhação!")

numero_secreto = 42
tentativas = 3

for rodada in range(1, tentativas + 1):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute_str = input("Digite um número entre 1 - 100: ")
    chute = int(chute_str)

    while (chute <= 0 or chute > 100):
        print("Chute inválido, você deve chutar um número entre 1 - 100. Tente novamente:")
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 - 100: ")
        chute = int(chute_str)

    if(chute == numero_secreto):
        print("Você acertou!")
        break
    else:
        if(chute > numero_secreto):
            print("O seu chute é maior que o número secreto.")
        else:
            print("O seu chute é menor que o número secreto.")

print("Fim do jogo")