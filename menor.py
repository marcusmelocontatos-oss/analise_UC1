# Fazer um programa que fará a leitura da idade de uma pessoa e o programa informará se a pessoa é menor de idade

idade = int(input('Informe a idade: '))
'''operadores relacionais
<
<=
>
>=
= (atribuição, uma variável recebendo um valor)
== (comparação)
!= (diferente)'''

#para fazer um bloco de comandos começamos com : 
if idade < 18:
    print("Menor de idade.")
    print('estou no if')
else:
    print('MAIOR DE IDADE.')
    
print('Fim do programa')
