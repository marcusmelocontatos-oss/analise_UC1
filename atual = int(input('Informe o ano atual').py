atual = int(input('Informe o ano atual '))
nascimento = int(input ('Informe o ano de nascimento '))
subtracao = atual - nascimento

print(f' Idade em anos {atual} - {nascimento} = {subtracao}')

idade = int(input('Informe a idade em meses '))
meses = int(input('Informe número de meses ao ano '))
multiplicacao = idade * meses

print(f' Idade em meses {idade} * {meses} = {multiplicacao}')

idade = int(input('Informe a idade em meses '))
dias = int(input('Informe número de dias ao ano '))
multiplicacao = idade * dias

print(f' Idade em meses {idade} * {dias} = {multiplicacao}')

#forma correta de calcular (ao invés de inserir muitos dados)

"""anoatual = 2025 ou anoatual = datetime.datetime.now().year
cmd import datetime (na primeira linha para que fique organizado)
idadeAnos = anoatual - anonasc
idadeMeses = idadeAnos *12 
idadeDias = idadeAnos * 360"""

"""print(f'''Você tem {idadeAnos} anos
Ou {idadeMeses} meses
Ou {idadeDias} dias''')
"""
#\n ou 3 áspas