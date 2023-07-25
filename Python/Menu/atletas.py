import os

#Variaveis Usadas e a Biblioteca

w = "N"
atletas = {}

#Menu Inicial

while w != "S":
    os.system("cls")
    print("Menu Inicial")
    print(" [1] - Registro")
    print(" [2] - Alterar")
    print(" [3] - Listar")
    print(" [4] - Sair")    
    s = int(input("Digite a opção desejada: "))

    if s == 1: 
#opção de registro
        y = 1
        os.system("cls")
        nome = input("Digite o nome do competidor: ")
        t = int(input("Digite quantos saltos o competidor deu: "))
        val = []
        for num in range(t):
            num = float(input(f"Digite a distância do {num+1}º salto: "))
            val.append(num)
        atletas[nome] = val 
#salva uma lista com os saltos dentro do nome do usuario
        os.system("cls")

    elif s == 2:
        os.system("cls")
        nome = input("Digite o nome do competidor: ")
        if nome in atletas: 
#verifica se o input existe no dicionario de competidores
            print(f"Digite qual dos {t} valores da lista deseja alterar")
            p = int(input("")) 
#input para selecionar qual dos valores deseja editar
            atletas[nome][p] = float(input("Digite qual o novo valor da entrada: "))
            os.system("cls")
        else:
            print("Competidor não encontrado")
            os.system("pause")

    elif s == 3 and y == 0:
            print("Você ainda não cadastrou nenhum usuario")
    elif s == 3 and y != 0:
            os.system("cls")
            for nome, saltos in atletas.items():
                soma_saltos = 0
                qtd_saltos = 0
                for salto in saltos:
                    soma_saltos += salto
                    qtd_saltos += 1
                media = soma_saltos / qtd_saltos
                print(f"{nome}: {saltos}, Média: {media}")
            os.system("pause")

    elif s == 4:
        w = "S"
    else:
        print("Esta opção não está na lista")