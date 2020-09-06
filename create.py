import sys
from selenium import webdriver

browser = webdriver.Chrome()

def create():
    project_name = str(sys.argv[1])

    browser.get("https://github.com/login")

    element = browser.find_element_by_id('login_field')
    element.send_keys('ShinyPotat')

    element = browser.find_elements_by_id('password')[0]
    element.send_keys('us43AF2P')

    element = browser.find_elements_by_xpath("//*[@id='login']/form/div[4]/input[9]")[0]
    element.click()

    browser.get("https://github.com/new")

    element = browser.find_elements_by_id('repository_name')[0]
    element.send_keys(project_name)

    element = browser.find_elements_by_xpath("//*[@id='new_repository']/div[4]/button")[0]
    element.submit()

if __name__ == "__main__":
    create()