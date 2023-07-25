import os

atletas = []
registros = []

while True:
    print("Menu Inicial\n")
    print("1- Registro")
    print("2- Alterar")
    print("3- Listar")
    print("4- Sair")
    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        os.system("cls")
        num_atletas = int(input("Digite a quantidade de atletas a serem registrados: "))

        for i in range(num_atletas):
            nome = input(f"Digite o nome do atleta {i+1}°: ")
            num_saltos = int(input("Digite a quantidade de saltos que ele irá realizar: "))
            saltos = []

            for j in range(num_saltos):
                salto = float(input(f"Distância do salto {j+1}°: "))
                saltos.append(salto)
            atleta = {"nome": nome, "saltos": saltos}
            registros.append(atleta)

    elif opcao == "2":
        os.system("cls")
        nome_alterar = input("Digite o nome do atleta a ser alterado: ")

        for i in range(len(registros)):
            if registros[i]["nome"] == nome_alterar:
                num_saltos = len(registros[i]["saltos"])

                for j in range(num_saltos):
                    salto = float(input(f"Distância do salto {j+1}°: "))
                    registros[i]["saltos"][j] = salto
                break
        else:
            print("Atleta não encontrado!")

    elif opcao == "3":
        os.system("cls")
        for atleta in registros:
            nome = atleta["nome"]
            saltos = atleta["saltos"]
            media = sum(saltos) / len(saltos)
            print(f"Atleta: {nome} - Saltos: {saltos} - Média: {media:.2f}")

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")