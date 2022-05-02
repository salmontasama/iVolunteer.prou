import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from Utilitis import constants as CO, driver as DR, func as FU

def test_navbar_ui():
    driver = DR.initroot()
    driver.get(CO.login_page_url)
    driver.implicitly_wait(30)
    email_field = driver.find_element(By.XPATH,CO.login_email_field_Xpath)
    password_field = driver.find_element(By.XPATH,CO.login_password_field_Xpath)
    send_button = driver.find_element(By.XPATH,CO.login_send_button_Xpath)
    fields = [email_field,password_field]
    for field,values in zip(fields,CO.user_details.values()):
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
    donat_add_exit = driver.find_element(By.XPATH,CO.main_add_exit_btn)
    try:
        action.move_to_element(donat_add_exit).click(donat_add_exit).perform()
    except:
        FU.printing(f"The Add exit Button is out bouns not clickble!", "red")
    nav_con = driver.find_element(By.XPATH,CO.navbar_container)
    navbar_links = nav_con.find_elements(by=By.TAG_NAME,value="button")
    for button,text in zip(navbar_links[1:],CO.navbar_buttons_text):
        assert button.text == text.upper()
        FU.printing(f"expected:{text.upper()} = actual:{button.text}","black")
    WebDriverWait(driver,15).until(
        EC.visibility_of(navbar_links[0])
    )
    FU.success_finish("Navbar UI")



def test_hero_ui():
    driver = DR.initroot()
    driver.get(CO.login_page_url)
    driver.implicitly_wait(30)
    email_field = driver.find_element(By.XPATH,CO.login_email_field_Xpath)
    password_field = driver.find_element(By.XPATH,CO.login_password_field_Xpath)
    send_button = driver.find_element(By.XPATH,CO.login_send_button_Xpath)
    fields = [email_field,password_field]
    for field,values in zip(fields,CO.user_details.values()):
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
    donat_add_exit = driver.find_element(By.XPATH,CO.main_add_exit_btn)
    try:
        action.move_to_element(donat_add_exit).click(donat_add_exit).perform()
    except:
        FU.printing(f"The Add exit Button is out bouns not clickble!","red")
    main_contant = driver.find_element(By.XPATH,CO.main_contant_hero_home).text
    assert main_contant == CO.top_contant_hero_home
    arrow_right = driver.find_element(By.XPATH,CO.arrow_right_hero_home_page)
    img1 = driver.find_element(By.XPATH,CO.imgs[0])
    img2 = driver.find_element(By.XPATH,CO.imgs[1])
    img3 = driver.find_element(By.XPATH,CO.imgs[2])
    img4 = driver.find_element(By.XPATH,CO.imgs[3])
    img5 = driver.find_element(By.XPATH,CO.imgs[4])
    img6 = driver.find_element(By.XPATH, CO.imgs[5])
    imgs = [img1,img2,img3,img4,img5,img6]
    try:
        for i,j in zip(range(6),imgs):
            j.is_displayed()
            arrow_right.click()
            time.sleep(2)
    except IndexError:
        pass
    headline = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]").text
    FU.printing(f"Expected:{CO.hero_head_cards_home_text} = Actual:{headline}","black")
    assert headline == CO.hero_head_cards_home_text
    hero_top_container = driver.find_element(By.XPATH,CO.home_page_hero_top_container)
    hero_buttom_container = driver.find_element(By.XPATH,CO.home_page_hero_buttom_container)
    top_hero_paragraph = hero_top_container.find_elements(By.TAG_NAME,"section")
    buttom_hero_paragraph = hero_buttom_container.find_elements(By.TAG_NAME,"section")
    top_hero_imgs = hero_top_container.find_elements(By.TAG_NAME,"img")
    buttom_hero_imgs = hero_buttom_container.find_elements(By.TAG_NAME,"img")
    for top_img,buttom_img,top_p,buttom_p,y,j in zip(top_hero_imgs,buttom_hero_imgs,top_hero_paragraph,buttom_hero_paragraph,CO.home_page_hero_top_text,CO.home_page_hero_buttom_text):
        WebDriverWait(driver,8).until(
            EC.visibility_of(top_img)
        )
        WebDriverWait(driver,8).until(
            EC.visibility_of(buttom_img)
        )
        assert top_p.text == y
        assert buttom_p.text == j
    left_hero_col_buttom_text = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[4]/div[2]/section[1]").text
    right_hero_col_buttom_text = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[4]/div[1]/section[1]").text
    assert left_hero_col_buttom_text == CO.left_buttom_col_hero_text
    FU.printing(f"Expected:{CO.left_buttom_col_hero_text}\n\nActual:{left_hero_col_buttom_text}",'blue')
    assert right_hero_col_buttom_text == CO.right_top_col_hero_text
    FU.success_finish("Test Hero UI")






def test_footer_ui():
    driver = DR.initroot()
    driver.get(CO.login_page_url)
    driver.implicitly_wait(30)
    email_field = driver.find_element(By.XPATH,CO.login_email_field_Xpath)
    password_field = driver.find_element(By.XPATH,CO.login_password_field_Xpath)
    send_button = driver.find_element(By.XPATH,CO.login_send_button_Xpath)
    fields = [email_field,password_field]
    for field,values in zip(fields,CO.user_details.values()):
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
    donat_add_exit = driver.find_element(By.XPATH,CO.main_add_exit_btn)
    try:
        action.move_to_element(donat_add_exit).click(donat_add_exit).perform()
    except:
        FU.printing("The Add exit Button is out bouns not clickble!","red")
    footer_btn = driver.find_element(By.CLASS_NAME,CO.footer_btn)
    try:
        footer_btn.click()
    except:
        FU.printing("The element can be clickd beacause the add interpted!","red")
    con_footer_links_social = driver.find_element(By.XPATH, CO.social_footer_links)
    con_footer_links_nav = driver.find_element(By.XPATH, CO.footer_nav_links)
    social_footer = con_footer_links_social.find_elements(By.TAG_NAME,"a")
    nav_footer = con_footer_links_nav.find_elements(By.TAG_NAME,"li")
    for i,text in zip(nav_footer,CO.footer_nav_text):
        FU.printing(f"Expected:{i.get_attribute('innerText')} = Actual:{text}", "black")
        assert i.get_attribute("innerText") == text
    for i in social_footer:
        WebDriverWait(driver,8).until(
            EC.visibility_of(i)
        )
    copyright_text = driver.find_element(By.CLASS_NAME,"copyright").get_attribute("innerText")
    FU.printing(f"Expected:{CO.footer_copyright} = Actual:{copyright_text}","yellow")
    assert copyright_text == CO.footer_copyright
    FU.success_finish("Volunteer UI")



def test_ui_home_page():
    test_navbar_ui()
    test_hero_ui()
    test_footer_ui()
    FU.printing("All UI Tests in Home Page are complete!", "blue")