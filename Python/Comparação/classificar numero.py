while True:
    n= float(input(f"Informe um valor a seguir:"))

    if (n>0):
        print (f"{n} é um número positivo")
    elif (n==0):
        print (f"{n} é igual a zero")
    else:
        print (f"{n} é um número negativo")
    
    opcao = input("Deseja sair do programa? (Y/N)").lower()
    if opcao == "y":
        break

