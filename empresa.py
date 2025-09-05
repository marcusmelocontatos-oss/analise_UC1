"""Uma empresa almeja um programa que fará a leiura de 5 produtos e no final irá exibir apenas
o somatório dos produtos que custam acima de 200 reais."""

soma = 0
for i in range(5):
    preco = float(input("Informe o preço: "))
    if preco >= 200:
        soma = soma + preco

print(f"A soma dos produto acima de R$ 200.0 reais é R$ {soma} reais")