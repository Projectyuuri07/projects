import os
os.system('cls') #limpa o terminal
n = int(input('Digite um número:')) #pede para o usuario enserir um numero que sera atribuido a uma variavel
for i in range(n+1): #cria um loopin aonde o codigo ira se repetir até o numero inserido acima acabar
    n == n-1 #realiza a conta para a listagem do numero em ordem crescente
    if (n%3) == 0:
        print('Senai')
    elif (n%5) == 0:
        print('Jundiaí')
    elif (n/3) == 0 and (n%5) == 0:
        print('Senai Jundiaí')
    else:
        print(n) #imprime o resultado da conta cada vez que o loopin se repete
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Correção do Código
import os
os.system('cls') 
n = int(input('Digite um número:')) 
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("SenaiJundiai")
    elif i % 3 == 0:
        print("Senai")
    elif i % 5 == 0:
        print("Jundiai")
    else:
        print(i)
os.system('pause')

#////////////////////////////////////////////////////////////////////////////////////////////////////////////