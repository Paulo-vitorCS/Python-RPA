# Abrir a Firefox e pesquisar o valor do dólar
import pyautogui


pyautogui.sleep(4)  # Aguarda um determinado tempo
print(pyautogui.position())  # Imprime a posição (x,y) do mouse

pyautogui.moveTo(x=1399, y=13)  # Move o cursor do mouse até a posição imposta
pyautogui.click(x=1399, y=13)  # Click na posição desejada
pyautogui.sleep(3)

pyautogui.typewrite('Firefox')
pyautogui.sleep(2)

pyautogui.moveTo(x=2354, y=203)
pyautogui.click(x=2354, y=203)
pyautogui.sleep(6)

pyautogui.typewrite('https://www.google.com')
pyautogui.sleep(2)

pyautogui.press('enter')
pyautogui.sleep(6)

pyautogui.typewrite('Valor do dolar')
pyautogui.sleep(2)
pyautogui.press('enter')
pyautogui.sleep(6)
