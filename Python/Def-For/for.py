import os
while True:

    print("Menu")
    print(" 1- Lista de 10 numeros")
    print(" 2- Lista de 5 nomes")
    print(" 3- Lista de 3 frutas")
    print(" 4- Chamada da Classe")
    es = int(input("Escolha a lista:  "))

    if es == 1:
        num = [0,1,2,3,4,5,6,7,8,9,10]
        print("")
        print("-------| Números de 1 a 10 |-------")
        print("")

        for N in num:
            print (N)

    elif es == 2:
        nom = ["Yuri","Carlos","Ruan","Thiago","Diego"]
        print("")
        print("------------| 5 Nomes |-----------")
        print("")

        for o in nom:
            
            print (o)
            nom[2]="Carol"

    elif es == 3:
        fru = ["Maça","Pera","Uva"]
        print("")
        print("-----------| 3 Frutas |-----------")
        print("")

        for u in fru:   
            print (u)

    elif es ==4:
        cha = [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
        print("")
        print("-| Números da chamada de 1 a 34 |-")
        print("")

        for c in cha:
            print (c)

    else:
        print("Opção Invalida")

    opcao = input("Deseja escolher outra lista (Y/N)").lower()
    if opcao =="y":
        os.system("cls")
    elif opcao != "y":

        opcao = input("Deseja sair do programa? (Y/N)").lower()
        if opcao == "y":
            break
        os.system("cls")

print("")
os.system("pause")