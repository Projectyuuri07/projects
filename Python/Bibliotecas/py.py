import pyautogui as pya
import time

pya.press('win')
time.sleep(1)
pya.write('Opera')
time.sleep(1)
pya.press('Enter')
time.sleep(1)
pya.write('www.google.com')
time.sleep(1)
pya.press('Enter')
time.sleep(2)
pya.write('paint online')
time.sleep(1)
pya.press('Enter')
time.sleep(1)
pya.moveTo(240, 452)
pya.click()
time.sleep(1)
pya.moveTo(240, 452)

pya.click()
time.sleep(1)
distance = 200
while distance > 0:
        pya.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        pya.drag(0, distance, duration=0.5)   # move down
        pya.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pya.drag(0, -distance, duration=0.5)  # move up
