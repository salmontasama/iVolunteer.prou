from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

def init():
    driver = webdriver.Chrome('../Base/Driver/chromedriver.exe')
    driver.get("https://ivolunteer-app.herokuapp.com/login")
    driver.maximize_window()
    return driver

def test_button_Working_right():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    WebDriverWait(driver, 20)

#registration
def test_registration_first_name():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/textarea[1]").send_keys("natan")
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
    sleep(3)

def test_registration_last_name():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/textarea[1]").send_keys("shete")
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
    sleep(5)



def test_registration_email():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[3]/div[1]/textarea[1]").send_keys("natanshete1@gmail.com")
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
    sleep(3)


def test_registration_Languages():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]").send_keys("Hebrew")
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
    sleep(3)


def test_registration_age():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/textarea[1]").send_keys("28")
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
    sleep(3)

def test_registration_phone():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/textarea[1]").send_keys("0549522659")
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
    sleep(3)

def test_registration_city():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    WebDriverWait(driver, 20)
    select = Select(driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/textarea[1]"))
    select.select_by_index()
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
    sleep(3)


def test_registration_description():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/textarea[1]").send_keys("holle")
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
    sleep(3)

def test_registration_image():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[3]").click()
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/fieldset[1]/legend[1]").send_keys("file:///C:/Users/king%20natan/OneDrive/%D7%A9%D7%95%D7%9C%D7%97%D7%9F%20%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94/a6091100-2d43-4174-acb5-9527610c6a7f.jpg")
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
    sleep(3)