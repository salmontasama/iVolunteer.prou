from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

def init():
    driver = webdriver.Chrome('../Base/Driver/chromedriver.exe')
    driver.get("https://ivolunteer-app.herokuapp.com/login")
    driver.maximize_window()
    return driver

def test_ui_button():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    value = driver.find_element(By.XPATH,"//header/div[1]/div[1]/div[4]/button[3]/span[1]").get_attribute("innerText")
    print(value)
    assert value == ""


def test_Video_background():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    ui = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/video[1]").get_attribute("innerText")
    print(ui)
    assert ui == ""


def test_title_land_a_hand():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    ui = driver.find_element(By.XPATH,"//h1[contains(text(),'Land a Hand')]").get_attribute("innerText")
    print(ui)
    assert ui == "Land a Hand"


def test_text_first_name():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    ui = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]").get_attribute("innerText")
    print(ui)
    assert ui == "First name *"


def test_text_last_name():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    ui = driver.find_element(By.XPATH,"//textarea[@id='mui-3']").get_attribute("innerText")
    print(ui)
    assert ui == "First name *"


def test_text_email():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    ui = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[3]").get_attribute("innerText")
    print(ui)
    assert ui == "First name *\nFirst name *"

def test_text_languages():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    ui = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[4]").get_attribute("innerText")
    print(ui)
    assert ui == "First name *\nFirst name *"

def test_text_age():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    ui = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[4]").get_attribute("innerText")
    print(ui)
    assert ui == "First name *"

def test_Cities_categories():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    ui = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/select[1]").get_attribute("innerText")
    print(ui)
    assert ui == "Age\nAge\n\n\nHaifa\nTel-Aviv\nJerusalem\nBeer Sheva\nEilat\nKiryat Shmona\nBeer Sheva\n\n\nPhone\nPhone\n\n\nImage for post\nImage for post\n\n"






