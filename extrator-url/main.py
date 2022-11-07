url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
#print(url)
#url=' '

# SANITIZAÇÃO DA URL
url=url.strip()

# Validação da URL
if url=='':
    raise ValueError('A URL está vazia')

#SEPARA BASE E OS PARÂMETROS
indice_interrogacao=url.find('?')
url_base=url[:indice_interrogacao]
#print(url_base)

url_parametros=url[indice_interrogacao+1:]
print(url_parametros)

#BUSCA O VALOR DO PARÂMETRO DE BUSCA
paremetro_busca='quantidade'
indice_paremetro=url_parametros.find(paremetro_busca)
#print(indice_paremetro)
indice_valor=indice_paremetro+len(paremetro_busca)+1
indice_e_comercial=url_parametros.find('&',indice_valor)
if indice_e_comercial==-1:
    valor=url_parametros[indice_valor:]
else:
    valor=url_parametros[indice_valor:indice_e_comercial]
print(valor)