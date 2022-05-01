from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def init():
    driver = webdriver.Chrome('../Base/Driver/chromedriver.exe')
    driver.get("https://ivolunteer-app.herokuapp.com/login")
    driver.maximize_window()
    return driver

#Checking email
#Check with a correct email and a correct password
def test_login_with_proper_email_and_posswerd():
    driver = init()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH,"//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    value = driver.find_element(By.XPATH,"//input[@id='mui-1']").get_attribute("innerText")
    sleep(3)
    print(value)
    assert value == ""


#Check with a correct posswerd and a _email_noll
def test_login_with_proper_posswerd_and_email_noll():
    driver = init()
    driver.find_element(By.XPATH,"//input[@id='mui-1']").send_keys("")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    value = driver.find_element(By.XPATH,"//input[@id='mui-2']").get_attribute("innerText")
    print(value)
    assert value == ""

#Check with a correct posswerd and a _email_posswerd
def test_login_with_invalid_email_and_noll_posswerd():
    driver = init()
    driver.find_element(By.XPATH,"//input[@id='mui-1']").send_keys("שלום")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    value = driver.find_element(By.XPATH,"//input[@id='mui-1']").get_attribute("innerText")
    print(value)
    assert value == ""


def test_login_with_numbers_email_and_noll_posswerd():
    driver = init()
    driver.find_element(By.XPATH,"//input[@id='mui-1']").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    value = driver.find_element(By.XPATH,"//input[@id='mui-1']").get_attribute("innerText")
    print(value)
    assert value == ""

def test_login_with_special_Characters_email_and_noll_posswerd():
    driver = init()
    driver.find_element(By.XPATH,"//input[@id='mui-1']").send_keys("@@@@@@")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    value = driver.find_element(By.XPATH,"//input[@id='mui-1']").get_attribute("innerText")
    print(value)
    assert value == ""




#Checking posswerd
#Check with a correct email and a noll_posswerd
def test_login_with_proper_email_and_noll_posswerd():
    driver = init()
    driver.find_element(By.XPATH,"//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    value = driver.find_element(By.XPATH,"//input[@id='mui-1']").get_attribute("innerText")
    sleep(3)
    print(value)
    assert value == ""


def test_login_with_proper_email_and_invalid_posswerd():
    driver = init()
    driver.find_element(By.XPATH,"//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("שלום")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    value = driver.find_element(By.XPATH,"//input[@id='mui-1']").get_attribute("innerText")
    sleep(3)
    print(value)
    assert value == ""


def test_login_with_proper_email_and_special_Characters_posswerd():
    driver = init()
    driver.find_element(By.XPATH,"//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("@@@@@")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    value = driver.find_element(By.XPATH,"//input[@id='mui-1']").get_attribute("innerText")
    sleep(3)
    print(value)
    assert value == ""

