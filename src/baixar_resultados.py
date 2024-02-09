from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.parse
import time
import os
from datetime import datetime

# Diretório onde deseja salvar o arquivo
download_dir = os.path.join(os.getcwd(), "resultados")

# Verifica se o diretório existe, senão o cria
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Configura as opções do Chrome para definir o diretório de download
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir}
chrome_options.add_experimental_option("prefs", prefs)

# Inicializa o serviço do ChromeDriver com as opções configuradas
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", options=chrome_options)

# URL do site
url = "https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx"

# Carrega a página
driver.get(url)

# Espera um pouco para garantir que a página tenha carregado completamente
time.sleep(3)

# Encontra o elemento do link de download utilizando XPath
link_download = driver.find_element(By.XPATH, "//a[@ng-click='baixarResultados()']")

# Obtém o link de download
download_url = link_download.get_attribute("href")

# Obtém a data e hora atual
now = datetime.now()
timestamp = now.strftime("%d-%m-%Y_%H%M%S")

# Define o nome do arquivo com a extensão .xlsx
file_name = f"mega_{timestamp}.xlsx"

# Clica no link para iniciar o download
link_download.click()

print("Download iniciado.")

# Espera um pouco para o download ser concluído
time.sleep(10)

# Renomeia o arquivo para o nome desejado
os.rename(os.path.join(download_dir, "Mega-Sena.xlsx"), os.path.join(download_dir, file_name))
print("Download concluído.")

# Salva o nome do arquivo no arquivo de log
log_file = os.path.join(os.getcwd(), "log.txt")
with open(log_file, "a") as f:
    f.write(file_name + "\n")

# Fecha o navegador
driver.quit()
