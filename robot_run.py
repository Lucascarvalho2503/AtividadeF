from robot import run
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Instala o ChromeDriver automaticamente e pega o caminho
driver_path = ChromeDriverManager().install()
print(f"ChromeDriver instalado em: {driver_path}")

# Define o driver para o SeleniumLibrary usar
import os
os.environ["webdriver.chrome.driver"] = driver_path

# Roda os testes da pasta tests/robot
run('tests/robot/')
