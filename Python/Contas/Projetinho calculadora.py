from math import sqrt, pow  # importa o comando "sqrt" e " pow" da bliblioteca "math"
import os

y = 0
man = 0
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def menu(men):
    kkj = [1, 2, 3, 4, 5]
    os.system("cls")
    if men == 1:
        men = None
        cal()
    elif men == 2:
        men = None
        cient()
    elif men == 3:
        men = None
        menucdm()
        men = None
    elif men == 4:
        men = None
        menucv()
    elif men not in kkj and men == None:
        men = None
        print("Opcao invalida")


def op_1():
    print("Você selecionou Km/h para m/s")
    velocidade_kmh = float(input("Digite a velocidade em Km/h: "))  # inseri o valor para conversão
    velocidade_ms = (velocidade_kmh / 3.6)  # faz a conta para que a velocidade em Km/h sejá convertida em m/s
    print(f"{velocidade_kmh} Km/h equivale a {velocidade_ms:.2f} m/s")  # inprimi na tela o resultado
    os.system("pause")


def op_2():
    print("Você selecionou m/s para Km/h")
    velocidade_ms = float(input("Digite a velocidade em m/s: "))  # inseri o valor para conversão
    velocidade_Kmh = (velocidade_ms * 3.6)  # faz a conta para que a velocidade em m/s sejá convertida em Km/h
    print(f"{velocidade_ms} m/s equivale a {velocidade_Kmh:.2f} Km/h")  # inprimi na tela o resultado
    os.system("pause")


def menucv():
    os.system("cls")
    print(" [1] Conversão de Km/h para m/s \n [2] Conversão de m/s para Km/h \n [3] Voltar")
    nu = int(input("Digite a opção desejada:"))  # Selecionar a opção desejada para realizar

    if nu == 1:
        os.system("cls")
        op_1()  # está alocando o def da conversão de Km/h para m/s

    elif nu == 2:
        os.system("cls")
        op_2()  # está alocando o def da conversão de m/s para Km/h

    elif nu == 3:
        return menu # encerra e retorna para o menu principal

    else:
        print("Opção Invalida")
        os.system("pause")


def cient():
    men = 0
    y = []  # lista dos valores de porcentagem
    l = []  # lista de valores da potencia

    selec = int(input("Escolha a opção que deseja fazer! \n [1] - Raiz Quadrada \n [2] - Porcentagem \n [3] - Potência \n [4] - Voltar \n "))  # input de seleção de opção
    if selec == 1:
        print("Você escolheu Raiz Quadrada")
        x = int(input("Digite o valor que deseja encontrar a raiz: "))
        print(f"Sua raiz quadrada é {sqrt(x):.2f}")  # utiliza  função "sqrt"  que significa Square root of a number ou Raiz quadrada de um numero
        os.system("pause")
    elif selec == 2:
        print("Você escolheu a porcentagem")
        for i in range(2):
            v = int(input("Digite o valor que deseja encontrar a porcentagem: "))
            y.append(v)  # armazena os valores dentro da lista
        r = (y[0] / y[1]) * 100  # faz um calculo para achar a pocentagem dos 2 valores
        print(f" a porcentagem entre os valores {y} é de {r:.2f}% ")
        os.system("pause")

    elif selec == 3:
        print("Você escolheu a potência")
        for i in range(1, 3):
            p = int(input(f"Digite o {i} valor que deseja encontrar a potência: "))
            l.append(p)  # coloca os valores da potencia dentro da lista "l"
        print(pow(l[0], l[1]))  # utiliza da função "pow" que pode ser traduzido como "potenciação" para fazer o calculo
        os.system("pause")

    elif selec == 4:
        print("Você escolheu voltar")
        os.system("cls")
        menu(men)
    else:
        print("Opção invalida")
    return men


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Menu de seleção do conversor
def menucdm():
    print("Olá! selecione uma opção dentre as seguintes \n 1 - Conversão de Km \n 2 - Conversão de M \n 3 - Conversão de cm \n 4 - Conversor de milímetros \n 5 - Voltar")
    slc = int(input("Digite a opção que deseja: "))  # input de opção desejada
    if slc == 1:
        km()
        y = 0
        os.system("cls")
    elif slc == 2:
        metros()
        y = 0
        os.system("cls")
    elif slc == 3:
        centimetros()
        y = 0
        os.system("cls")
    elif slc == 4:
        milímetros()
        y = 0

    elif slc == 5:
        y = 1

    else:
        os.system("cls")
        print("Essa opção não existe")
        menucdm()
        os.system("pause")

    return y


