import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Utilitis import constants as CO, driver as DR, func as FU


def test_navbar_ui():
    driver = DR.initroot()
    driver.get(CO.login_page_url)
    driver.implicitly_wait(30)
    email_field = driver.find_element(By.XPATH, CO.login_email_field_Xpath)
    password_field = driver.find_element(By.XPATH, CO.login_password_field_Xpath)
    send_button = driver.find_element(By.XPATH, CO.login_send_button_Xpath)
    fields = [email_field, password_field]
    for field, values in zip(fields, CO.user_details.values()):
        time.sleep(1)
        field.send_keys(values)
    send_button.click()
    time.sleep(0.5)
    obj = driver.switch_to.alert
    msg = obj.text
    print("Alert shows following message: " + msg)
    obj.accept()
    print(" Clicked on the OK Button in the Alert Window")
    action = ActionChains(driver)
    donat_add_exit = driver.find_element(By.XPATH, CO.main_add_exit_btn)
    try:
        action.move_to_element(donat_add_exit).click(donat_add_exit).perform()
    except:
        FU.printing(f"The Add exit Button is out bouns not clickble!", "red")
    nav_con = driver.find_element(By.XPATH, CO.navbar_container)
    navbar_links = nav_con.find_elements(by=By.TAG_NAME, value="button")
    for button, text in zip(navbar_links[1:], CO.navbar_buttons_text):
        assert button.text == text.upper()
        FU.printing(f"expected:{text.upper()} = actual:{button.text}", "black")
    WebDriverWait(driver, 15).until(
        EC.visibility_of(navbar_links[0])
    )
    FU.success_finish("Navbar UI")


def test_hero_ui():
    driver = DR.initroot()
    driver.get(CO.login_page_url)
    driver.implicitly_wait(30)
    email_field = driver.find_element(By.XPATH, CO.login_email_field_Xpath)
    password_field = driver.find_element(By.XPATH, CO.login_password_field_Xpath)
    send_button = driver.find_element(By.XPATH, CO.login_send_button_Xpath)
    fields = [email_field, password_field]
    for field, values in zip(fields, CO.user_details.values()):
        time.sleep(1)
        field.send_keys(values)
    send_button.click()
    time.sleep(0.5)
    obj = driver.switch_to.alert
    msg = obj.text
    print("Alert shows following message: " + msg)
    obj.accept()
    print(" Clicked on the OK Button in the Alert Window")
    action = ActionChains(driver)
    donat_add_exit = driver.find_element(By.XPATH, CO.main_add_exit_btn)
    try:
        action.move_to_element(donat_add_exit).click(donat_add_exit).perform()
    except:
        FU.printing("The Add exit Button is out bouns not clickble!", "red")
    volunteers_button = driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[4]/button[4]")
    try:
        volunteers_button.click()
    except:
        FU.printing("The element can be clickd beacause the add interpted!", "red")
    buttons_div = driver.find_element(By.XPATH, CO.volunteer_page_div)
    buttons = buttons_div.find_elements(By.TAG_NAME, "button")
    for i, button, header, paragraph in zip(range(1, 13), buttons, CO.h1_text.keys(), CO.h1_text.values()):
        button.click()
        y = driver.find_element(By.XPATH,
                                f"//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/section[{i}]/div[2]/div[1]/h1[1]").text
        x = driver.find_element(By.XPATH,
                                f"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/section[{i}]/div[2]/div[1]/p[1]").text
        assert y == header
        assert x == paragraph
    time.sleep(0.5)
    FU.success_finish("Hero UI")


def test_footer_ui():
    driver = DR.initroot()
    driver.get(CO.login_page_url)
    driver.implicitly_wait(30)
    email_field = driver.find_element(By.XPATH, CO.login_email_field_Xpath)
    password_field = driver.find_element(By.XPATH, CO.login_password_field_Xpath)
    send_button = driver.find_element(By.XPATH, CO.login_send_button_Xpath)
    fields = [email_field, password_field]
    for field, values in zip(fields, CO.user_details.values()):
        time.sleep(1)
        field.send_keys(values)
    send_button.click()
    time.sleep(0.5)
    obj = driver.switch_to.alert
    msg = obj.text
    print("Alert shows following message: " + msg)
    obj.accept()
    print(" Clicked on the OK Button in the Alert Window")
    action = ActionChains(driver)
    donat_add_exit = driver.find_element(By.XPATH, CO.main_add_exit_btn)
    try:
        action.move_to_element(donat_add_exit).click(donat_add_exit).perform()
    except:
        FU.printing("The Add exit Button is out bouns not clickble!", "red")
    footer_btn = driver.find_element(By.CLASS_NAME, CO.footer_btn)
    try:
        footer_btn.click()
    except:
        FU.printing("The element can be clickd beacause the add interpted!", "red")
    con_footer_links_social = driver.find_element(By.XPATH, CO.social_footer_links)
    con_footer_links_nav = driver.find_element(By.XPATH, CO.footer_nav_links)
    social_footer = con_footer_links_social.find_elements(By.TAG_NAME, "a")
    nav_footer = con_footer_links_nav.find_elements(By.TAG_NAME, "li")
    for i, text in zip(nav_footer, CO.footer_nav_text):
        FU.printing(f"Expected:{i.get_attribute('innerText')} = Actual:{text}", "black")
        assert i.get_attribute("innerText") == text
    for i in social_footer:
        WebDriverWait(driver, 8).until(
            EC.visibility_of(i)
        )
    copyright_text = driver.find_element(By.CLASS_NAME, "copyright").get_attribute("innerText")
    FU.printing(f"Expected:{CO.footer_copyright} = Actual:{copyright_text}", "yellow")
    assert copyright_text == CO.footer_copyright
    FU.success_finish("Volunteer UI")


def test_ui_volunteer_page():
    test_navbar_ui()
    test_hero_ui()
    test_footer_ui()
    FU.printing("All UI Tests in Volunteer Page are complete!", "blue")
