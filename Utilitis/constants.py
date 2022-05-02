from colorama import Fore
from colorama import Style
base_url = 'https://ivolunteer-app.herokuapp.com/'
driver_executable_path = 'C:/Users/Dell/Desktop/AutoMation Subjects/Selenium/WebDriver(Browsers)/Chrome/chromedriver.exe'
volunteer_button_login = "//button[contains(text(),'Go-Volunteer!')]"
login_page_url = "https://ivolunteer-app.herokuapp.com/login"
login_email_field_Xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
login_password_field_Xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]"
user_details = {"email":"Morlove123@gmail.com","password":123456789}
login_send_button_Xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]"
acomplish = Fore.LIGHTGREEN_EX+"Test Finish!"+Style.RESET_ALL
slider_section_home_page = "//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]"
imgs = ["//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[1]","//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[2]","//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[3]","//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[4]","//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[5]","//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[6]"]
footer_div = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[4]"
proveed_assistance_url = "https://ivolunteer-app.herokuapp.com/addVolPost"
footer_btn = "footer-btn"
social_footer_links = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/footer[1]/div[1]"
footer_nav_links = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/footer[1]/ul[1]"
volunteer_page_div = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]"
volunteer_page_url = "https://ivolunteer-app.herokuapp.com/volPosts"

volunters_h1 = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/h1[1]"
volunters_p = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/p[1]"
h1_text = {"Asaf Subai":"Hello everyone my name is Assaf and i'm 28 years old, I'm passionate about animals, I have three dogs, and I'm a street artist. After starting to draw when I was 5 years old, I knew very soon that this is what I want to do. I would love to share some of the knowledge I have with others.",
           "Ester Belous":"Hello everyone my name is Ester and i'm 41 years old, I'm a lawyer and I have two children a son and a daughter of 8 years old twins I really like nature and travel.It would be an honor for me to give a Lecture for Women on Female Empowerment",
           "Eyal Lasker":"Hello everyone my name is Eyal and i'm 35 years old, I'm from spain and I came here for a roots trip and I would love to volunteer to distribute food to the elderly. I have my own farm in Spain and I am good with animals.",
           "Lisa Megan":"Hello everyone my name is Lisa and i'm 29 years old, I'm the CEO of a cyber company I believe that volunteering in the community contributes a lot to improving life I have been volunteering for five years.",
           "Ofek Ziv":"I'm Ofek , and I'm a clown by profession and I like to make people laugh. In the past I volunteered in the pediatric ward at a hospital and I would love to do it again",
           "Amir Ben Natan":"Hello I'm Amir , and I'm a I have been a professional photographer for 15 years. I would love to conduct a photography workshop for people who want to know how to photograph better to document their loved ones",
           "Vered Mangisto":"Hello I'm Vered ,Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quasi cumque animi voluptatum ab deleniti, molestiae modi saepe vero minima labore, esse fugiat perspiciatis eaque, est maiores eveniet.",
           "Elad Haziza":"Hello everyone my name is Elad Haziza and i'm 28 years old, I'm passionate about animals, I have three dogs, and I'm a street artist. After starting to draw when I was 5 years old, I knew very soon that this is what I want to do. I would love to share some of the knowledge I have with others.",
           "Ofek Lev":"Hello everyone my name is Ofek Levi and i'm 58 years old, I'm passionate about animals, I have three dogs, and I'm a street artist. After starting to draw when I was 5 years old, I knew very soon that this is what I want to do. I would love to share some of the knowledge I have with others.",
           "Tomer Hindi":"Hello everyone my name is Tomer Hindi and i'm 41 years old, I'm passionate about animals, I have three dogs, and I'm a street artist. After starting to draw when I was 5 years old, I knew very soon that this is what I want to do. I would love to share some of the knowledge I have with others.",
           "Bar Musan":"Hello everyone my name is Bar Musan and i'm 36 years old, I'm passionate about animals, I have three dogs, and I'm a street artist. After starting to draw when I was 5 years old, I knew very soon that this is what I want to do. I would love to share some of the knowledge I have with others.",
           "Mishel Shabyev":"Hello everyone my name is Mishel Shabyev and i'm 31 years old, I'm passionate about animals, I have three dogs, and I'm a street artist. After starting to draw when I was 5 years old, I knew very soon that this is what I want to do. I would love to share some of the knowledge I have with others."}


volunteer_exit_btn = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/*[1]"

main_add_exit_btn = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[5]/div[1]/*[1]"

navbar_container = "//header[1]/div[1]/div[1]/div[4]"

navbar_buttons_text = ["Provide assistance", "Seeking assistance", "volunteers", "need volunteers"]

home_button_icon = "//header/div[1]/div[1]/div[4]/button[1]/i[1]"

footer_nav_text = ["Home", "Services", "About", "Terms", "Privacy Policy"]

footer_copyright = "i Volunteer © 2022"


top_contant_hero_home = "Who we are\niVolunteer is the leading organization in the field of volunteering in Israel, specializing in matching volunteers between people\nOur Background Connects people who want to volunteer with associations and organizations that need volunteers, using a unique search engine that allows you to find personalized volunteering. On our website you can choose a volunteer that interests you according to your location in the country, and according to an area that interests you.\nOur Vision We believe everyone has the power to do good, which is why we specialize in connecting individuals to causes and organizations they’re passionate about, in order to help them to make a difference in the world.\nWhat We Do At iVolunteer, we connect people who are interested in volunteering in Israel to and people looking for volunteers across the country. we offer volunteering opportunities, Placements are according to the volunteer’s preferences iVolunteer is the intermediate between you, and the volunteer."

main_contant_hero_home = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]"


hero_head_cards_home_text = "Success Story"

home_page_hero_top_container = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[3]/div[1]"

home_page_hero_top_text = ["I would like to express my gratitude to Daniel Dahan, who donated food baskets for Passover for the needy. He also provided a regional distribution.","We would like to express our appreciation to Lisa Megan and her staff for assisting with agricultural work and tree planting in the Carmel Forest.","We would like to express our appreciation to The lovely Anat gave a two-hour lecture on finance and managed to pass on her vast knowledge to tech career students."]


home_page_hero_buttom_text = ["Thanks to Adar Avraham and Eyal Levy who donated a buffet, a coffee table, a kitchen stand, and a wall mirror for a young woman who was at risk. You helped her a lot! Thank you very much!","Many thanks to the Astrenzka workers and their children, who volunteered to help establish seating areas and upgrade the yard at the Beit Tef boarding school in honor of Hanukkah. Lovely!","There are no words to thank Omri for the above and beyond he did in recruiting computers, you brought him to Gedera and installed it together with his friend, you took care of all the requests in Gedera and we are thrilled by your work. Thanks!"]


home_page_hero_buttom_container = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[3]/div[2]"


home_page_hero_container = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[4]/div[1]/section[1]"

right_top_col_hero_text = "Doing good\nhas never been easier\nVolunteer as a team:\nConnect to your mission by embracing social responsibility.\nCLICK TO VOLUNTEER"


left_buttom_col_hero_text = "The change is in your\nhands\nContribute to the missions you love. Make a difference\nwith your team or on your own, remotely or on-site.\nCLICK TO DONATE"


arrow_right_hero_home_page = "//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/*[1]"