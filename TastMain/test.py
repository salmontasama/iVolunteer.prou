# from selenium import webdriver
# from selenium.webdriver.common.by import By
from time import sleep
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC, wait
# from selenium.webdriver.support.ui import WebDriverWait


def init():
    driver = webdriver.Chrome("C:/Users/IMOE001/PycharmProjects/pythonProject/pythonProject/Driver/chromedriver.exe")
    driver.get('https://ivolunteer-app.herokuapp.com/')
    driver.maximize_window()
    return driver



def test_yosef_link():

    driver = init()
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    sleep(4)
    first = driver.window_handles[0]
    driver.switch_to.window(first)
    sleep(3)
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/i[1]").click()
    first = driver.window_handles[0]
    driver.switch_to.window(first)
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[3]/i[1]").click()
    first = driver.window_handles[0]
    driver.switch_to.window(first)


def test_oshri_link():
    driver = init()
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/i[1]").click()
    sleep(4)
    first = driver.window_handles[0]
    driver.switch_to.window(first)
    sleep(3)
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[2]/i[1]").click()
    first = driver.window_handles[0]
    driver.switch_to.window(first)
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[3]/i[1]").click()
    first = driver.window_handles[0]
    driver.switch_to.window(first)


def test_matan_link():
    driver = init()
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/a[1]/i[1]").click()
    sleep(4)
    first = driver.window_handles[0]
    driver.switch_to.window(first)
    sleep(3)
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/a[2]/i[1]").click()
    first = driver.window_handles[0]
    driver.switch_to.window(first)
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/a[3]/i[1]").click()
    first = driver.window_handles[0]
    driver.switch_to.window(first)


def test_go_volunteer_button():
    driver = init()
    driver.find_element(By.XPATH, "//button[contains(text(),'Go-Volunteer!')]").click()
    verify = driver.find_element(By.XPATH, "//h1[contains(text(),'Login')]").text
    assert verify == 'Login'


def test_valid_Offers_help():
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
    driver.find_element(By.XPATH, "//div[1]/div[4]/button[3]").click()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div["
                                  "1]/textarea[1]").send_keys('salmon')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div["
                                  "1]/textarea[1]").send_keys('hasname')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div["
                                  "1]/textarea[1]").send_keys('24')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[3]/div["
                                  "1]/textarea[1]").send_keys('salmon997@gmail.com')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div["
                                  "1]/textarea[1]").send_keys('0547877244')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[4]/div["
                                  "1]/textarea[1]").send_keys('Hebrew')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[3]/div["
                                  "1]/textarea[1]").send_keys('https://upload.wikimedia.org/wikipedia/commons/4/42'
                                                              '/Solar_prominence_from_STEREO_spacecraft_September_29'
                                                              '%2C_2008.jpg')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div["
                                  "1]/textarea[1]").send_keys('Nursing Home')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()


