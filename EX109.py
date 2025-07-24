#Exercício Python 109: Adapte o código do desafio #108, criando uma um parametro adicional chamado formato que,
# caso seja passado como True, formate os valores monetários com o símbolo de moeda.

from modulos import moeda as md

valor = float(input('Digite um valor: R$ '))

print(f'Aumentando 10%: {md.aumentar(valor, 1.1)}')
print(f'Diminuindo 10%: {md.diminuir(valor, 0.9)}')
print(f'Dobro: {md.dobro(valor)}')
print(f'Metade: {md.metade(valor, False)}')