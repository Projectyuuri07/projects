import os

class Menu:
    def show_menu(self):
        print("1. Área de um circulo 1")
        print("2. Circunferencia de um circulo 2")
        print("3. Transformar o circulo em um cilindro 3")
        print("4. calcular o volume de um cilindro 4")
        print("5. Calcule o volume de uma piramide 5")
        print("6. Calcule o perimetro de uma piramide 6")
        print("7. Calcule a area da base de uma piramide 7")
        print("8. Sair do programa!")

    def get_option(self):
        option = int(input("Digite a opção desejada: "))
        return option