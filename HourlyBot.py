import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random



driver = webdriver.Chrome(executable_path='H:\Descargas\chromedriver.exe',) ## Replace H:\Descargas\chromedriver.exe with the path where you have chromedriver.exe 



images =  ["1", "2", "3"] ## Replace 1, 2, 3, etc with links to the images with t.co links separated by commas. 
## open twitter
driver.get('https://twitter.com/i/flow/login')

time.sleep(7)
## Log in
textbox = driver.find_element(By.XPATH, '//input[@autocorrect="on"]')

textbox.send_keys("USERNAME")  ## Replace USERNAME with your account's username

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Siguiente']"))).click() ## If your twitter language is not spanish, replace Siguiente with the equivalent in your language. It's the button above "Forgot my password"
time.sleep(1)

password = driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
password.send_keys("PASSWORD") ## Replace PASSWORD with your account's password 
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Iniciar sesión']"))).click() ## If your twitter language is not spanish, replace Iniciar sesión with the equivalent in your language. It's the log in button.
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"]')))
## Post tweets
while True:
 t = time.localtime()
 current_time = time.strftime("%H:%M:%S", t)
 tweet = driver.find_element(By.XPATH, '//div[@contenteditable="true"]')

 tweet.send_keys(random.choice(images))
 WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]'))).click()
 driver.refresh()
 print("Tweeted at " + current_time)
 time.sleep(3600)
 
