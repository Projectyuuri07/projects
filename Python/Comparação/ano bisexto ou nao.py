Y=1
while Y==1:
    n = int(input(f"Informe um ano a seguir:"))

    if (n%4) == 0:
        print (f"{n} é um ano bissexto")
    else:
        print (f"{n} não é um ano bissexto")
    
    input ("Voce deseja sair?")
    Y=2