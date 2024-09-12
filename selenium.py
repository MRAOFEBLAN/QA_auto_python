
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

try:
    
    driver.get("https://www.saucedemo.com/")
    
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    
    time.sleep(2)  

    driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    
    assert "Sauce Labs Backpack" in driver.page_source
    
    
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    
    
    driver.find_element(By.ID, "finish").click()
    
    
    assert "THANK YOU FOR YOUR ORDER" in driver.page_source

finally:
    
    time.sleep(5)  
    driver.quit()