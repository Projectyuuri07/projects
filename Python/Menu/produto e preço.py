Y=1
while Y==1:

    linha    = ("Produto | Preço ")
    linha1    =("   1    |   10  ")
    linha2    =("   2    |   20  ")
    linha3    =("   3    |   30  ")
    linha4    =("   4    |   40  ")
    linha5    =("   5    |   50  ")

    print(linha)
    print(linha1)
    print(linha2)
    print(linha3)
    print(linha4)
    print(linha5)

    pedido= int(input("Escolha um produto do 1 ao 5 : "))

    if (pedido == 1):
        print ("O valor do produto e R$10,00")
    elif (pedido == 2):
        print ("O valor do produto e R$20,00")
    elif (pedido == 3):
        print ("O valor do produto e R$30,00")
    elif (pedido == 4):
        print ("O valor do produto e R$40,00")
    elif (pedido == 5):
        print ("O valor do produto e R$50,00")

    input ("Voce deseja sair?")
    Y=2