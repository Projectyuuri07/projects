import os
import time

class Personagens:
    def vida(vida):
        vida = 10
        return vida
    
    def dano(dano):
        dano = 10
        return dano
    
class Mago(Personagens):
    def vida(vida):
        vida = 7
        return vida
    
    def dano(dano):
        dano = 13
        return dano
    
    def longo_alcance(defesa):
        longo_alcance = 5
        return longo_alcance

class Guerreiro(Personagens):
    def vida(vida):
        vida = 13
        return vida
    
    def dano(dano):
        dano = 8
        return dano
    
    def defesa(defesa):
        defesa = 20
        return defesa
    

class Inimigos(Personagens):
    def vida(vida):
        vida = 10
        return vida

    def dano_inimigo(dano):
        dano = 10
        return dano
    
class Ini_forte(Inimigos):
    def vida_inimigo(vida):
        vida = 15
        return vida

    def dano_inimigo(dano):
        dano = 15
        return dano

class Ini_fraco(Inimigos):
    def vida_inimigo(vida):
        vida = 2
        return vida

    def dano_inimigo(dano):
        dano = 2
        return dano

def espera():
    time.sleep(3)

def espera2():
    time.sleep(2)