###=-|COMO USAR UM DICIONÁRIO|-=############################################################################

# Criar um dicionário
dicionario = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3",
}

# Acessando valores do dicionário
print(dicionario["chave1"]) #Saida: valor1

# Adicionando um novo par chave-valor ao dicionário
dicionario["chave4"] = "valor4"

# Modificar um valor existente
dicionario["chave2"] = "novo_valor2"

# Removendo um par chave-valor do dicionário
del dicionario["chave3"]

# Verificando se uma chave existe no dicionário
if "chave1" in dicionario:
    print("A chave1 está presente no dicionário")

# Obtendo todas as chaves do dicionário
chaves = dicionario.keys()
print(chaves) #Saida: dic_keys(["chave1", "chave2", "chave4"])

# Obtendo todos os valores do dicionário
valores = dicionario.values()
print(valores) #Saida: dict_values(["valor1", "novo_valor2", "valor4"])

# Iterando sobre as chaves e valores do dicionario
for chave, valor in dicionario.items():
    print(chave, valor)

###=-|USUARIO FAZER A INSERÇÂO DOS DADOS NO DICIONÁRIO|-=###################################################

# Criando um dicionario vazio
dicionario = {}

# Solicitando input do usuario para adicionar valores ao dicionário
chave = input("Digite a chave: ")
valor = input("Digite o valor: ")

# Adicionando a entrada do usuario ao dicionário
dicionario[chave] = valor

# Imprimindo o dicionario atualizado
print(dicionario)

###=-|MODIFICAR O VALOR DE UMA CHAVE|-=#####################################################################

# Criando um dicionário de exemplo
dicionario = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3",
}

# Solicitando ao usuario a chave a ser modificada
chave_modificar = input("Digite a chave que deseja modificar: ")

# Verificando se a chave está presente no dicionário
if chave_modificar in dicionario:
    # Solicitando ao usuario o novo valor para a chave
    novo_valor = input("Digite o novo valor para a chave: ")

    # Atualizando o valor correspondente a chave fornecida pelo usuario
    dicionario[chave_modificar] = novo_valor
    print("Chave modificada com sucesso!")
else:
    print("Chave não encontrada no dicionário.")

# Imprimindo o dicionário atualizado
print(dicionario)

###=-|MODIFICAR A CHAVE DO USUARIO|-=#######################################################################

# Criando um dicionário de exemplo
dicionario = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3",
}

# Solicitando ao usuario a chave a ser modificada
chave_modificar = input("Digite a chave que deseja modificar: ")

# Verificando se a chave está presente no dicionário
if chave_modificar in dicionario:
    # Solicitando ao usuario o novo valor para a chave
    nova_chave = input("Digite a nova chave: ")

    # Criando um novo item a chave modificada e o mesmo
    valor = dicionario[chave_modificar]
    dicionario[nova_chave] = valor

    # Removendo o item antigo do dicionário
    del dicionario[chave_modificar]

    print("Chave modificada com sucesso!")
else:
    print("Chave não encontrada no dicionário.")

# Imprimindo o dicionario atualizado
print(dicionario)

###=-|Mediana usando o dicionário|-=########################################################################

# Criando um dicionário vazio
dicionario = {}

# Solicitando ao usuário inserir pares chave-valor
while True:
    chave = input("Digite uma chave (ou 'sair' para encerrar): ")
    if chave.lower() == "sair":
        break
    valor = float(input("Digite um valor para a chave {}: ".format(chave)))
    dicionario[chave] = valor

# Obtendo os valores do dicionário em uma lista
valores = list(dicionario.values())

# Ordenando a lista de valores em ordem crescente
valores_ordenados = sorted(valores)

# Calculando o tamanho da lista
tamanho = len(valores_ordenados)

# Verificando se a lista possui um número par de elementos
if tamanho % 2 == 0:
    # Se for par, calculando a média dos dois elementos do meio
    indice_meio = tamanho // 2
    mediana = (valores_ordenados[indice_meio - 1] + valores_ordenados[indice_meio]) / 2
else:
    # Se for ímpar, pegando o elemento do meio
    indice_meio = tamanho // 2
    mediana = valores_ordenados[indice_meio]

# Imprimindo a mediana
print("A mediana dos valores do dicionário é:", mediana)
