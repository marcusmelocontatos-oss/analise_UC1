categoria = int(input("Informe a categoria: "))

match categoria:
    case 1:
        print("Alimentos")
    case 2:
        print("Bebidas")
    case 3 | 4:
        print("Cosméticos")
    case 5 | 6:
        print("Produtos de Limpeza")
    case _:
        print("Categoria não encontrada")