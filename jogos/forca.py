import random



def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicialize_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    erros = 0

    while not enforcou:# Também não foi necessário aqui and not acertou:
        chute = pede_chute()

        if(chute in palavra_secreta):
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

            if(erros < len(palavra_secreta)):
                print('Você errou! Lhe restam {} tentativas'.format(len(palavra_secreta) - erros))

        print('')
        print(letras_acertadas)

        if(erros == len(palavra_secreta) or '_' not in letras_acertadas):
            break

    fim_do_jogo(letras_acertadas, palavra_secreta, erros)

    print("\nFim do Jogo")

def imprime_mensagem_abertura():
    print(33*"*")
    print("Bem vindo ao jogo de Forca!")
    print(33*"*")

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicialize_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    chute = input("\nQual letra? ")
    chute = chute.strip().upper()
    return chute

def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1

def fim_do_jogo(letras_acertadas, palavra_secreta, erros):
    if ('_' not in letras_acertadas):
        print('Você ganhou!\nParabéns...')
    elif (erros == len(palavra_secreta)):
        print('Você perdeu!\n\nA palavra era {}'.format(palavra_secreta.upper()))

if(__name__ == "__main__"):
    jogar()