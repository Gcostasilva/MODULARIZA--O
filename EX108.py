#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from modulos import moeda as md

valor = float(input('Digite um valor: R$ '))

print(f'Aumentando 10%: {md.formatar(md.aumentar(valor, 1.1))}')
print(f'Diminuindo 10%: {md.formatar(md.diminuir(valor, 0.9))}')
print(f'Dobro: {md.formatar(md.dobro(valor))}')
print(f'Metade: {md.formatar(md.metade(valor))}')