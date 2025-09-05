"""Faça um programa que executará a conversão de temperatuas Celsius
para Fahrenheit começando em 10 graus Celcius até 60 graus Celsius, saltando de 5 em 5 graus.
A fórmula da conversão é F = 9C / 5 + 32"""

C = 10
F = 9*C / 5 + 32

for celsius in range (10,61, 5):
    f = ((9 * celsius) / 5) + 32
    print(f"{celsius}ºc = {f}ºf")

#pass (pode ser utilizado para implementar depois dentro do for)