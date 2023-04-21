from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def config(browser):
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
