from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
sleep(1)
driver.maximize_window()
input = driver.find_element(By.NAME, "q")
input.send_keys("kodlamaio")
sleep(1)
searchButton = driver.find_element(By.NAME, "btnK")
searchButton.click()
sleep(1)
firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
sleep(1)
firstResult.click()
sleep(1)
listOfCourses = driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"Kodlamaio siteside şu anda {len(listOfCourses)} adet kurs var.")
#input()
while True:
    continue
#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a