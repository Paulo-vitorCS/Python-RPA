from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui


browser = webdriver.Firefox()
browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

pyautogui.sleep(1)

browser.find_element(By.NAME, 'endereco').send_keys('05892387')
pyautogui.sleep(2)
browser.find_element(By.NAME, 'btn_pesquisar').click()

pyautogui.sleep(2)

# Dados do site Busca cep
rua = browser.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
bairro = browser.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
uf = browser.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
cep = browser.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text

print(rua, bairro, uf, cep, sep='\n')

pyautogui.sleep(2)
browser.close()