# Menu de seleção do km
def km():
    os.system("cls")
    print("Você escolheu a opção Conversor de Km \n Escolha para qual medida você quer converter:\n 1 - Conversão de M \n 2 - Conversão de cm \n 3 - Conversor de milímetros \n 4 - Voltar")
    s2 = int(input("Digite a opção que deseja: "))  # input de opção desejada

    if s2 == 1:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 * 1000
        print(f"{x} metros")
        os.system("pause")
    elif s2 == 2:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 * 100000
        print(f"{x} centímetros")
        os.system("pause")
    elif s2 == 3:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 * 1000000
        print(f"{x} milímetros")
        os.system("pause")
    elif s2 == 4:
        os.system("cls")
        menucdm()

    else:
        print("essa opção não existe")
        os.system("pause")


# menu de seleção de metros
def metros():
    os.system("cls")
    print("Você escolheu a opção Conversor de M \n Escolha para qual medida você quer converter:\n 1 - Conversão de Km \n 2 - Conversão de cm \n 3 - Conversor de milímetros \n 4 - Voltar")
    s3 = int(input("Digite a opção que deseja: "))  # input de opção desejada

    if s3 == 1:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 / 1000
        print(f"{x} quilometros")
        os.system("pause")
    elif s3 == 2:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 * 100
        print(f"{x} centímetros")
        os.system("pause")
    elif s3 == 3:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 * 1000
        print(f"{x} milímetros")
        os.system("pause")
    elif s3 == 4:
        os.system("cls")
        menucdm()

    else:
        os.system("cls")
        print("essa opção não existe")
        os.system("pause")


# menu de seleção de centímetros


def centimetros():
    os.system("cls")
    print("Você escolheu a opção Conversor de M \n Escolha para qual medida você quer converter:\n 1 - Conversão de Km \n 2 - Conversão de M \n 3 - Conversor de milímetros \n 4 - Voltar")
    s4 = int(input("Digite a opção que deseja: "))  # input de opção desejada

    if s4 == 1:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 / 100000
        print(f"{x} quilometros")
        os.system("pause")
    elif s4 == 2:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 / 100
        print(f"{x} metros")
        os.system("pause")
    elif s4 == 3:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 * 10
        print(f"{x} milímetros")
        os.system("pause")
    elif s4 == 4:
        os.system("cls")
        menucdm()
    else:
        os.system("cls")
        print("essa opção não existe")
        os.system("pause")


# menu de seleção de milímetros
def milímetros():
    os.system("cls")
    print("Você escolheu a opção Conversor de M \n Escolha para qual medida você quer converter:\n 1 - Conversão de Km \n 2 - Conversão de M \n 3 - Conversor de cm \n 4 - Voltar")
    s5 = int(input("Digite a opção que deseja: "))  # input de opção desejada

    if s5 == 1:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 / 1000000
        print(f"{x} quilometros")
        os.system("pause")
    elif s5 == 2:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 / 1000
        print(f"{x} metros")
        os.system("pause")
    elif s5 == 3:
        os.system("cls")
        n1 = int(input("Digite qual número você deseja converter:"))
        x = n1 / 10
        print(f"{x} centímetros")
    elif s5 == 4:
        os.system("cls")
        menucdm()
    else:
        os.system("cls")
        print("essa opção não existe")
        os.system("pause")


def cal():
    men = 0
    val = []

    ops = [1, 2, 3, 4, 5]
   
    operacao = int(input("Escolha a opção que deseja fazer! \n[1] - Adição\n[2] - Subtração \n[3] - Divisão \n[4] - Multiplicação \n[5] - Voltar \n"))

    if operacao not in ops:
        print("Operação invalida")
    elif operacao == 5:
        menu(men)
    else:
        quant = int(input("Quantos numeros deseja utilizar na operação? "))
        if operacao == 1:
            for num in range(quant):
                num = float(input("Digite o numero: "))
                val.append(num)
            soma = 0
            for z in val:
                soma += z
            os.system("cls")
            print(f"O valor da sua soma é {soma}")
            os.system("pause")


        elif operacao == 2:
            for num in range(quant):
                num = float(input("Digite o numero: "))
                val.append(num)
            sub = val[0] * 2
            for z in val:
                sub -= z
            os.system("cls")
            print(f"O valor da sua subtração é {sub}")
            os.system("pause")

        elif operacao == 3:
            divi = [2]
            for num in range(1, quant + 1):
                num = float(input("Digite o numero: "))
                divi.append(num)
            div = divi[1] * 2
            divi[1] = 1
            for z in divi:
                div /= z
            os.system("cls")
            print(f"O valor da sua divisão é {div}")
            os.system("pause")

        elif operacao == 4:
            for num in range(quant):
                num = float(input("Digite o numero: "))
                val.append(num)
            mult = 1
            for z in val:
                mult *= z
            os.system("cls")
            print(f"O valor da sua multiplicação é {mult}")
            os.system("pause")


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

z = 1
while z == 1:
    os.system("cls")
    men = int(input("Digite a opção que deseja fazer! \n [1] - Calculadora Aritmética \n [2] - Calculadora Científica \n [3] - Conversor de Medidas \n [4] - Conversor de Velocidades \n [5] - Sair \n"))
    if men == 5:
        z = 0
    else:
        menu(men)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////