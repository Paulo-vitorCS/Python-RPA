import pyautogui


opcao = pyautogui.confirm('Clique no botão desejado', buttons=['LibreOffice Calc', 'Editor de Texto'])

if opcao == 'LibreOffice Calc':
    pyautogui.sleep(2)
    pyautogui.hotkey('win')
    pyautogui.sleep(3)
    pyautogui.typewrite('LibreOffice Calc')
    pyautogui.sleep(3)
    pyautogui.press('enter')
elif opcao == 'Editor de Texto':
    pyautogui.sleep(2)
    pyautogui.hotkey('win')
    pyautogui.sleep(3)
    pyautogui.typewrite('Editor de Texto')
    pyautogui.sleep(3)
    pyautogui.press('enter')
