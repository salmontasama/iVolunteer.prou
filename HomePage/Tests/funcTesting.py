import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from Utilitis import constants as CO, driver as DR, func as FU


# def test_valid_login():
#     driver = DR.initroot()
#     driver.get(CO.login_page_url)
#     driver.implicitly_wait(20)
#     email_field = driver.find_element(By.XPATH,CO.login_email_field_Xpath)
#     password_field = driver.find_element(By.XPATH,CO.login_password_field_Xpath)
#     send_button = driver.find_element(By.XPATH,CO.login_send_button_Xpath)
#     fields = [email_field,password_field]
#     for field,values in zip(fields,CO.user_details.values()):
#         field.send_keys(values)
#     send_button.click()
#     time.sleep(5)
#     obj = driver.switch_to.alert
#     msg = obj.text
#     print("Alert shows following message: " + msg)
#     obj.accept()
#     print(" Clicked on the OK Button in the Alert Window")
#     print("Valid login "+CO.acomplish)


def test_link_navbar():
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
    navbar_links = nav_con.find_elements(By.TAG_NAME, "button")
    try:
        for i in navbar_links[1:]:
            i.click()
    except:
        FU.printing("The element can be clickd beacause the add interpted!", "red")
    FU.success_finish("Navbar link ")


def test_link_hero():
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
    arrow_right = driver.find_element(By.XPATH, CO.arrow_right_hero_home_page)
    img1 = driver.find_element(By.XPATH, CO.imgs[0])
    img2 = driver.find_element(By.XPATH, CO.imgs[1])
    img3 = driver.find_element(By.XPATH, CO.imgs[2])
    img4 = driver.find_element(By.XPATH, CO.imgs[3])
    img5 = driver.find_element(By.XPATH, CO.imgs[4])
    img6 = driver.find_element(By.XPATH, CO.imgs[5])
    imgs = [img1, img2, img3, img4, img5, img6]
    try:
        for i, j in zip(range(6), imgs):
            j.is_displayed()
            arrow_right.click()
            time.sleep(1)
    except IndexError:
        pass
    FU.success_finish("Hero link ")


def test_link_footer():
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
    buttom_div = driver.find_element(By.XPATH, CO.footer_div)
    buttons = buttom_div.find_elements(By.TAG_NAME, "button")
    try:
        buttons[0].click()
    except:
        FU.printing("The element can be clickd beacause the add interpted!", "red")
    driver.back()
    buttom_div = driver.find_element(By.XPATH, CO.footer_div)
    buttons = buttom_div.find_elements(By.TAG_NAME, "button")
    buttons[1].click()
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    print("Page title :")
    print(driver.title)
    driver.close()
    driver.switch_to.window(p)
    print("Current page title:")
    print(driver.title)
    time.sleep(0.5)
    FU.success_finish("Footer link ")


def test_footer_btn():
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
    footer_btn = driver.find_element(By.CLASS_NAME, CO.footer_btn)
    try:
        footer_btn.click()
    except:
        FU.printing("The element can be clickd beacause the add interpted!", "red")
    con_footer_links_social = driver.find_element(By.XPATH, CO.social_footer_links)
    con_footer_links_nav = driver.find_element(By.XPATH, CO.footer_nav_links)
    social_footer = con_footer_links_social.find_elements(By.TAG_NAME, "a")
    nav_footer = con_footer_links_nav.find_elements(By.TAG_NAME, "li")
    for i in social_footer:
        i.click()
        time.sleep(0.5)
    for i in nav_footer:
        i.click()
        time.sleep(0.5)
    FU.success_finish("Footer_BTN links ")


def test_func_home_page():
    test_link_navbar()
    test_link_hero()
    test_link_footer()
    test_footer_btn()
    FU.printing("All Functionalty Test in Home Page are complete!", "blue")
