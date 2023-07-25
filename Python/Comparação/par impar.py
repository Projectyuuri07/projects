while True:
    n = int(input(f"Informe um valor a seguir:"))

    if (n%2) == 0:
        print (f"{n} é um número par")
    else:
        print (f"{n} é um número impar")
    
    opcao = input("Deseja sair do programa? (Y/N)").lower()
    if opcao == "y":
        break

 