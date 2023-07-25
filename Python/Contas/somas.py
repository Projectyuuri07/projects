import os

numeros = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

cont = 0
for i in numeros:
     cont += i 

print("resultado = ", cont)

os.system("Pause")