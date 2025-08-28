altura = float(input('Informe a altura em metros: '))
sexo = input("Informe o sexo: ")
peso = 0.0
if sexo == 'M' or sexo == "m":
    peso = (72.7 * altura) - 58
elif sexo == 'F' or sexo == "f":
    peso = (62.1 * altura) - 44.7
else:
    print('Informação inválida')
print(f'O peso ideal é: {peso:.3f}')