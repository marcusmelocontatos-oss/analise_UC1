#Ler indeterminados números interiros e informar a soma. A condição de parada é o usuário responder 'n' a pergunta se ele deseja continuar.
soma = 0
while True:
    n = int(input("Informe o número: "))
    soma = soma + n
    r = input("Deseja continuar? (s/n) ")
    if r == "n" or r == "N":
        break
    
print(f"A soma é {soma}")