# def test_invalid_Offers_help_null_name():
#     driver = init()
#     driver.find_element(By.XPATH, "//button[contains(text(),'Go-Volunteer!')]").click()
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
#                                          "1]/input[1]").send_keys('salmon997@walla.co.il')
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div["
#                                          "1]/input[1]").send_keys('123456')
#     driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
#     sleep(3)
#     x = driver.switch_to.alert
#     x.accept()
#     driver.find_element(By.XPATH, "//div[1]/div[4]/button[3]").click()
#     # driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div["
#     #                               "1]/textarea[1]").send_keys('salmon')
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div["
#                                   "1]/textarea[1]").send_keys('hasname')
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div["
#                                   "1]/textarea[1]").send_keys('24')
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[3]/div["
#                                   "1]/textarea[1]").send_keys('salmon997@gmail.com')
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div["
#                                   "1]/textarea[1]").send_keys('0547877244')
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[4]/div["
#                                   "1]/textarea[1]").send_keys('Hebrew')
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[3]/div["
#                                   "1]/textarea[1]").send_keys('https://upload.wikimedia.org/wikipedia/commons/4/42'
#                                                               '/Solar_prominence_from_STEREO_spacecraft_September_29'
#                                                               '%2C_2008.jpg')
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div["
#                                   "1]/textarea[1]").send_keys('Nursing Home')
#     driver.find_element(By.XPATH, "//div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
#     name = driver.find_element(By.XPATH, "//div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").get_attribute('willValidate')
#     assert name != 'true'







def test_valid_volunteer():
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
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[1]/div[1]/textarea[1]").send_keys('salmon')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[1]/textarea[1]").send_keys('tasname')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[3]/div[1]/textarea[1]").send_keys('salmon997@gmail.com')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[4]/div[1]/textarea[1]").send_keys('24')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[5]/div[1]/textarea[1]").send_keys('Adult help')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[1]/div[1]/textarea[1]").send_keys('9:00')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[2]/div[1]/textarea[1]").send_keys('17:00')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[3]/div[1]/textarea[1]").send_keys('0547877244')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[4]/div[1]/textarea[1]").send_keys("https://upload.wikimedia"
                                                                                          ".org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg")
    sleep(3)
    selec = Select(driver.find_element(By.XPATH,'//form[1]/div[2]/select[1]'))
    selec.select_by_index(2)
    sleep(3)
    driver.find_element(By.XPATH, "//form[1]/div[3]/div[1]/div[1]/textarea[1]").send_keys('Hebrew')
    driver.find_element(By.XPATH, "//form[1]/div[3]/div[2]/div[1]/textarea[1]").send_keys('Nursing Home')
    driver.find_element(By.XPATH, "//form[1]/div[3]/button[1]").click()




def test_invalid_volunteer_null_name():
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
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[1]/div[1]/textarea[1]").send_keys('salmon')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[1]/textarea[1]").send_keys('tasname')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[3]/div[1]/textarea[1]").send_keys('salmon997@gmail.com')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[4]/div[1]/textarea[1]").send_keys('24')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[5]/div[1]/textarea[1]").send_keys('Adult help')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[1]/div[1]/textarea[1]").send_keys('9:00')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[2]/div[1]/textarea[1]").send_keys('17:00')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[3]/div[1]/textarea[1]").send_keys('0547877244')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[4]/div[1]/textarea[1]").send_keys("https://upload.wikimedia"
                                                                                          ".org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg")
    sleep(3)
    selec = Select(driver.find_element(By.XPATH,'//form[1]/div[2]/select[1]'))
    selec.select_by_index(2)
    sleep(3)
    driver.find_element(By.XPATH, "//form[1]/div[3]/div[1]/div[1]/textarea[1]").send_keys('Hebrew')
    driver.find_element(By.XPATH, "//form[1]/div[3]/div[2]/div[1]/textarea[1]").send_keys('Nursing Home')
    driver.find_element(By.XPATH, "//form[1]/div[3]/button[1]").click()
    first_name = driver.find_element(By.XPATH, "//form[1]/div[1]/div[1]/div[1]/textarea[1]").get_attribute('validationMessage')
    assert first_name == 'זהו שדה חובה.'



def test_invalid_volunteer_null_last_name():
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
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[1]/div[1]/textarea[1]").send_keys('salmon')
    # driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[1]/textarea[1]").send_keys('tasname')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[3]/div[1]/textarea[1]").send_keys('salmon997@gmail.com')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[4]/div[1]/textarea[1]").send_keys('24')
    driver.find_element(By.XPATH, "//form[1]/div[1]/div[5]/div[1]/textarea[1]").send_keys('Adult help')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[1]/div[1]/textarea[1]").send_keys('9:00')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[2]/div[1]/textarea[1]").send_keys('17:00')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[3]/div[1]/textarea[1]").send_keys('0547877244')
    driver.find_element(By.XPATH, "//form[1]/div[2]/div[4]/div[1]/textarea[1]").send_keys("https://upload.wikimedia"
                                                                                          ".org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg")
    sleep(3)
    selec = Select(driver.find_element(By.XPATH,'//form[1]/div[2]/select[1]'))
    selec.select_by_index(2)
    sleep(3)
    driver.find_element(By.XPATH, "//form[1]/div[3]/div[1]/div[1]/textarea[1]").send_keys('Hebrew')
    driver.find_element(By.XPATH, "//form[1]/div[3]/div[2]/div[1]/textarea[1]").send_keys('Nursing Home')
    driver.find_element(By.XPATH, "//form[1]/div[3]/button[1]").click()
    last_name = driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]").get_attribute('validationMessage')
    assert last_name == 'זהו שדה חובה.'


