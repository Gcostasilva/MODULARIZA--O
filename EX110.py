#Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo()
#que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from modulos import moeda as md

valor = float(input('Digite um valor: R$ '))

print(md.resumo(valor, 1.2, 0.8))
