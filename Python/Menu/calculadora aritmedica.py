import os
while True:
    os.system("cls")
    # Solicita ao usuário para inserir a operação desejada com base nas opções da tabela
    print("Selecione o número da operação desejada:")
    print("  1 - Soma")
    print("  2 - Subtração")
    print("  3 - Multiplicação")
    print("  4 - Divisão")
    operacao = int(input("Digite sua escolha (1/2/3/4): "))

    # Verifica a operação escolhida e a escolha dos numeros para a conta, por fim realiza a conta
    if operacao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print("O resultado da soma é: ", resultado)

    elif operacao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print("O resultado da subtração é: ", resultado)

    elif operacao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print("O resultado da multiplicação é: ", resultado)

    elif operacao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 == 0 or num1 == 0:
            print("Erro: divisão por zero")
        else:
            resultado = num1 / num2
            print("O resultado da divisão é: ", resultado)
    else:
        print("Operação inválida")

    # Pergunta ao usuário se deseja fazer outra conta
    opcao = input("Deseja fazer outra conta? (Y/N)").lower()
    if opcao != "y":

    # Pergunta ao usuário se deseja sair do programa
        opcao = input("Deseja sair do programa? (Y/N)").lower()
        if opcao == "y":
            break