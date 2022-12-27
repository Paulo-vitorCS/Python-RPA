import xlsxwriter  # Biblioteca para trabalhar com excel | LibreOffice
import os


caminho_arquivo = '/home/paulo/PycharmProjects/Python-RPA/Robo02/teste.xlsx'
planilha = xlsxwriter.Workbook(caminho_arquivo)  # Cria e/ou abre o arquivo especificado em segundo plano
planilha1 = planilha.add_worksheet()  # Cria uma nova planilha

planilha1.write('A1', 'Nome')  # Na coluna A, linha 1, escreve Nome
planilha1.write('B1', 'Idade')
planilha1.write('A2', 'Amanda')
planilha1.write('B2', 28)
planilha1.write('A3', 'Roberto')
planilha1.write('B3', 25)

planilha.close()  # Fecha o arquivo em segundo plano (Não está visivel)

os.system('xdg-open ' + caminho_arquivo)  # Usado para abrir a plan. no linux | Windows: os.startfile(caminha_arquivo)
