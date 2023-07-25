
val1 = -1
val2 = 0
val3 = 0
mediana = 0

num1 = 0
num2 = 0
num3 = 0
z = 1
#while para verificar se o usuario quer ou não sair do programa
while z == 1:

    dec = 0
    primo = 0
    decw = 0
    med = 0

    selec = int(input("Menu \n 1 - Numeros Primos \n 2 - Numeros Decrescentes \n 3 - Mediana de 3 numeros \n 4 - Sair \n "))

    while primo == 0:
        if selec == 1:
            print("Numeros Primos")
            p = int(input(" 1 - Lógica \n 2 - Refazer \n 3 - Voltar \n "))
            if p == 1:
                val1 = int(input("Digite seu numero: "))
            if val1 % val1 == 0 and val1 % 1 == 0:
                print("Seu numero é primo")
            else:
                print("Seu numero não é primo")
        elif p == 2:
            if val1 == -1:
                print("Erro! Você precisa ter efetuado a lógica primeiro")
            else: 
                if val1 == 1:
                    print("Seu numero é primo")
                else:
                    print("Seu numero não é primo")

            if p == 3:
                primo = 1
                p = 0
                val1 = -1

    while decw == 0:
        if selec == 2:
            print("Numero decrescente!")
            dec = int(input(" 1 - logica \n 2 - refazer \n 3 - voltar \n 4 - sair \n "))
            if dec == 1:
                val1= int(input("Digite o numero que você quer ver a regressiva: "))
                while val1 !=0:
                        val3 = val1 
                        val1 = val1 -1
                        print(val1)

            elif dec == 2:
                    if val1 == -1:
                        print("Erro! Você precisa ter efetuado a lógica primeiro \n")
                    else:
                        while val3 !=0:
                            val3 = val3 -1
                            print(val3)

                    if dec == 3:
                            primo = 1
                            decw = 1
                            dec = 0
                            val1 = -1

                    if dec == 4:
                         primo = 1
                         decw = 1
                         dec = 1
                         val1 = -1
                         z = 0
                         

    while med == 0:
            if selec == 3:
                print("Você escolheu Mediana")
                med = int(input(" 1 - logica \n 2 - refazer \n 3 - voltar \n"))
                if med == 1:
                        num1 = float(input("Digite o primeiro número: "))
                        num2 = float(input("Digite o segundo número: "))
                        num3 = float(input("Digite o terceiro número: "))

                        if num1 > num2:
                            if num2 > num3:
                                mediana = num2
                            elif num1 > num3:
                                mediana = num3
                            else:
                                mediana = num1
                        else:
                            if num2 < num3:
                                mediana = num2
                            elif num1 < num3:
                                mediana = num3
                            else:
                                mediana = num1


                        print("A mediana é:", mediana)
                elif med == 2:
                    if mediana == 0:
                          print("Erro! Você precisa ter efetuado a lógica primeiro")
                    else:
                        print("A mediana é:", mediana)
    while z == 1:            
        if med == 3:     
            mediana = 0
            med = 0 
            primo = 1
            decw = 1