"""Crie um programa que fará a leitura de indeterminados números
que serão armazenados em uma lista, deverá ser digitado o número 0 (zero)
para interromper a leitura

No final, o programa deverá informar o número de total de elementos da lista,
a soma dos números pares e a média dos números impares."""

"""soma = 0
while True:
    n = int(input("Informe o número: "))
    soma = soma + n
    r = input("Caso não deseje continuar digite 0: ")
    if r == "0":
        break
print(f"A soma é {soma}")
#lista = lista + n
lista =[]
lista = lista + soma
print(lista)
print(type(lista))
print(f"O número total de elementos da lista é: {len(lista)}")


#frutas = ["Pêra", "Uva", "Morango"]
#frutas = frutas + ["Abacaxi", "Ovo"]"""
#correção
numeros = []
while True:
    n = int(input("Informe o número: "))
    
    numeros.append(n)
    if n == 0:
        break

print(f"Total de elementos é : {len(numeros)}")
somaPares = 0
somaImpares = 0
quantImpares = 0
for i in numeros:
    if i % 2 == 1:
        print("Ímpar")
        somaImpares = somaImpares + i
        quantImpares = quantImpares + 1
    elif i % 2 == 0:
        print("Par")
        somaPares = somaPares + i

print(f"A soma dos números pares é: {somaPares}")
mediaImpares = somaImpares / quantImpares
print(f"A média dos ímpares é: {mediaImpares}")