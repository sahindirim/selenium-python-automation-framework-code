import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from testcases.test_confest import setup
from pages.yatra_launch_page import LaunchPage

@pytest.mark.usefixtures('setup')
class TestSearchFlight():
    def test_search_flight(self,setup):
        lp = LaunchPage(self.driver)
        lp.departfrom("istanbul")
        lp.goingto("New York")
        lp.selectdate("04/03/2022")
        lp.searchclick()

