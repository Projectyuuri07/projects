Y=1
while Y==1:

    a = int(input(f"Informe o lado A do triangulo:"))
    b = int(input(f"Informe o lado B do triangulo:"))
    c = int(input(f"Informe o lado C do triangulo:"))

    if (a==b) and (a==c) and (c==b):
        print ("É um triangulo Equilatero")
    elif (a==b) or (a==c) or (b==c):
        print ("É um triangulo Isósceles") 
    else:
        print ("E um triangulo Escaleno")

    input ("Voce deseja sair?")
    Y=2