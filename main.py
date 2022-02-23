from unittest.util import strclass
from account import username, password, user_id
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from contextlib import nullcontext
import io

def scrapping(profile):
    driver = webdriver.Chrome(
        "./chromedriver")

    # Login
    url = "https://twitter.com/login"

    driver.maximize_window()
    driver.get(url)

    time.sleep(3)

    un = driver.find_element_by_xpath("//input[@autocomplete='username']")
    un.send_keys(username, Keys.ENTER)
    time.sleep(2)

    try:
        driver.find_element_by_xpath(
            "//input[@autocomplete='on']").send_keys(user_id, Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath(
            "//input[@name='password']").send_keys(password, Keys.ENTER)
    except:
        ps = driver.find_element_by_xpath(
            "//input[@name='password']").send_keys(password, Keys.ENTER)
    time.sleep(5)

    # Profile
    driver.get(f"{profile}")
    time.sleep(2)
    if(driver.find_element_by_xpath("//*[@id='layers']/div/div[1]/div/div/div/div[2]/div[2]/div/div[1]") != None):
        # be sure to log in
        driver.refresh()
        time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/a").click()
    time.sleep(3)
    # Scraping
    flist = []
    fl = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/section/div").find_elements_by_css_selector(
        ".css-901oao.css-bfa6kz.r-9ilb82.r-18u37iz.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0")
    for i in fl:
        flist.append(i.text)
    time.sleep(2)


    last_height = driver.execute_script(
        "return document.documentElement.scrollHeight")

    while True:
        # Scroll down 'til "next load".
        driver.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)
        fl = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/section/div").find_elements_by_css_selector(
            ".css-901oao.css-bfa6kz.r-9ilb82.r-18u37iz.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0")
        # Wait to load everything thus far.
        for i in fl:
            if i.text not in flist:
                flist.append(i.text)
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script(
            "return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    j = 1
    for i in flist:
        print(f"{j}-{i}")
        j += 1
        
if __name__=="__main__":
    scrapping(sys.argv[1])
