from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from openpyxl import Workbook  # Bibliotecas para trabalhar com planilhas
import os


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

# ---------------------------------------------------------------
# Salvando o endereço em uma planilha

caminho_arquivo = '/home/paulo/PycharmProjects/Python-RPA/Robo03/pequisaEndereco.xlsx'

# Usando o Workbook nesse formato de código, a planilha é sempre recriada!
wb = Workbook()  # Classe para começar a trabalhar com a planilha

planilha = wb.active  # Ativando o uso da planilha
planilha.title = 'Dados'

planilha['A1'] = 'Endereço'
planilha['B1'] = 'Bairro'
planilha['C1'] = 'Cidade'
planilha['D1'] = 'CEP'

linha = len(planilha['A']) + 1
colunaA = 'A' + str(linha)
colunaB = 'B' + str(linha)
colunaC = 'C' + str(linha)
colunaD = 'D' + str(linha)

planilha[colunaA] = rua
planilha[colunaB] = bairro
planilha[colunaC] = uf
planilha[colunaD] = cep

wb.save(filename=caminho_arquivo)

os.system('xdg-open ' + caminho_arquivo)  # Usado para abrir a plan. no linux | Windows: os.startfile(caminha_arquivo)
