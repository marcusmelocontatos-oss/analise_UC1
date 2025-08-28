"""Uma escola solicita um programa que calcule e informe a méda e a situação dos alunos.
Para isso o programa deverá solicitar que o usuário informe as 4 notas.
Se a média for maior ou igual a 7, deverá informar que o aluno está aprovado, senão deverá pedir a nota de recuperação.
O programa fará um novo cálculo entre a média e a nota de recuperação, caso, essa nova média seja inferior a 5, o progrma informará que o aluno está reprovado, senão, aprovado"""

nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
nota3 = float(input('Informe sua terceira nota: '))
nota4 = float(input('Informe sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) /4

print(f"A média é {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media < 7:
    print("Recuperação")

    recuperacao = float(input('Informe sua nota de recuperação: '))
    nota5 = (media + recuperacao) /2

    print(f'{nota5}')
    if nota5 < 5:
        print("Reprovado")
    elif nota5 > 5:
        print("Aprovado")