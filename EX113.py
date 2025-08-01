#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from modulos import moeda as md

inteiro = md.leiaInt(input('Digite um número inteiro: '))
print(f'Você digitou o número inteiro: {inteiro}')

real = md.leiaReal(input('Digite um número real: '))
print(f'Você digitou o número real: {real}')