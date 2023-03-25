from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains 



class Test_Sauce:
    def __init__(self):
        self.driver=webdriver.Chrome
        self.driver.maximize_window
        self.driver.get("https://www.saucedemo.com/")
    def test_invalid_login(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput= self.driver.find_element(By.ID, "user-name")
        userPwInput= self.driver.find_element(By.ID, "password")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys("1")
        userPwInput.send_keys("1")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text =="Epic sadface: You can only access '/inventory.html' when you are logged in"
        print(f"Test Sonucu: {testResult}")
        sleep(1)
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput= self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"password")))
        userPwInput= self.driver.find_element(By.ID, "password")
        #Action Chains
        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput, "standart_user")
        actions.send_keys_to_element(userPwInput, "secret_sauce")
        actions.perform()
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(2)
        



testClass= Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()