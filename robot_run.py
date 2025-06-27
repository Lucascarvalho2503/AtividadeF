from robot import run
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile

user_data_dir = tempfile.mkdtemp()
print(f"User data dir temporário: {user_data_dir}")

chrome_options_list = [
    f"--user-data-dir={user_data_dir}",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--headless=new",
    "--disable-gpu",
]

driver_path = ChromeDriverManager().install()
print(f"ChromeDriver instalado em: {driver_path}")

# Passa as opções no formato literal de lista Python (com colchetes e aspas)
chrome_options_for_robot = str(chrome_options_list)

run('tests/robot/',
    variable=[f'CHROME_OPTIONS:{chrome_options_for_robot}'])
