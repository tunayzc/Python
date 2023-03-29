from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import  WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class test_homework4:
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.Path=str(date.today())
        Path(self.Path).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    def inputUserName(self,userName):
        userNameInput = self.driver.find_element(By.ID ,"user-name")
        self.waitForElementVisible(By.ID ,"user-name")
        userNameInput.send_keys(userName)
    def inputPassword(self,password):
        userPwInput = self.driver.find_element(By.ID ,"password")
        self.waitForElementVisible(By.ID ,"password")
        userPwInput.send_keys(password)
    def loginButton(self):
        self.waitForElementVisible(By.ID, "login-button")
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
    def validLogin(self):
        self.inputUserName("standart_user")
        self.inputPassword("secret_sauce")
        self.loginButton()
   
   ##########################################################################################
   
    def null_login(self):
        self.inputUserName("")
        self.inputPassword("")
        self.loginButton()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3" )
        assert errorMessage.text == "Epic sadface: Username is required"
        

    def null_password_login(self):
        self.inputUserName("standart_user")
        self.inputPassword("")
        self.loginButton()
        errorMessage= self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Password is required"
        
        sleep(2)
    
    def forbidden_user_login(self):
        self.inputUserName("locked_out_user")
        self.inputPassword("secret_sauce")
        self.loginButton()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
      
    
    def error_showcase(self):
        self.inputUserName("")
        self.inputPassword("")
        self.loginButton()
        
        errorButton= self.driver.find_element(By.CLASS_NAME, "error-button")
        errorButton.click()
        errorIcons = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        assert len(errorIcons)==0
    
    def true_login(self):
        self.inputUserName("standart_user")
        self.inputPassword("secret_sauce")
        self.loginButton()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    def qty_item(self):
        test_homework4.true_login(self)
        self.waitForElementVisible(By.CLASS_NAME, "inventory_item")
        currentItems = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(currentItems) == 6

    def add_cart(self):
        test_homework4.validLogin(self)
        self.waitForElementVisible(By.CLASS_NAME, "inventory_item")
        addCartButton = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addCartButton.click()
        
    def remove_cart(self):
        test_homework4.validLogin(self)
        self.waitForElementVisible(By.CLASS_NAME, "inventory_item")
        removeCartButton = self.driver.find_element(By.ID,"remove-sauce-labs-backpack")
        removeCartButton.click()

    def goToShoppingCart(self):
        test_homework4.validLogin(self)
        self.waitForElementVisible(By.CLASS_NAME, "inventory_item")
        toShoppingCart = self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        toShoppingCart.click()
        pageLoaded=self.driver.current_url=="https://www.saucedemo.com/cart.html"
        assert pageLoaded==True
        
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("performance_glitch_user","secret_sauce"),("problem_user","secret_sauce")])
    def test_valid_users(self,username,password):
        self.inputUserName(username)
        self.inputPassword(password)
        self.loginButton()

        ifPageLoaded=self.driver.current_url=="https://www.saucedemo.com/inventory.html"
        assert (ifPageLoaded==True)
        self.driver.save_screenshot(f"{self.folderPath}/test_valid_users.png")


    



        
    