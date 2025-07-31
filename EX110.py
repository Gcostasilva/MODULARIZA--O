#Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo()
#que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from modulos import moeda as md

valor = input('Digite um valor: R$ ')
n_valor = md.corrige(valor)
print(md.resumo(n_valor, 35, 22))
