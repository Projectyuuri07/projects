import os

numeros = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < num:
        menor = num

os.system("cls")
print("O maior numero é:", maior)
print("O menor número é:", menor)