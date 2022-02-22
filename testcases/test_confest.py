
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\DRIVERS\WIN\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver =driver #Cls aslında class yani
    yield
    driver.close()