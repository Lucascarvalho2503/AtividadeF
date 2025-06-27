from robot import run
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import os

os.environ['PATH'] += os.pathsep + os.path.dirname(driver_path)
user_data_dir = tempfile.mkdtemp()
print(f"User data dir temporário: {user_data_dir}")

driver_path = ChromeDriverManager().install()
print(f"ChromeDriver instalado em: {driver_path}")

vars_path = os.path.join(os.getcwd(), 'chrome_options_vars.py')

with open(vars_path, 'w') as f:
    f.write(f"""\
from selenium.webdriver.chrome.options import Options

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--user-data-dir={user_data_dir}")
CHROME_OPTIONS.add_argument("--no-sandbox")
CHROME_OPTIONS.add_argument("--disable-dev-shm-usage")
CHROME_OPTIONS.add_argument("--headless=new")
CHROME_OPTIONS.add_argument("--disable-gpu")
""")

print(f"Arquivo de variáveis criado em: {vars_path}")

run(
    'tests/robot/',
    variablefile=[vars_path],
    variable=[f'DRIVER_PATH:{driver_path}']
)
