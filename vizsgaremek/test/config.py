from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def chrome_driver_config():
    s = Service(executable_path=ChromeDriverManager().install())
    o = Options()
    o.add_experimental_option('detach', True)
    browser = webdriver.Chrome(service=s, options=o)
    o.add_argument('--headless')
    o.add_argument('--no-sandbox')
    o.add_argument('--disable-dev-shm-usage')

    return browser
