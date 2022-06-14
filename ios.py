from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "deviceName":"iPhone 12",
    "platformName":"ios",
    "platformVersion":"14",
    "isRealMobile":True,
    "app":"lt://", 
    "build":"Python Vanilla iOS",
    "name":"Sample Test - Python",
    "network":True,
    "visual":True,
    "video":True
}

def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        username = "username" #Enter LT username here if environment variables have not been added
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        accesskey = "accesskey" #Enter LT accesskey here if environment variables have not been added
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://"+username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")
        time.sleep(3)
        colorElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,"color")))
        colorElement.click()
        textElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,"Text")))
        textElement.click()

        #Close the application
        driver.close_app()

        #Open the application
        driver.open_app()

        toastElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,"toast")))
        toastElement.click()
        notification = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,"notification")))
        notification.click()

        driver.quit()
    except:
        driver.quit()

startingTest()
