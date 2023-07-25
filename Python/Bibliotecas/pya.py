import pyautogui as pag #importa o pyautogui e apelida ele de pag
import time #importa tempo
import os

#//////////////////////////////////////////////////////////////////////////////////////////////////////////

#Por questões de segurança esse código devera ser ativado apenas pela pessoa quando já estiver com o gmail aberto
def sleep():#função para intervalo
    time.sleep(1)#tempo do intervalo

#//////////////////////////////////////////////////////////////////////////////////////////////////////////

time.sleep(5)#intervalo inicial, para dar tempo de entrar no gmail
pag.moveTo(71, 228)#move a seta do mouse
pag.click()#clica
sleep()
pag.moveTo(904, 1070)#move a seta do mouse
pag.click()#clica
y = input("Digite o gmail do destinatário:")#coloca o gmail do destinatário
z = input("Digite o assunto do seu gmail:")#coloca o assunto do gmail
sleep()
pag.keyDown('alt')#aperta alt
pag.press('tab',presses=1,interval=0.5)#pressiona tab
pag.keyUp('alt')#aperta alt
sleep()
pag.write(y)#escreve o gmail de destino
sleep()
pag.moveTo(1257, 468)
pag.click()
time.sleep(2)
pag.moveTo(1257, 468)#move a seta do mouse
pag.click()#clica
pag.write(z)#escreve o assunto do gmail
sleep()
pag.moveTo(1312, 980)#move a seta do mouse
pag.click()#clica
sleep()
pag.click()#clica
pag.write("Curriculo.txt")#digita o nome do arquivo
pag.press('enter')#pressiona enter
pag.moveTo(1109, 575)#move a seta do mouse
sleep()
pag.press('tab')
sleep()
pag.press('enter')