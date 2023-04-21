'''

Regisztráció -> TC-01; TC-02
Bejelentkezés -> TC-03
Adatkezelési nyilatkozat használata -> TC-05
Adatok listázása -> TC-10
Több oldalas lista bejárása -> TC-07
Új adat bevitel -> TC-06
Ismételt és sorozatos adatbevitel adatforrásból -> TC-01; TC-02
Meglévő adat módosítás -> TC-09
Adat vagy adatok törlése -> TC-08
Adatok lementése felületről -> TC-11
Kijelentkezés -> TC-04

'''

from main_functions import *
import allure
from config import *


class TestSignUp(object):


    def setup_method(self):
        self.browser = webdriver.Chrome()
        config(self.browser)
        self.browser.get('http://localhost:1667/#/register')

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-01")
    @allure.title("Sign up with valid data")
    def test_sign_up_with_csv_valid(self):
        wait = WebDriverWait(self.browser, 2)
        for user in get_users_from_file():
            use_case, username, email, password, expected_title, expected_description = user
            if use_case.startswith('signup_valid'):
                signup(self.browser, username, email, password)
                assert get_error_title(self.browser) == expected_title
                assert get_error_description(self.browser) == expected_description


    @allure.id("TC-02")
    @allure.title("Sign up with invalid data")
    def test_sign_up_with_csv_invalid(self):
        wait = WebDriverWait(self.browser, 2)
        for user in get_users_from_file():
            use_case, username, email, password, expected_title, expected_description = user
            if use_case.startswith('signup_invalid'):
                signup(self.browser, username, email, password)
                assert get_error_title(self.browser) == expected_title
                assert get_error_description(self.browser) == expected_description

'''
class TestSignInAndSignOut:

    def setup_method(self):
        self.browser = config.chrome_driver_config()
        self.browser.get('http://localhost:1667/#/login')

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-03")
    @allure.title("Sign in with valid and invalid data")
    def test_sign_in_with_csv(self):
        wait = WebDriverWait(self.browser, 2)
        for user in get_users_from_file():
            if user[0].startswith('signin'):
                use_case, username, email, password, expected_title, expected_description = user
                signin(self.browser, email, password)
                try:
                    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@active-class='active']")))
                    logout_button.click()
                except:
                    assert get_error_title(self.browser) == expected_title
                    assert get_error_description(self.browser) == expected_description
                    error_but = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']")))
                    error_but.click()

    @allure.id("TC-04")
    @allure.title("Kijelentkezés")
    def testsingout(self):
        wait = WebDriverWait(self.browser, 5)
        for user in get_users_from_file():
            if user[0].startswith('signin_valid'):
                use_case, username, email, password, expected_title, expected_description = user
                signin(self.browser, email, password)
        logout(self.browser)


class TestPrivacyPolicy:

    def setup_method(self):
        self.browser = config.chrome_driver_config()
        self.browser.get('http://localhost:1667/#/')

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-05")
    @allure.title("Cookie elfogadásának tesztelése")
    def test_accept_cookies(self):
        accept_cookies(self.browser)


class TestPostHandling:

    def setup_method(self):
        self.browser = config.chrome_driver_config()
        self.browser.get('http://localhost:1667/#/login')
        for user in get_users_from_file():
            if user[0].startswith('signin_valid'):
                use_case, username, email, password, expected_title, expected_description = user
                signin(self.browser, email, password)

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-06")
    @allure.title("Új poszt létrehozása")
    def test_new_post(self):
        create_new_post(self.browser)

    @allure.id("TC-07")
    @allure.title("Több oldalas lista bejárása")
    def testpaging(self):
        go_through_page_list(self.browser)

    @allure.id("TC-08")
    @allure.title("Delete taggal rendelkező poszt törlése")
    def testpostdelete(self):
        wait = WebDriverWait(self.browser, 5)
        delete_last_post(self.browser)


class TestModifyUserData:

    def setup_method(self):
        self.browser = config.chrome_driver_config()
        self.browser.get('http://localhost:1667/#/login')
        for user in get_users_from_file():
            if user[0].startswith('signin_valid'):
                use_case, username, email, password, expected_title, expected_description = user
                signin(self.browser, email, password)

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-09")
    @allure.title("Felhasználó adatainak módosítása")
    def testmodifyuserdata(self):
        modify_user_data(self.browser)


class TestListOperations:

    def setup_method(self):
        self.browser = config.chrome_driver_config()
        self.browser.get('http://localhost:1667/#/login')
        for user in get_users_from_file():
            if user[0].startswith('signin_valid'):
                use_case, username, email, password, expected_title, expected_description = user
                signin(self.browser, email, password)

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-10")
    @allure.title("Feedek címeinek listázása")
    def test_listing_titles(self):
        list_data(self.browser)
        print(list_to_save)

    @allure.id("TC-11")
    @allure.title("Feedek címeinek listázása és mentése külső fájlba")
    def test_save_data(self):
        saved_data = []
        print(list_to_save)
        with open('export_article.txt', 'w', newline='') as file:
            for title in list_to_save:
                file.write("%s\n" % title)
        with open('export_article.txt', 'r', newline='') as f:
            for i in f:
                saved_data.append(i.replace("\n", ""))
        print(saved_data)
'''