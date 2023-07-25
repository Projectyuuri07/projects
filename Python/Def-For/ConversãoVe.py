import os

def op_1():
    print("Você selecionou Km/h para m/s")
    velocidade_kmh = float(input("Digite a velocidade em Km/h: ")) #inseri o valor para conversão
    velocidade_ms = velocidade_kmh / 3.6 #faz a conta para que a velocidade em km/h sejá convertida em m/s
    print(f"{velocidade_kmh} Km/h equivale a {velocidade_ms:.2f} m/s") #inprimi na tela o resultado
    os.system("pause")

def op_2():
    print("Você selecionou m/s para Km/h")
    velocidade_ms = float(input("Digite a velocidade em m/s: ")) #inseri o valor para conversão
    velocidade_Kmh = velocidade_ms * 3.6 #faz a conta para que a velocidade em m/s sejá convertida em km/h
    print(f"{velocidade_ms} m/s equivale a {velocidade_Kmh:.2f} Km/h") #inprimi na tela o resultado
    os.system("pause")

w = 0
while w == 0:
    os.system("cls")
    print(" [1] Conversão de Km/h para m/s \n [2] Conversão de m/s para Km/h \n [3] Voltar")
    nu = int(input("Digite a opção desejada:")) #Selecionar a opção desejada para realizar

    if nu == 1:
        os.system("cls")
        op_1() #está alocando o def da conversão de km/h para m/s

    elif nu == 2:
        os.system("cls")
        op_2() #está alocando o def da conversão de m/s para km/h
        
    elif nu == 3:
        w = 1 #encerra o while e retorna para o menu principal

    else:
        print("Opção Invalida")
        os.system("pause")