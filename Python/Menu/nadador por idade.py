Y=1
while Y==1:

    l0 =("| Categorias |     Idade        |")
    l00=("|------------|------------------|")
    l1 =("| Infantil A | Até 6 anos       |")
    l2 =("| Infantil B | De 6 até 12 anos |")
    l3 =("| Juvenil  A | De 13 até 15 anos|")
    l4 =("| Juvenil  B | De 16 até 18 anos|")
    l5 =("| Adulto     | Maiores de 18    |")


    print(l0)
    print(l00)
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)

    i = int(input("Informe a idade do participante:"))

    if (i<=6):
            print ("Participante da categoria Infantil A")
    elif (i>=6) and (i<=12):
            print ("Participante da categoria Infantil B")
    elif (i>=13) and (i<=15):
            print ("Participante da categoria Juvenil A")
    elif (i>=16) and (i<=18):
            print ("Participante da categoria Juvenil B")
    elif (i>18):
            print ("Participante da categoria Adulto")

    input ("Voce deseja sair?")
    Y=2