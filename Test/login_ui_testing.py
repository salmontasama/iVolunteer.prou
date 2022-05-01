from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def init():
    driver = webdriver.Chrome('../Base/Driver/chromedriver.exe')
    driver.get("https://ivolunteer-app.herokuapp.com/login")
    driver.maximize_window()
    return driver

#Checking a background image

def test_ui_login_background_imega():
    driver =  init()
    sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]")
    value = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").get_attribute("innerText")
    print(value)
    assert value == ""
    sleep(3)


def test_ui_login_titel():
    driver = init()
    sleep(3)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
    value = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").get_attribute("innerText")
    print(value)
    assert value == "Login"
    sleep(3)


def test_ui_email_titel():
    driver = init()
    sleep(3)
    driver.find_element(By.XPATH,"//label[@id='mui-1-label']")
    value = driver.find_element(By.XPATH,"//label[@id='mui-1-label']").get_attribute("innerText")
    print(value)
    assert value == "Email *"
    sleep(3)

def test_ui_email_asterisk_in_titel():
    driver = init()
    sleep(3)
    driver.find_element(By.XPATH,"//input[@id='mui-1']")
    value = driver.find_element(By.XPATH,"//input[@id='mui-1']").get_attribute("innerText")
    print(value)
    assert value == ""
    sleep(3)


def test_ui_password_titel():
    driver = init()
    sleep(3)
    driver.find_element(By.XPATH,"//input[@id='mui-2']")
    value = driver.find_element(By.XPATH,"//input[@id='mui-2']").get_attribute("innerText")
    print(value)
    assert value == ""
    sleep(3)


def test_ui_button_send():
    driver = init()
    sleep(3)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
    value = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").get_attribute("innerText")
    print(value)
    assert value == "SEND"
    sleep(3)