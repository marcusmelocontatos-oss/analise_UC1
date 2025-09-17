contatos = []
nome = "Luis"
nome = "Claudio"
print(nome)

contatos.append(nome)
contatos.append("Feliciano")
#append sempre adiciona ao final da lista
contatos.insert(0, "Paula")
#insert adiciona na posição indicada e desloca os demais
print(contatos)
contatos.insert(99, "André")
print(contatos)
print(contatos[1])
contatos[3] = "Fernanda"
#pode utilizar para alteração nunca para inserir
for i in contatos:
    print(i)
#é possóvel inserir qualquer coisa 
contatos.append(20)
contatos.append(4.5)
print(contatos)

contatos.append(["Renato", 20])
print(contatos)