import sys
import os
from selenium import webdriver

username = os.environ.get('GITUSERNAME')
pwd = os.environ.get('GITPASSWORD')

project_name = str(sys.argv[1])

browser = webdriver.Chrome()

def create():

    browser.get("https://github.com/login")

    element = browser.find_element_by_id('login_field')
    element.send_keys(username)

    element = browser.find_elements_by_id('password')[0]
    element.send_keys(pwd)

    element = browser.find_elements_by_xpath("//*[@id='login']/form/div[4]/input[9]")[0]
    element.click()

    browser.get("https://github.com/new")

    element = browser.find_elements_by_id('repository_name')[0]
    element.send_keys(project_name)

    element = browser.find_elements_by_xpath("//*[@id='new_repository']/div[4]/button")[0]
    element.submit()

    browser.quit()

if __name__ == "__main__":
    create()