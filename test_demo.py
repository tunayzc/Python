from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
#prefix == ön ek test
#postfix 
class Test_DemoClass:
    #---testten önce---
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    #---testten sonra---
    def teardown_method(self):
        self.driver.quit()

    # --- setup > test_demoFunc > teardown    
    def test_demoFunc(self):
        text= "hello"
        assert text == "hello"

    def test_demo2(self):
        assert True
    @pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","şifrem")])
    def test_invalid_login(self,username,password):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput= self.driver.find_element(By.ID, "user-name")
        userPwInput= self.driver.find_element(By.ID, "password")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys(username)
        userPwInput.send_keys(password)
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text =="Epic sadface: Username and password do not match any user in this service"
 
    
