clientes = []

while True:
    pessoa = {}
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    pessoa["nome"] = nome
    pessoa["idade"] = idade
    
    animais = []
    while True:
        pet = input("Informe o nome do pet: ")
        animais.append(pet)

        r1 = input("Deseja cadastrar mais um pet? (s/n)")
        if r1.lower() == "n":
            break
    pessoa["animais"] = animais
    clientes.append(pessoa)
    r = input("Deseja cadastrar mais um cliente? (s/n)")
    if r.lower() == "n":
        break

print("Fim")