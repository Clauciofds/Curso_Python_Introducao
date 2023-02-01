# Exemplos de URLs válidas:#
# bytebank.com/cambio
# bytebank.com.br/cambio
# www.bytebank.com/cambio
# www.bytebank.com.br/cambio
# http://www.bytebank.com/cambio
# http://www.bytebank.com.br/cambio
# https://www.bytebank.com/cambio
# https://www.bytebank.com.br/cambio

# Exemplos de URLs inválidas:#
# https://bytebank/cambio
# https://bytebank.naoexiste/cambio
# ht://bytebank.naoexiste/cambio

# htpps://www.bytebank.com.br/cambio

import re

url = 'htpps://www.bytebank.com.br/cambio'
padrao_url = re.compile('(htpp(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError('A URL NÃO é válida')

print('A URL é vãlida.')
