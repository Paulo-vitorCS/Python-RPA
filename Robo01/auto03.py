# Abrindo o terminal usando hotkeys e por ele abrir o bloco de notas(gedit)
import pyautogui


pyautogui.hotkey('ctrl', 'alt', 't')  # Usada para digitar hotkeys ou teclas de atalho
pyautogui.sleep(3)

pyautogui.typewrite('gedit')
pyautogui.sleep(2)

pyautogui.press('enter')
pyautogui.sleep(2)

pyautogui.typewrite('Bloco de notas aberto com sucesso!')
pyautogui.sleep(2)

# Linux does not support getActiveWindow()gedit
# fecharGedit = pyautogui.getActiveWindow()  # Captura qual a janela aberta/ativa no momento
# fecharGedit.close()  # Fechar a janela ativa

# pyautogui.press('tab')
# pyautogui.sleep(2)
#
# pyautogui.press('enter')
# pyautogui.sleep(2)
