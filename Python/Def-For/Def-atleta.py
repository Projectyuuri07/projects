import os

def registro(atletas):
    nome = input("Digite o nome do competidor: ")
    t = int(input("Digite quantos saltos o competidor deu: "))
    val = []
    for num in range(t):
        num = float(input(f"Digite a distância do {num+1}º salto: "))
        val.append(num)
    atletas[nome] = val

def alterar(atletas):
    nome = input("Digite o nome do competidor: ")
    if nome in atletas:
        t = len(atletas[nome])
        print(f"Digite qual dos {t} valores da lista deseja alterar?")
        p = int(input(""))
        atletas[nome][p] = float(input("Digite qual o novo valor da entrada: "))
    else:
        print("Competidor não encontrado")

def listar(atletas):
    if not atletas:
        print("Você ainda não cadastrou nenhum usuário")
    else:
        for nome, saltos in atletas.items():
            soma_saltos = 0
            qtd_saltos = 0
            for salto in saltos:
                soma_saltos += salto
                qtd_saltos += 1
            media = soma_saltos / qtd_saltos
            print(f"{nome}: {saltos}, Média: {media:.2f}")

def competicao():
    w = "N"
    atletas = {}

    while w != "S":
        os.system("cls")
        print("Selecione uma opção dentre as seguintes \n [1] Registro \n [2] Alterar \n [3] Listar \n [4] Sair")
        s = int(input("Digite a opção que deseja: "))

        if s == 1:
            os.system("cls")
            registro(atletas)
            os.system("cls")

        elif s == 2:
            os.system("cls")
            alterar(atletas)
            os.system("cls")

        elif s == 3:
            os.system("cls")
            listar(atletas)
            os.system("pause")

        elif s == 4:
            w = "S"
        else:
            print("Esta opção não está na lista")

competicao()