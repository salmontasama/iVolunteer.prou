from selenium import webdriver
from Utilitis import constants as CO


def initroot():
    driver = webdriver.Chrome(
        executable_path=CO.driver_executable_path)
    return driver

def init_home_page():
    driver = webdriver.Chrome(
        executable_path=CO.driver_executable_path)
    driver.get(CO.base_url)
    return driver