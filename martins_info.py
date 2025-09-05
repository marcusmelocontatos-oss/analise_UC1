"""A martins informática comercializa os seguintes produtos

Código      Nome                Preço
10          Pendrive 64GB       40,00
11          PowerBank 30000     130,00
12          Headse              80,00
13          Mouse               15,00
14          Teclado             20,00

Faça um programa que fará a leitura do código e a quantidade, a cada
interação, o programa deverá perguntar se o usuário deseja continuar
cadastrando itens. Caso a resposta for 'n',
o programa exibirá a soma e encerrará."""

"""soma = 0
while True:
    codigo = float(input("Informe o código do produto: "))
    quantidade = float(input("Informe a quantidade de produto(s): "))
    
    match codigo:
        case 10:
            print(f"Pendrive 64GB {quantidade * 40} reais")
        case 11:
            print(f"PowerBank 30000 {quantidade * 130} reais")
        case 12:
            print(f"Headse {quantidade * 80} reais")
        case 13:
            print(f"Mouse {quantidade * 15} reais")
        case 14:
            print(f"Teclado {quantidade * 20} reais")
    r = input("Deseja continuar? (s/n) ")
    if r == "n" or r == "N":
        break
    
print(f"A soma é {soma}")"""

#correção

soma= 0

while True:

    codigo = int(input("Informe o código: "))
    quantidade = int(input("Quantidade: "))

    match (codigo):
        case 10:
            soma = soma + (40 * quantidade)
        case 11:
            soma = soma + (130 * quantidade)
        case 12:
            soma = soma + (80 * quantidade)
        case 13:
            soma = soma + (15 * quantidade)
        case 14:
            soma = soma + (20 * quantidade)
        case _:
            print("Código inválido")

    r = input("Deseja continuar? (s/n) ")
    if r == "n" or r == "N":
        break

print(f"O total é {soma:.2f}")