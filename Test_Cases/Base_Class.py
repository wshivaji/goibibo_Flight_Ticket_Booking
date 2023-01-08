import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from Utilities.Excel_Utils import get_data_from_CSV
import pandas as pd


class initialization:

    """Initailize objects which will be used by all the test cases across framework"""
    lg = object()
    sr = object()
    df = pd.DataFrame()
    data = get_data_from_CSV()
    df = data.get_travellers()

    """set chrome driver and its setting"""
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as ex:
        print("init constructor in base class has an err: ", ex)

    """set implicit wait for all the web elements used across framework"""
    def Implicit_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    """set Explicit wait function to be used by all the web elements where ever it is needed"""
    def Explicit_wait(self, seconds, element):
        wait = WebDriverWait(self.driver, seconds)
        # ele = wait.until(expected_conditions.visibility_of_element_located(element))
        ele = wait.until(expected_conditions.element_to_be_clickable(element))


"""get the list of source, destination, adults, children and infant information from test data file"""


def get_list():
    df = initialization.df
    print("X: ", df)
    shape = df.shape
    row = shape[0]
    column = shape[1]
    print("df length: ", shape, " Rows: ", row, " Columns: ", column)
    for i in range(row):
        print("Source: ", df.iloc[i, 1], " Destination: ", df.iloc[i, 2])
    src = [i for i in df["source"]]
    dest = [i for i in df["destination"]]
    adult = [i for i in df["adults"]]
    children = [i for i in df["children"]]
    infant = [i for i in df["infant"]]
    print(src)
    print(dest)
    list_zip = zip(src, dest, adult, children, infant)
    city_list = list(list_zip)
    print(city_list)
    return city_list


"""****************************************** End ************************************************"""