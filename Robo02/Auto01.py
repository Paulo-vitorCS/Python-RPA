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
                                              'div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]')[0].text

print(valor_dolar)

pyautogui.sleep(1)
browser.close()
