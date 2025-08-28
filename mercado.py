"""Uma empresa precisa que quando o usuário digitar o número 1,
o programa imprimirá a palavra "Alimentos".
Se o usuário digitar o número 2, imprimirá a palavra "Bebidas"
Se o usuário digitar o número 3 ou 4, imprimirá a palavra "Cosméticos"
Se usuário digitar o número 5 ou 6, imprimirá a palavra "Produtos de Limpeza"

Qualquer outro, o programa imprimirá "Categoria não encontrada"""

n = int(input("Informe um número: "))
if n == 1:
    print("Alimentos")
elif n == 2:
    print("Bebidas")
elif n == 3 or n == 4:
    print("Cosméticos")
elif n == 5 or n == 6:
    print("Produtos de Limpeza")
else:
    print("Categoria não encontrada")