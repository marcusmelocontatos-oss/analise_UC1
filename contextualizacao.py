nome = "Luis"
print(nome)
print(type(nome))
print(nome.lower()) #Imprime em minúscula sem alterar o conteúdo
print(nome.upper()) #Imprime em maiúscula sem alterar o conteúdo
nome2 = "Renato"
print(nome2)
print(type(nome2))

#Lista
contatos = []
#contatos[1] = "Ricardo" não pode ser
#utilizado quando for primeiro cadastro
contatos.append ("Ricardo")
contatos.append ("Luis")
contatos.append ("Renato")
print(contatos)
print(type(contatos))

frutas = ["Pêra", "Uva", "Morango"]
frutas = frutas + ["Abacaxi", "Ovo"]
print(frutas)
print(type(frutas))

frutas[4] = "Kiwi"
print(frutas)
print(f"Quantidade de letras de {nome} é {len(nome)}")
print(f"Tamanho da lista de frutas é {len(frutas)}")

for f in frutas:
    print(f)

frutas.pop(2) #Utilizado para eliminar elementos por posição exemplo a uva nº2
print(frutas)
frutas.remove("Uva") #Utilizado para eliminar elementos por nome do objeto exemplo uva
print(frutas)

#frutas.pop(20)
#frutas.remove("Ovo")

#Ordenar
frutas.sort() #ordem crescente
print(frutas)
frutas.reverse() #ordem decrescente
print(frutas)