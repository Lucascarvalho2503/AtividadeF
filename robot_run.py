from robot import run
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile


chrome_options = Options()

user_data_dir = tempfile.mkdtemp()
print(f"User data dir temporário: {user_data_dir}")
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--disable-gpu')


driver_path = ChromeDriverManager().install()
print(f"ChromeDriver instalado em: {driver_path}")


run('tests/robot/',
    variable=[
        f'CHROME_OPTIONS:{chrome_options.arguments}'  
    ])
