import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from Utilitis import constants as CO, driver as DR, func as FU


def test_navbar_links():
    driver = DR.initroot()
    driver.get(CO.login_page_url)
    driver.implicitly_wait(20)
    email_field = driver.find_element(By.XPATH,CO.login_email_field_Xpath)
    password_field = driver.find_element(By.XPATH,CO.login_password_field_Xpath)
    send_button = driver.find_element(By.XPATH,CO.login_send_button_Xpath)
    fields = [email_field,password_field]
    for field,values in zip(fields,CO.user_details.values()):
        time.sleep(1.5)
        field.send_keys(values)
    send_button.click()
    time.sleep(5)
    obj = driver.switch_to.alert
    msg = obj.text
    print("Alert shows following message: " + msg)
    obj.accept()
    print(" Clicked on the OK Button in the Alert Window")
    action = ActionChains(driver)
    donat_add_exit = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[5]/div[1]/*[1]")
    action.move_to_element(donat_add_exit).click(donat_add_exit).perform()
    volunteers_button = driver.find_element(By.XPATH,"//header/div[1]/div[1]/div[4]/button[4]")
    volunteers_button.click()
    nav_con = driver.find_element(By.XPATH,CO.navbar_container)
    navbar_links = nav_con.find_elements(by=By.TAG_NAME,value="button")
    time.sleep(4)
    for i in navbar_links[1:]:
        i.click()
    FU.success_finish("Navbar link")

def test_hero_page_links():
    driver = DR.initroot()
    driver.get(CO.login_page_url)
    driver.implicitly_wait(20)
    email_field = driver.find_element(By.XPATH,CO.login_email_field_Xpath)
    password_field = driver.find_element(By.XPATH,CO.login_password_field_Xpath)
    send_button = driver.find_element(By.XPATH,CO.login_send_button_Xpath)
    fields = [email_field,password_field]
    for field,values in zip(fields,CO.user_details.values()):
        time.sleep(1.5)
        field.send_keys(values)
    send_button.click()
    time.sleep(5)
    obj = driver.switch_to.alert
    msg = obj.text
    print("Alert shows following message: " + msg)
    obj.accept()
    print(" Clicked on the OK Button in the Alert Window")
    action = ActionChains(driver)
    donat_add_exit = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[5]/div[1]/*[1]")
    action.move_to_element(donat_add_exit).click(donat_add_exit).perform()
    volunteers_button = driver.find_element(By.XPATH,"//header/div[1]/div[1]/div[4]/button[4]")
    volunteers_button.click()
    buttons_div = driver.find_element(By.XPATH,CO.volunteer_page_div)
    buttons = buttons_div.find_elements(By.TAG_NAME,"button")
    for i in buttons:
        i.click()
        time.sleep(2)
        exit_button = driver.find_element(By.XPATH,
                                          CO.volunteer_exit_btn)
        action.move_to_element(exit_button).click(exit_button)
        time.sleep(2)
    FU.success_finish("Volunteer link ")


def test_footer_btn():
    driver = DR.initroot()
    driver.get(CO.login_page_url)
    driver.implicitly_wait(20)
    email_field = driver.find_element(By.XPATH,CO.login_email_field_Xpath)
    password_field = driver.find_element(By.XPATH,CO.login_password_field_Xpath)
    send_button = driver.find_element(By.XPATH,CO.login_send_button_Xpath)
    fields = [email_field,password_field]
    for field,values in zip(fields,CO.user_details.values()):
        time.sleep(1.5)
        field.send_keys(values)
    send_button.click()
    time.sleep(5)
    obj = driver.switch_to.alert
    msg = obj.text
    print("Alert shows following message: " + msg)
    obj.accept()
    print(" Clicked on the OK Button in the Alert Window")
    action = ActionChains(driver)
    donat_add_exit = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[5]/div[1]/*[1]")
    action.move_to_element(donat_add_exit).click(donat_add_exit).perform()
    volunteers_button = driver.find_element(By.XPATH,"//header/div[1]/div[1]/div[4]/button[4]")
    volunteers_button.click()
    footer_btn = driver.find_element(By.CLASS_NAME,CO.footer_btn)
    footer_btn.click()
    time.sleep(3)
    con_footer_links_social = driver.find_element(By.XPATH,CO.social_footer_links)
    con_footer_links_nav = driver.find_element(By.XPATH,CO.footer_nav_links)
    social_footer = con_footer_links_social.find_elements(By.TAG_NAME,"a")
    nav_footer = con_footer_links_nav.find_elements(By.TAG_NAME,"li")
    for i in social_footer:
        i.click()
        time.sleep(2)
    for i in nav_footer:
        i.click()
        time.sleep(2)
    FU.success_finish("Footer_BTN links ")


def test_volunteer_page():
    test_navbar_links()
    test_hero_page_links()
    test_footer_btn()