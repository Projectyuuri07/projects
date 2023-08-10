from classe import*

def main():
    menu = Menu()

    menu.show_menu()

    option = menu.get_option()

    if option == 1:
        os.system("cls")
        print("Área de um circulo")

    elif option == 2:
        os.system("cls")
        print("Circunferencia de um circulo")

    elif option == 3:
        os.system("cls")
        print("Transformar o circulo em um cilindro")

    elif option == 4:
        os.system("cls")
        print("calcular o volume de um cilindro")

    elif option == 5:
        os.system("cls")
        print("Calcule o volume de uma piramide")

    elif option == 6:
        os.system("cls")
        print("Calcule o perimetro de uma piramide")

    elif option == 7:
        os.system("cls")
        print("Calcule a area da base de uma piramide")
        
    elif option == 8:
        os.system("cls")
        print("Sair do programa!")
    else:
        print("Opção inválida")