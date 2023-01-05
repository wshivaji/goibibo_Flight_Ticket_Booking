import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class initialization:
    #driver = webdriver.Chrome()
    lg = object()
    sr = object()
    def Implicit_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def Explicit_wait(self, seconds, element):
        wait = WebDriverWait(self.driver, seconds)
        #ele = wait.until(expected_conditions.visibility_of_element_located(element))
        ele = wait.until(expected_conditions.element_to_be_clickable(element))


