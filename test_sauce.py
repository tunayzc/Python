from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        userNameInput= driver.find_element(By.ID, "user-name")
        userPwInput= driver.find_element(By.ID, "password")
        sleep(1)
        userNameInput.send_keys("1")
        userPwInput.send_keys("1")
        sleep(1)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text =="HATALI GİRİŞ"
        print(f"Test Sonucu: {testResult}")
        sleep(1)
testClass= Test_Sauce()
testClass.test_invalid_login()
