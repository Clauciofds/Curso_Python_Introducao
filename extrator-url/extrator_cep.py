endereco= 'Rua Cavalo n!água, 1010, casa, Jardim Tropéiro, Mogi da Cruzaes, SP, 12345-321'

import re #Regular Expression -- RegEx

#Padrão da extrutura do CEP brasileiro

padrao=re.compile('[0-9]{5}[-," "]{0,1}[0-9]{3}')
busca=padrao.search(endereco) #Mach
if busca:
    cep=busca.group()
    print(cep)