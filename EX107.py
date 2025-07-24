#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from modulos import moeda as md

valor = float(input('Digite um valor: R$ '))

print(f'Aumentando 10%: {md.aumentar(valor, 1.1):.2f}')
print(f'Diminuindo 10%: {md.diminuir(valor, 0.9)}')
print(f'Dobro: {md.dobro(valor)}')
print(f'Metade: {md.metade(valor)}')