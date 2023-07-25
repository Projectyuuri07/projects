import requests as r
import json
import os

x= "x"
while x == "x":
    os.system('clear')
    imagem = input("Coloque o Link da sua imagem aqui: ")
    url = "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/70da8d97-23c8-4810-b87f-6c8ced8c4b4f/classify/iterations/CAPYBARA/url"

    header = {
        "Prediction-Key": "f340bb64e4b9499f89fd1aa2ac649176",
        "Content-Type": "application/json",
    }
    body = {"Url": f"{imagem}"}

    response = r.post(url, json=body, headers=header)


    resultado = json.loads(response.text)

    print("Esse é o possivel resultado da sua imagem:")
    for prediction in resultado['predictions']:
        probabilidades = prediction['probability'] * 100
        print(f"{prediction['tagName']}: {probabilidades:.2f}%")

    os.system("pause") 
    sair = input("Deseja Sair? (Y/N): ")
    sair.upper()
    if sair == "N":
        os.system("cls")
    elif sair == "Y":
        x = 0