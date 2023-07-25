def soma (x,y):
    S = x+y
    if S>0:
        v = True
    else:
        v = False
    return v

import os
os.system("cls")

a = int(input("Informe os dois valores: "))
b = int(input("Informe os dois valores: "))

print (soma (a,b))

os.system("pause")