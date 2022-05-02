from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from fdfd import string_normalize



def init():
    driver = webdriver.Chrome("C:/Users/IMOE001/PycharmProjects/pythonProject/pythonProject/Driver/chromedriver.exe")
    driver.get('https://ivolunteer-app.herokuapp.com/')
    driver.maximize_window()
    return driver


# ui home page main
def test_ui_yosef():
    driver = init()
    sleep(4)
    yosef = driver.find_element(By.XPATH,
                                "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h2[1]").text
    assert yosef == 'Lior Yosef'


def test_ui_oshri():
    driver = init()
    sleep(4)
    oshri = driver.find_element(By.XPATH,
                                "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h2[1]").text
    assert oshri == 'Oshri-el Tzagay'


def test_ui_matan():
    driver = init()
    sleep(4)
    matan = driver.find_element(By.XPATH,
                                "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/h2[1]").text
    assert matan == 'Matan ysayas'


def test_ui_logo():
    driver = init()
    sleep(4)
    logo = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/h1[1]").text
    assert logo == 'iVolunteer'


def test_ui_logo_button():
    driver = init()
    sleep(4)
    button_logo = driver.find_element(By.XPATH,
                                      "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    assert button_logo == 'Go-Volunteer!'


# ui provide assistance page
def test_ui_provide_assistance():
    driver = init()
    driver.find_element(By.XPATH, "//button[contains(text(),'Go-Volunteer!')]").click()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
                                  "1]/input[1]").send_keys('salmon997@walla.co.il')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div["
                                  "1]/input[1]").send_keys('123456')
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    x = driver.switch_to.alert
    x.accept()
    # driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[1]/div[4]/button[3]").click()
    provide_assistance_button_ = driver.find_element(By.XPATH, "//button[2]").text
    assert provide_assistance_button_ == 'PROVIDE ASSISTANCE'


def test_ui_provide_assistance_fields():
    driver = init()
    driver.find_element(By.XPATH, "//button[contains(text(),'Go-Volunteer!')]").click()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
                                  "1]/input[1]").send_keys('salmon997@walla.co.il')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div["
                                  "1]/input[1]").send_keys('123456')
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    x = driver.switch_to.alert
    x.accept()
    driver.find_element(By.XPATH, "//button[2]").click()
    fields = driver.find_element(By.XPATH, "//form[1]").get_attribute('innerText')
    assert string_normalize(fields) == "First name *\nFirst name *\nLast name *\nLast name *\nEmail *\nEmail " \
                                       "*\nAge\nAge\nSkills\nSkills\nStartHour\nStartHour\nFinishHour\nFinishHour" \
                                       "\nPhone\nPhone\nProfilePic\nProfilePic\nHaifa\nTel-Aviv\nJerusalem\nBeer " \
                                       "Sheva\nEilat\nKiryat Shmona\nBeer " \
                                       "Sheva\n\n\nLanguage\nLanguage\nDescription\nDescription\nSEND"


def test_ui_provide_assistance_title():
    driver = init()
    driver.find_element(By.XPATH, "//button[contains(text(),'Go-Volunteer!')]").click()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
                                  "1]/input[1]").send_keys('salmon997@walla.co.il')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div["
                                  "1]/input[1]").send_keys('123456')
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    x = driver.switch_to.alert
    x.accept()
    driver.find_element(By.XPATH, "//button[2]").click()
    title = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").text
    assert string_normalize(title) == 'Want\nTo\nVolunteer..?'


def test_ui_provide_assistance_Bottom_page1():
    driver = init()
    driver.find_element(By.XPATH, "//button[contains(text(),'Go-Volunteer!')]").click()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
                                  "1]/input[1]").send_keys('salmon997@walla.co.il')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div["
                                  "1]/input[1]").send_keys('123456')
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    x = driver.switch_to.alert
    x.accept()
    driver.find_element(By.XPATH, "//button[2]").click()
    bottom_page = driver.find_element(By.XPATH, "//footer[1]/ul[1]").get_attribute('innerText')
    assert string_normalize(bottom_page) == "HomeServicesAboutTermsPrivacy Policy"


def test_ui_provide_assistance_Bottom_page2():
    driver = init()
    driver.find_element(By.XPATH, "//button[contains(text(),'Go-Volunteer!')]").click()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
                                  "1]/input[1]").send_keys('salmon997@walla.co.il')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div["
                                  "1]/input[1]").send_keys('123456')
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    x = driver.switch_to.alert
    x.accept()
    driver.find_element(By.XPATH, "//button[2]").click()
    bottom_page = driver.find_element(By.XPATH, "//footer[1]/p[1]").get_attribute('innerText')
    assert string_normalize(bottom_page) == "i Volunteer © 2022"
