import requests
import os

print ('GitHub Users')

username = input("Qual é o nome do usuário? \n")
os.system('cls')
print (username)

url= f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print (f'Nome completo: {data["name"]}')
    print (f'Bio: {data["bio"]}')
    print (f'Localização: {data["location"]}')
    print (f'Seguidores: {data["followers"]}')
    print (f'Seguindo: {data["following"]}')

else:
    print ('Não foi encontrado o usuário!')