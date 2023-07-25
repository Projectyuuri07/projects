Y=1
while Y==1:

    nome1 = input("Informe o nome do Aluno 1:  ")
    idade1 = input(f"Informe a idade do {nome1}: ")

    nome2 = input("Informe o nome do Aluno 2:  ")
    idade2 = input(f"Informe a idade do {nome2}: ")

    if idade1>idade2:
        print(f"{nome1} tem {idade1} anos, {nome2} tem {idade2} anos, {nome1} é mais velho")
    else:
        print (f"{nome1} tem {idade1} anos, {nome2} tem {idade2} anos, {nome2} é mais velho")

    x = int(idade1)+int(idade2)

    print(f"A idade somada dos alunos é de {x} anos")

    input ("Voce deseja sair?")
    Y=2