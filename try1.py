from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
class Test:
    driver=webdriver.Chrome()
    website = "https://www.saucedemo.com"
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    def inputUserName(self,userName):
        userNameInput = self.driver.find_element((By.ID ,"user-name"))
        self.waitForElementVisible(By.ID ,"user-name")
        userNameInput.send_keys(userName)
    def inputPassword(self,password):
        userPwInput = self.driver.find_element(By.ID ,"password")
        self.waitForElementVisible((By.ID ,"password"))
        userPwInput.send_keys(password)
    def loginButton(self):
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
    def null_login(self):
        self.inputUserName("")
        self.inputPassword("")
        self.loginButton()
        errorMessage= self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Password is required"
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("performance_glitch_user","secret_sauce"),("problem_user","secret_sauce")])
    def test_valid_users(self,username,password):
        self.inputUserName(username)
        self.inputPassword(password)
        self.loginButton()

       
test = Test()
test.null_login()