from robot import run
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import os


user_data_dir = tempfile.mkdtemp()
print(f"User data dir temporário: {user_data_dir}")


driver_path = ChromeDriverManager().install()
print(f"ChromeDriver instalado em: {driver_path}")


vars_path = os.path.join(os.getcwd(), 'chrome_options_vars.py')
with open(vars_path, 'w') as f:
    f.write(
        'LIST__CHROME_OPTIONS = ' +
        repr([
            f"--user-data-dir={user_data_dir}",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--headless=new",
            "--disable-gpu",
        ]) +
        '\n'
    )
print(f"Arquivo de variáveis criado em: {vars_path}")


run(
    'tests/robot/',
    variablefile=[vars_path]
)