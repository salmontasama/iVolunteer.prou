from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Base.Utils.string_format import string_normalize
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

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
    value = driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[1]/div[5]/button[1]").get_attribute("innerText")
    print(value)
    assert value == "R"

#bug
def test_ui_log_out_in_button():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    value = driver.find_element(By.XPATH,"/html[1]/body[1]/div[4]/div[3]").get_attribute("innerText")
    print(value)
    assert value =="Provide assistanceSeeking assistancevolunteersneed volunteers"

def test_log_out_button_workin():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[1]/div[5]/button[1]").click()
    sleep(4)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[3]").click()
    sleep(4)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[2]/button[1]").click()
    sleep(3)


def test_ui_Logg_off_from_iVolunteer():
    driver = init()
    driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("natanshete1@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("123456789")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[1]/div[5]/button[1]").click()
    WebDriverWait(driver, 20)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[3]").click()
    WebDriverWait(driver, 20)
    ui1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/h2[1]").get_attribute("innerText")
    assert string_normalize(ui1) =="Logg-Off From iVolunteer"
    ui2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/div[1]/p[1]").get_attribute("innerText")
    sleep(4)
    assert string_normalize(ui2) == "Hey natanshete1@gmail.com ! We Hope to see you soon again"