# def test_invalid_volunteer_null_():
#     driver = init()
#     driver.find_element(By.XPATH, "//button[contains(text(),'Go-Volunteer!')]").click()
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
#                                          "1]/input[1]").send_keys('salmon997@walla.co.il')
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div["
#                                          "1]/input[1]").send_keys('123456')
#     driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
#     sleep(3)
#     x = driver.switch_to.alert
#     x.accept()
#     driver.find_element(By.XPATH, "//button[2]").click()
#     driver.find_element(By.XPATH, "//form[1]/div[1]/div[1]/div[1]/textarea[1]").send_keys('salmon')
#     driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[1]/textarea[1]").send_keys('tasname')
#     driver.find_element(By.XPATH, "//form[1]/div[1]/div[3]/div[1]/textarea[1]").send_keys('salmon997@gmail.com')
#     driver.find_element(By.XPATH, "//form[1]/div[1]/div[4]/div[1]/textarea[1]").send_keys('24')
#     driver.find_element(By.XPATH, "//form[1]/div[1]/div[5]/div[1]/textarea[1]").send_keys('Adult help')
#     driver.find_element(By.XPATH, "//form[1]/div[2]/div[1]/div[1]/textarea[1]").send_keys('9:00')
#     driver.find_element(By.XPATH, "//form[1]/div[2]/div[2]/div[1]/textarea[1]").send_keys('17:00')
#     driver.find_element(By.XPATH, "//form[1]/div[2]/div[3]/div[1]/textarea[1]").send_keys('0547877244')
#     driver.find_element(By.XPATH, "//form[1]/div[2]/div[4]/div[1]/textarea[1]").send_keys("https://upload.wikimedia"
#                                                                                           ".org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg")
#     sleep(3)
#     selec = Select(driver.find_element(By.XPATH,'//form[1]/div[2]/select[1]'))
#     selec.select_by_index(2)
#     sleep(3)
#     driver.find_element(By.XPATH, "//form[1]/div[3]/div[1]/div[1]/textarea[1]").send_keys('Hebrew')
#     driver.find_element(By.XPATH, "//form[1]/div[3]/div[2]/div[1]/textarea[1]").send_keys('Nursing Home')
#     driver.find_element(By.XPATH, "//form[1]/div[3]/button[1]").click()
#      = driver.find_element(By.XPATH, "").get_attribute('validationMessage')
#     assert  =='זהו שדה חובה.'

#
# def test_invalid_volunteer_null_():
#     driver = init()
#     driver.find_element(By.XPATH, "//button[contains(text(),'Go-Volunteer!')]").click()
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
#                                          "1]/input[1]").send_keys('salmon997@walla.co.il')
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div["
#                                          "1]/input[1]").send_keys('123456')
#     driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
#     sleep(3)
#     x = driver.switch_to.alert
#     x.accept()
#     driver.find_element(By.XPATH, "//button[2]").click()
#     driver.find_element(By.XPATH, "//form[1]/div[1]/div[1]/div[1]/textarea[1]").send_keys('salmon')
#     driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[1]/textarea[1]").send_keys('tasname')
#     driver.find_element(By.XPATH, "//form[1]/div[1]/div[3]/div[1]/textarea[1]").send_keys('salmon997@gmail.com')
#     driver.find_element(By.XPATH, "//form[1]/div[1]/div[4]/div[1]/textarea[1]").send_keys('24')
#     driver.find_element(By.XPATH, "//form[1]/div[1]/div[5]/div[1]/textarea[1]").send_keys('Adult help')
#     driver.find_element(By.XPATH, "//form[1]/div[2]/div[1]/div[1]/textarea[1]").send_keys('9:00')
#     driver.find_element(By.XPATH, "//form[1]/div[2]/div[2]/div[1]/textarea[1]").send_keys('17:00')
#     driver.find_element(By.XPATH, "//form[1]/div[2]/div[3]/div[1]/textarea[1]").send_keys('0547877244')
#     driver.find_element(By.XPATH, "//form[1]/div[2]/div[4]/div[1]/textarea[1]").send_keys("https://upload.wikimedia"
#                                                                                           ".org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg")
#     sleep(3)
#     selec = Select(driver.find_element(By.XPATH,'//form[1]/div[2]/select[1]'))
#     selec.select_by_index(2)
#     sleep(3)
#     driver.find_element(By.XPATH, "//form[1]/div[3]/div[1]/div[1]/textarea[1]").send_keys('Hebrew')
#     driver.find_element(By.XPATH, "//form[1]/div[3]/div[2]/div[1]/textarea[1]").send_keys('Nursing Home')
#     driver.find_element(By.XPATH, "//form[1]/div[3]/button[1]").click()
#      = driver.find_element(By.XPATH, "").get_attribute('validationMessage')
#     assert  == 'זהו שדה חובה.'