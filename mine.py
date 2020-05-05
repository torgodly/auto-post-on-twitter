from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox(executable_path='C:\webdriver/geckodriver.exe')

#dirver configtion
#driver = webdriver.Chrome()


driver.get('https://twitter.com/login')


def login(user, pwd):

         #input scion in login page
         email = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
         password = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')


         # Login info
         email.send_keys(user)
         password.send_keys(pwd)
         #login botten
         driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()

         driver.get('https://twitter.com/home')
         time.sleep(2)

         tweet_section = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
         action = ActionChains(driver)
         action.move_to_element(tweet_section).click()
         action.send_keys('hello homeww word!!!')
         time.sleep(2)
         action.perform()

         tweet_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
         tweet_btn.click()
         time.sleep(3)

         print(user, 'yes')

         driver.get("https://twitter.com/logout")
         time.sleep(2)
         driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div").click()

user_names = open("users.txt").read()
passwords = open("pwd.txt").read()

user_names_list = user_names.split()
passwords_list = passwords.split()

zip = zip(user_names_list,passwords_list)

for i in range(0, 10):
    for usr,pas in zip:
        login(usr, pas)
        time.sleep(2)
        driver.get("https://twitter.com/login")

# TODO figer out way to loop the class