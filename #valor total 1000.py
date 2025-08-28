#valor total 1000
#numero de parcelas 5
 
#numero1 = int(input ('Informe valor gasto'))
#numero2 = int(input ('Informe o valor de parcelas'))

#divisao = numero1 / numero2

#print(f'{numero1} / {numero2} = {divisao}')

total = float(input ('Informe o valor total:'))
parcelas = int(input('Informe o valor de parcelas:'))
prestacao = total/ parcelas
#prestacao = float(input('Informe o valor da prestação:'))

print(f'O valor da prestação é {prestacao:.2f}')
#:.2f delimitando a quantidade de casa decimal (no caso em duas)