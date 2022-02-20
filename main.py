from account import kullanici_adi,sifre,kullanici_id
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("C:/Users/alpca/OneDrive/Masaüstü/scraping-twitter-followers/chromedriver.exe")

url="https://twitter.com/login"

driver.maximize_window()
driver.get(url)

time.sleep(3)

un=driver.find_element_by_xpath("//input[@autocomplete='username']")
un.send_keys(kullanici_adi,Keys.ENTER)
time.sleep(2)
if(driver.find_element_by_xpath("//input[@autocomplete='on']")!=None ):
    au=driver.find_element_by_xpath("//input[@autocomplete='on']").send_keys(kullanici_id,Keys.ENTER)
time.sleep(2)
ps=driver.find_element_by_xpath("//input[@name='password']").send_keys(sifre,Keys.ENTER)
time.sleep(5)
driver.get("https://twitter.com/aysudlahmetoglu")
time.sleep(2)
if(driver.find_element_by_xpath("//*[@id='layers']/div/div[1]/div/div/div/div[2]/div[2]/div/div[1]")!=None):
    driver.refresh() #be sure to log in
    time.sleep(2)
driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/a").click()
time.sleep(5)
fl=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/section/div").find_elements_by_css_selector(".css-901oao.css-bfa6kz.r-9ilb82.r-18u37iz.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0")

last_height = driver.execute_script("return document.documentElement.scrollHeight")

# while True:
#         # Scroll down 'til "next load".
# driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

#         # Wait to load everything thus far.
#         time.sleep(2)

#         # Calculate new scroll height and compare with last scroll height.
#         new_height = driver.execute_script("return document.documentElement.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height

j=1
for i in fl:
    print(f"{j}-{i.text}")
    j+=1
