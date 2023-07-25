class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.saltos = []

    def adicionar_salto(self, salto):
        self.saltos.append(salto)

    def media_saltos(self):
        return sum(self.saltos) / len(self.saltos)

    def atualizar_salto(self, indice, novo_valor):
        self.saltos[indice] = novo_valor


atletas = []
opcao = 0

while opcao != 4:
    print("Menu inicial \n")
    print("1- Registro \n 2- Alterar \n 3- Listar \n 4- Sair \n")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        num_atletas = int(input("Quantos atletas participaram da prova? "))
        for i in range(num_atletas):
            nome = input(f"Nome do atleta {i+1}: ")
            atleta = Atleta(nome)
            for j in range(5):
                salto = float(input(f"Digite o valor do {j+1}º salto: "))
                atleta.adicionar_salto(salto)
            atletas.append(atleta)

        print("\n Valores registrados com sucesso! \n ")

    elif opcao == 2:
        print("\n Atletas registrados: \n")
        for i, atleta in enumerate(atletas):
            print(f"{i+1}. {atleta.nome}")
        escolha_atleta = int(input(" \n Escolha o número do atleta que deseja alterar: "))
        atleta_alterar = atletas[escolha_atleta - 1]
        print(f"\n O que deseja alterar para {atleta_alterar.nome}?")
        for i, salto in enumerate(atleta_alterar.saltos):
            print(f"{i+1}º salto: {salto}")
        escolha_salto = int(input("\n Escolha o número do salto que deseja alterar: "))
        novo_valor = float(input("\n Digite o novo valor do salto: "))
        atleta_alterar.atualizar_salto(escolha_salto - 1, novo_valor)
        print("\n Valor alterado com sucesso! \n")
        escolha_continuar = input("Deseja voltar para o menu inicial (M) ou alterar outro resultado (A)? ")
        while escolha_continuar.upper() not in ["M", "A"]:
            escolha_continuar = input("Opção inválida! Digite M para voltar ao menu ou A para alterar outro resultado: ")
        if escolha_continuar.upper() == "M":
            print("")
        elif escolha_continuar.upper() == "A":
            opcao = 2

    elif opcao == 3:
        print("\n Resultados dos atletas: \n")
        for atleta in atletas:
            print(f"{atleta.nome}: {atleta.media_saltos()}")

    elif opcao == 4:
        print("\n Saindo...")

    else:
        print("\n Opção inválida! \n")
