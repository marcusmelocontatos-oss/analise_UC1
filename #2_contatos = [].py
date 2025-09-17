#Exempplo de matriz
contatos = []
contatos.append(["Renato", 20])
contatos.append(["Paula", 15])
contatos.append(["Adilson", 50, ["Joca", "Mingau"]])
print(contatos)

for i in contatos:
    #print(i)
    for j in i:
        print(j)
        #for k in j:
            #print(k)

print(contatos[1][0])
print(contatos[2][2][0])
print(contatos[2][2][1])