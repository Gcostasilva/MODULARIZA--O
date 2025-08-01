#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests 

url = 'https://google.com'

try:
    teste = requests.get(url)
except Exception:
    print(f'O site {url} não está acessível no momento.')
else:
    print(f'O site {url} está acessível no momento.')
