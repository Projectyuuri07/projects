import pandas as pan

df = pan.read_excel('C:\\Projetos\\Projeto Python\\pla1.xlsx') # Ela carrega os dados do arquivo do Excel em um DataFrame chamado df
dfcopy = df.copy() #Cria uma cópia do DataFrame e faz com que a cópia seja armazenada em um novo DataFrame chamado dfcopy
dfcopy.to_excel('C:\\Projetos\\Projeto Python\\pla2.xlsx', index=False)#Essa linha salva o DataFrame dfcopy em um novo arquivo xlsx
print(df)