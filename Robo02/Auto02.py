# Biblioteca selenium usada para trabalhar com páginas web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui

browser = webdriver.Firefox()
browser.get('https://www.google.com/')

pyautogui.sleep(1)

# Procurando pelo elemento NAME, e ao encontrar escrever 'dolar hoje'
browser.find_element(By.NAME, 'q').send_keys('Dolar hoje')
pyautogui.sleep(1)

# Faz a busca da key digitada | "Tecla enter"
browser.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
pyautogui.sleep(2)

# Captura o valor do dolar que foi pesquisado
valor_dolar = browser.find_elements(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/'
                                    + 'div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]')[0].text

print('Esse é o valor do dollar hoje: R$', valor_dolar)

# O código acima é uma cópia de Auto01.py
# -----------------------------------------------------

pyautogui.sleep(1)

# Procurando pelo elemento NAME, e ao encontrar não escreve nada
browser.find_element(By.NAME, 'q').send_keys('')
pyautogui.sleep(1)

# Pressiona tab para selecionar X (clear) na barra de pesquisa do google
pyautogui.press('tab')
pyautogui.sleep(2)

# Pressiona enter limpando a barra de pesquisa
pyautogui.press('enter')
pyautogui.sleep(2)

# Procurando pelo elemento NAME, e ao encontrar escrever 'euro hoje'
browser.find_element(By.NAME, 'q').send_keys('euro hoje')
pyautogui.sleep(1)

# Faz a busca da key digitada | "Tecla enter"
browser.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
pyautogui.sleep(2)

# Captura o valor do dolar que foi pesquisado
valor_euro = browser.find_elements(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/'
                                   + 'div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]')[0].text

print('Esse é o valor do euro hoje: R$', valor_euro)

browser.close()
