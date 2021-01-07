# This is a bot which automatically plays the lastest English lecture in my school's website.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Your credentials
roll_no = ""
password = ""

#Define webdriver object with filesystem path of chromedriver
path = "/home/sujay1844/MyFiles/Python/chromedriver"
driver = webdriver.Chrome(path)

#Go to Base login page
driver.get("https://base.resonance.ac.in/student/login.aspx")
driver.maximize_window()
time.sleep(2)

#Enter roll no.
username = driver.find_element_by_css_selector("#txt_roll_no")
username.send_keys(roll_no)
#Enter password
pwd = driver.find_element_by_css_selector("#txt_pwd")
pwd.send_keys(password)
#Click the login button
driver.find_element_by_css_selector("#btnLogin").click()

#Click on E-learning
driver.find_element_by_css_selector("#dvNonOL > div:nth-child(1) > div > a").click()

#Click on Live Sessions
driver.find_element_by_css_selector("#form1 > div.wrapper > div.main-panel > div.content > div > div > div > div.card-body > div > div:nth-child(1) > div > a").click()

#Click on the subjects dropdown and select english
driver.find_element_by_css_selector("#ddl_subject").click()
driver.find_element_by_css_selector("#ddl_subject > option:nth-child(7)").click()
time.sleep(2)

#Click on the first video
driver.find_element_by_css_selector("#grd_list_btn_play_0").click()
