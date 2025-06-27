from robot import run
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import tempfile
import os

driver_path = ChromeDriverManager().install()
print(f"ChromeDriver instalado em: {driver_path}")

os.environ["webdriver.chrome.driver"] = driver_path

user_data_dir = tempfile.mkdtemp()
print(f"User data dir temporário: {user_data_dir}")

chrome_options = f"--headless --no-sandbox --disable-dev-shm-usage --disable-gpu --user-data-dir={user_data_dir}"

os.environ["ROBOT_CHROME_OPTIONS"] = chrome_options

run('tests/robot/')
