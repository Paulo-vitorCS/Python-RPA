# Sistema operacional utilizado: Ubuntu 22.04
# Dois monitores
import pyautogui


pyautogui.sleep(4)  # Faz um sleep para mudarmos a posição do mouse
print(pyautogui.position())  # Imprime a posição (x,y) do mouse

pyautogui.moveTo(x=1399, y=13)  # Move o cursor do mouse até a posição imposta
pyautogui.click(x=1399, y=13)  # Click na posição desejada

pyautogui.sleep(3)

pyautogui.typewrite('Calculadora')

pyautogui.sleep(2)

pyautogui.moveTo(x=2354, y=203)
pyautogui.click(x=2354, y=203)
