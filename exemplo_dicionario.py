dono1 = {"nome" : "Renato", "idade" : 20}
print(dono1["nome"])
print(dono1["idade"])

dono1["nome"] = "Luis Renato"
print(dono1["nome"])
print(dono1["idade"])

dono1["celular"] = "3932-2020"
print(dono1["nome"])
print(dono1["idade"])
print(dono1["celular"])

dono1["animais"] = ["Lucky"]
print(dono1["nome"])
print(dono1["idade"])
print(dono1["celular"])
print(dono1["animais"])

dono2 = {"nome" : "Paula", "idade" : 15}
dono3 = {"nome" : "Adilson", "idade" : 50, "animais": ["Joca", "Mingau"]}

contatos = [] #também poderia ser feito contatos = [dono1, dono2, dono3]
contatos.append(dono1)
contatos.append(dono2)
contatos.append(dono3)

for i in contatos:
    print(f'{i["nome"]} - {i["idade"]}')
    try:
        for j in i["animais"]:
            print(j)
    except:
        print("Não possui animais")