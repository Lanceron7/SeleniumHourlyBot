import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import concurrent.futures
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random



driver = webdriver.Chrome(executable_path='H:\Descargas\chromedriver.exe',) 


testing = ["test1" , "test2" , "test3" ,"test4" , "test5"]
images =  ["https://t.co/h3S73V5Luu", "https://t.co/OImz8U85eo", "https://t.co/KzA7pSFUZx", "https://t.co/AN2jbLpesw", "https://t.co/NpoHsKpOzN", "https://t.co/whxcWEoX6G", "https://t.co/f1Ci4KnltQ", "https://t.co/aGLxT18iXD", "https://t.co/GfcdAyFy5h", "https://t.co/MG61XKjRk5", "https://t.co/M94NhnuSGI", "https://t.co/8MzdopQn6O", "https://t.co/jVxuaxik1j", "https://t.co/gBe9KsuFCT", "https://t.co/BoOvgl6CV1", "https://t.co/wNKPs9urcP", "https://t.co/lnkGCxfuU8", "https://t.co/5zdmGmMBvk", "https://t.co/smYH7n7U5O", "https://t.co/UlBCw2wa8D", "https://t.co/eW4KTU9UFA", "https://t.co/jIbVjM6ZKn", "https://t.co/o8Fk4eJGCd", "https://t.co/4EUx0Cs6En", "https://t.co/phz4tuRRjQ", "https://t.co/opS8y0l8fp", "https://t.co/g0IbiO895U", "https://t.co/F6B4fV33B2", "https://t.co/u3weVYA7nd", "https://t.co/AZ3fvscK0L", "https://t.co/24XeyPZTe8", "https://t.co/Sx9kb1bLhl", "https://t.co/SvB1PLDuln", "https://t.co/Y3tC4Mdi8R", "https://t.co/1JI9vFX2WG", "https://t.co/FX4uXiR8Pd", "https://t.co/I8qaxLy2hH", "https://t.co/z0xePN4Rxg", "https://t.co/kBmPiw0gnT", "https://t.co/IJyjMTzQkK", "https://t.co/REvIXwnBYx", "https://t.co/KPZRWeza87", "https://t.co/sJgVK09mR7", "https://t.co/dNFpfkX1lM", "https://t.co/KYXcc0RCJh", "https://t.co/0YjnZXzZbo", "https://t.co/eWYOfrY3qx", "https://t.co/8v8yJgydiY", "https://t.co/pFs3aryQ7r", "https://t.co/r0IBoLbsT2", "https://t.co/sIlHdZNodL", "https://t.co/LuHhzH21J8", "https://t.co/9plvxFPWyD", "https://t.co/CPUuK1cELA", "https://t.co/5HYcTBxen0", "https://t.co/fRuSJmz5qn", " https://t.co/suzLD8bKfC", "https://t.co/bJ3V1iebUd", "https://t.co/5l2NTMQH0z", "https://t.co/t46vkVNIyx", "https://t.co/Kj0QGVxg4d", "https://t.co/Y6EOKAL1uW", "https://t.co/ID5zZconb1", "https://t.co/RiwlOVxdwR", "https://t.co/PGrufLRnVg", "https://t.co/Es8YwxizRY", "https://t.co/zgX7ISFJce", "https://t.co/xQDNIOKoUm", "https://t.co/eAzHjSS5Bd", "https://t.co/m273ZKJ7Mf", "https://t.co/kHVaGU6J3D", "https://t.co/wzbAV55PoZ", "https://t.co/IzQHVnZtLS", "https://t.co/eXG34tUHl4", "https://t.co/0eynZkLJso", "https://t.co/19Nw06ype8", "https://t.co/uGdyyneJHv", "https://t.co/ClAlREqhP2"]
## open twitter
driver.get('https://twitter.com/i/flow/login')

time.sleep(7)
## Log in
textbox = driver.find_element(By.XPATH, '//input[@autocorrect="on"]')

textbox.send_keys("HourlyAryu")  

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Siguiente']"))).click()
time.sleep(1)

password = driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
password.send_keys("Luther2346")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Iniciar sesión']"))).click()
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
 