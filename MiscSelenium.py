from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
import time

driver = webdriver.Chrome()
# navigate to the download page
driver.get("http://45.76.1.18:5000/")

try:
    #verify the Login page button exist and click it
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Login page')]"))
    )
    driver.find_element_by_xpath("//a[contains(text(),'Login page')]").click()

    #type in username and password
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
    )
    driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("admin")

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
    )
    driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("admin1234")

    #click login button
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Login']"))
    )
    driver.find_element_by_xpath("//input[@value='Login']").click()

    #TO-DO: for some reason the locator doesnt work. also tried //pre[contains(text(), 'Hello admin!']
    # greeting = driver.find_element_by_xpath("//pre[@xpath='1']")
    # assert "Hello admin!" in greeting

    #click the items page
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Items page')]"))
    )
    driver.find_element_by_xpath("//a[contains(text(),'Items page')]").click()

    # select the 2nd download item
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//a[contains(text(),'Download item')])[2]"))
    )
    driver.find_element_by_xpath("(//a[contains(text(),'Download item')])[2]").click()

    is_file = os.path.isfile("/Users/kchen/Downloads/item.txt")
    counter = 0
    while not is_file and counter < 5:
        time.sleep(1)
        counter = counter + 1
        is_file = os.path.isfile("/Users/kchen/Downloads/item.txt")

    with open("/Users/kchen/Downloads/item.txt") as file:
            text = file.readline()
            print(text)

    driver.back()

    # click logout button
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Logout')]"))
    )
    driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()

    #verify we are back to the login page
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Login page')]"))
    )
except Exception as ex:
    print(ex)
finally:
    driver.quit()