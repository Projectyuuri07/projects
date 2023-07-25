import os

c=(int(input("Escreva os 3 primeiros numeros do cpf:")))
p=(int(input("Escreva os 3 numeros do meio do cpf:")))
f=(int(input("Escreva os 3 ultimos numeros do cpf:")))

x=(int(input("informe a senha:")))

a=256
b=567
c=245

d=567347

if a==c and b==p and c==f:
    print ("cpf correto")
else:
    print ("cpf incorreto")

if x==d:
    print ("Senha correta")
else:
    print ("Senha incorreta")

os.system ("pause")
