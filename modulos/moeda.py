# MOEDA.PY
# Módulo para manipulação de valores monetários

def aumentar(vlr = 0 , percentual = 1.1, formato = True):
    '''Aumenta o valor de acordo com o percentual informado.'''
    if formato == True:
        return formatar(vlr * ((percentual+100)/100))
    else:
        return vlr * percentual
    
def diminuir(vlr = 0 , percentual = 0.1, formato = True):
    '''Diminui o valor de acordo com o percentual informado.'''
    if formato == True:
        return formatar(vlr * (1-((percentual/100))))
    else:
        return vlr * percentual
    
def dobro(vlr = 0, formato = True):
    '''Retorna o dobro do valor informado.'''
    if formato == True:
        return formatar(vlr * 2)
    else:
        return vlr * 2
    
def metade(vlr = 0, formato = True):
    '''Retorna a metade do valor informado.'''
    if formato == True:
        return formatar(vlr / 2)
    else:
        return vlr / 2

def formatar(vlr = 0):
    '''Formata o valor monetário para o padrão brasileiro.'''
    return f'R$ {vlr:.2f}'.replace('.', ',')

def corrige(vlr):
    '''ACEITA APENAS NUMEROS, INTEIROS E DECIMAIS.'''
    if ',' in vlr:
        vlr = vlr.replace(',', '.')

    if vlr.replace('.', '').isdigit():
        return float(vlr)
    else:
        while not vlr.replace('.', '').isdigit():
            vlr = input('Valor inválido. Digite novamente: R$ ')
            vlr = vlr.replace(',', '.')
            
        return float(str(vlr))
def leiaInt(n):
    while n.isnumeric() == False:
        n = input('Digite um número inteiro: ')
    
    return int(n)

def leiaReal(n):
    try:
        n = float(n)
    except Exception:
        while True:
            try:
                n = input('Valor inválido. Digite novamente: ')
            except Exception:
                pass
            else:
                break
    return corrige(n) 



#Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo()
#que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
#incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def resumo(vlr = 0 , aumento = 1.1, reducao = 0.9):
    '''Mostra um resumo do valor com aumento e redução.'''
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado: ":<20}{formatar(vlr):>8}')
    print(f'{"Dobro do preço: ":<20}{dobro(vlr):>8}')
    print(f'{"Metade do preço: ":<20}{metade(vlr):>8}')
    print(f'{"Aumento de "}{aumento*100 - 100:.0f}{"%":<6}{aumentar(vlr, aumento):>8}')
    print(f'{"Redução de "}{reducao*100 - 100:.0f}{"%":<6}{diminuir(vlr, reducao):>8}')
    print('-' * 30)
