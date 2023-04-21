from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import csv
import time


def signup(browser, username, email, password):
    wait = WebDriverWait(browser, 10)
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    email_input = browser.find_element(By.XPATH, "//input[@placeholder='Email']")
    password_input = browser.find_element(By.XPATH, "//input[@placeholder='Password']")
    signup_but = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary pull-xs-right']")
    username_input.send_keys(username)
    email_input.send_keys(email)
    password_input.send_keys(password)
    signup_but.click()
    get_error_title = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='swal-title']")))
    get_error_description = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='swal-text']")))
    confirm_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='OK']")))
    confirm_button.click()


def get_error_title(browser):
    wait = WebDriverWait(browser, 10)
    title_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
    return title_element.text


def get_error_description(browser):
    wait = WebDriverWait(browser, 10)
    description_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="swal-text"]')))
    return description_element.text


def get_users_from_file():
    with open('datasource_users.csv', 'r', encoding='UTF-8') as datafile:
# local with open('datasource_users.csv', 'r', encoding='UTF-8') as datafile:
        users = csv.reader(datafile, delimiter=';')
        next(users)
        return list(users)


def signin(browser, email, password):
    wait = WebDriverWait(browser, 10)
    email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Email']")))
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
    sign_in_button = browser.find_element(By.XPATH, "//button[normalize-space()='Sign in']")
    email_input.click()
    time.sleep(0.2)
    email_input.send_keys(Keys.CONTROL + 'a')
    time.sleep(0.2)
    email_input.send_keys(Keys.DELETE)
    time.sleep(0.2)
    password_input.click()
    time.sleep(0.2)
    password_input.send_keys(Keys.CONTROL + 'a')
    time.sleep(0.2)
    password_input.send_keys(Keys.DELETE)
    time.sleep(0.2)
    email_input.send_keys(email)
    time.sleep(0.2)
    password_input.send_keys(password)
    time.sleep(0.2)
    sign_in_button.click()


def accept_cookies(browser):
    wait = WebDriverWait(browser, 10)
    cookie_accept = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[@class='cookie__bar__buttons__button cookie__bar__buttons__button--accept']")))
    cookie_accept.click()
    cookie_status = browser.get_cookie("vue-cookie-accept-decline-cookie-policy-panel")
    assert cookie_status["value"] == "accept"


def logout(browser):
    wait = WebDriverWait(browser, 20)
    logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='container']/ul/li)[5]")))
    logout_button.click()
    time.sleep(2)
    signin_button = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='container']/ul/li)[2]")))
    assert signin_button.text == "Sign in"


def create_new_post(browser):
    topic = "teszttopic"
    article = "tesztarticle"
    title = "todelete"
    tag = "teszttag"
    wait = WebDriverWait(browser, 20)
    new_article_nav = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='#/editor']")))
    new_article_nav.click()
    article_inp = wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@class='form-control']")))
    text_area = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@type='text']")))
    title_input = text_area[0]
    topic_input = text_area[1]
    tag_input = text_area[2]
    title_input.send_keys(title)
    article_inp.send_keys(article)
    tag_input.send_keys(tag)
    topic_input.send_keys(topic)
    publish = browser.find_element(By.XPATH, "//button[@type='submit']")
    publish.click()
    title_res = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='container']/h1"))).text
    assert title_res == title
    time.sleep(1)


def modify_user_data(browser):
    description_text = "Test modified description"
    username_text = "Automated modified username"
    picture_url = "https://thumbs.dreamstime.com/z/vector-illustration-avatar-dummy-sign-collection-avatar-image-stock-symbol-web-vector-design-avatar-dummy-137160097.jpg"
    wait = WebDriverWait(browser, 20)
    time.sleep(2)
    settings = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='container']/ul/li)[3]")))
    settings.click()
    picture = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='URL of profile picture']")))
    username = wait.until(EC.visibility_of_element_located((By.XPATH, "// input[@placeholder='Your username']")))
    description = wait.until(
        EC.visibility_of_element_located((By.XPATH, "// textarea[@placeholder='Short bio about you']")))
    update_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, " //button[normalize-space()='Update Settings']")))
    picture.send_keys(Keys.CONTROL + 'a')
    picture.send_keys(Keys.DELETE)
    picture.send_keys(picture_url)
    description.send_keys(Keys.CONTROL + 'a')
    description.send_keys(Keys.DELETE)
    description.send_keys(description_text)
    username.send_keys(Keys.CONTROL + 'a')
    username.send_keys(Keys.DELETE)
    username.send_keys(username_text)
    time.sleep(5)
    update_button.click()
    update_message = wait.until(EC.visibility_of_element_located((By.XPATH, " //div[@class='swal-title']")))
    assert update_message.text == "Update successful!"
    ok_button = wait.until(EC.visibility_of_element_located((By.XPATH, " //button[normalize-space()='OK']")))
    ok_button.click()
    assert picture.get_attribute("value") == picture_url
    assert username.get_attribute("value") == username_text
    assert description.get_attribute("value") == description_text


def go_through_page_list(browser):
    wait = WebDriverWait(browser, 20)
    pagination = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pagination")))
    page_links = pagination.find_elements(By.TAG_NAME, "a")
    counter = 0
    for page_link in page_links:
        counter += 1
        page_link.click()
        continue
    assert str(counter) == page_links[-1].text


def delete_last_post(browser):
    wait = WebDriverWait(browser, 20)
    last_post_link = wait.until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                       "//div[@class='article-preview']")))[-1]
    last_post_link_title = \
        wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "(//div[@class='article-preview'])[last()]//a/h1")))[-1]
    assert last_post_link_title.text == "todelete"
    last_post_link.click()
    delete_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-outline-danger btn-sm']")))
    delete_button.click()
    last_post_link_after_delete_title = \
        wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "(//div[@class='article-preview'])[last()]//a/h1")))[-1]
    assert not last_post_link_after_delete_title.text == "todelete"


list_to_save = []


def list_data(browser):
    wait = WebDriverWait(browser, 10)
    articletitles = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, f'//div[@class="article-preview"]/a[@class="preview-link"]/h1')))
    global list_to_save
    for articletitle in articletitles:
        list_to_save.append(articletitle.text)
