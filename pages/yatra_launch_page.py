import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from testcases.test_confest import setup


class LaunchPage():
    def __init__(self,driver):
        self.driver = driver

    #Locators boylece ana sayfada bir daha kullanacak
    DEPART_FROM_FIELD =  "//input[@id='BE_flight_origin_city']"

    def getDepartFromField(self):
        return self.driver.find_element(By.XPATH,self.DEPART_FROM_FIELD)


    def departfrom(self,departlocation):
        self.getDepartFromField().click()

        time.sleep(2)
        self.getDepartFromField().clear()
        self.getDepartFromField().send_keys(departlocation)
        time.sleep(2)
        self.getDepartFromField().send_keys(Keys.ENTER)
        time.sleep(2)

    def goingto(self,goingtolocation):
        going_to = self.driver.depart_from = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys(goingtolocation)
        time.sleep(4)
        search_result = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for result in search_result:
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(3)
                break
    def selectdate(self, selectiondate):
        origin = self.driver.find_element_by_id("BE_flight_origin_date")
        origin.click()
        departure_dates = self.driver.find_elements_by_xpath(
            "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in departure_dates:
            if date.get_attribute("data-date") == (selectiondate):
                date.click()
                break
        arrival_date = self.driver.find_element_by_xpath("//label[@for='BE_flight_arrival_date']")
        arrival_date.click()
        return_dates = self.driver.find_elements_by_xpath("//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in return_dates:
            if date.get_attribute("data-date") == "15/05/2022":
                date.click()
                break

    def searchclick(self):
        search_result = self.driver.find_element_by_id("BE_flight_flsearch_btn")
        search_result.click()
