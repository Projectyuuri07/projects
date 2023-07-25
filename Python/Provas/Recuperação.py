import os

lista = [3, 1, 4, 6, 2, 5]

meudict = {}
#############################################################################

meudict[(0,0)] = lista[2]
meudict[(0,1)] = 0
meudict[(0,2)] = 0
meudict[(0,3)] = lista[3]
#############################################################################

meudict[(1,0)] = 0
meudict[(1,1)] = 0
meudict[(1,2)] = lista[1]
meudict[(1,3)] = 0
#############################################################################

meudict[(2,0)] = 0
meudict[(2,1)] = 0
meudict[(2,2)] = lista[4]
meudict[(2,3)] = 0
#############################################################################

meudict[(3,0)] = 0
meudict[(3,1)] = lista[0]
meudict[(3,2)] = 0
meudict[(3,3)] = lista[5]
#############################################################################

os.system('cls')
print(meudict[(0,0)],meudict[(0,1)],meudict[(0,2)],meudict[(0,3)])
print(meudict[(1,0)],meudict[(1,1)],meudict[(1,2)],meudict[(1,3)])
print(meudict[(2,0)],meudict[(2,1)],meudict[(2,2)],meudict[(2,3)])
print(meudict[(3,0)],meudict[(3,1)],meudict[(3,2)],meudict[(3,3)])
os.system('pause')