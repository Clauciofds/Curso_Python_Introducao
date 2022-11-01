numero_secreto = 42

chute_str = int(input("Digite o seu numero: "))
print("Voce digitou ", chute_str)

acertou = (chute_str == numero_secreto)
maior   = (chute_str > numero_secreto)
menor   = (chute_str < numero_secreto)

print(type(acertou))
