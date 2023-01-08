import time
import pytest
import Page_Objects.MMT_Home_Page_Object
import Page_Objects.MMT_Search_Result_Page_Opject
from Utilities.Read_Config_Info import Read_Config as Rc
from selenium.webdriver.common.by import By
from Utilities.Custom_Logger import log_gen as logger
from Test_Cases.Base_Class import initialization
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Utilities.Excel_Utils import get_data_from_CSV
import pandas as pd
from Test_Cases.Base_Class import get_list

"""This is test case class and all the test case scripts included here"""

"""Access/Inherit all the base case class file objects """


class Test_Cases(initialization):
    """This is fixture function"""

    def setup_method(self):
        try:
            self.driver = initialization.driver

            self.lg = Page_Objects.MMT_Home_Page_Object.Home_page(self.driver, self.Explicit_wait, self.Implicit_wait)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(50)
            self.driver.set_script_timeout(30)
            self.driver.implicitly_wait(30)

            self.sr = Page_Objects.MMT_Search_Result_Page_Opject.search_result(self.driver, self.Explicit_wait,
                                                                               self.Implicit_wait)

        except Exception as ex:
            print("file read exception: ", ex)

    # ------------------------------------

    """This is Test case 1 code"""

    def test_TC001(self):
        try:
            """Test case TC001 include testing flow of searching flight"""
            # ------------------------------------
            self.driver.get(Rc.read_url())
            #assert self.driver.current_url == "https://www.makemytrip.com/flights/"
            self.lg.click_front_cover()
            self.lg.scroll()
            self.lg.click_flight_btn()
            self.lg.click_oneWay_option()
            self.lg.enter_from("Jaipur")
            self.lg.enter_to("Bhopal")
            self.lg.dep_date("25/01/2023")
            self.lg.travellers(2, 1, 2)
            self.lg.regular_btn()
            self.lg.search_btn()
            self.driver.back()
            # --------------------------------------
        except Exception as ex:
            print("test_TC001 exception generated ", ex)

    """Test Case TC002 code (parameterized) """
    @pytest.mark.parametrize('src, dest, adult, children, infant,  departure_date', get_list())
    def test_TC002(self, src, dest, adult, children, infant, departure_date):
        try:
            # self.driver.get(Rc.read_url())

            self.driver.switch_to.new_window()
            self.driver.get(Rc.read_url())
            #assert self.driver.current_url == "https://www.makemytrip.com/flights/"
            self.lg.click_front_cover()
            self.lg.scroll()
            self.lg.click_flight_btn()
            self.lg.click_oneWay_option()
            self.lg.enter_from(src)
            self.lg.enter_to(dest)
            self.lg.dep_date(departure_date)
            #self.lg.dep_date_1(departure_date)
            self.lg.travellers(adult, children, infant)
            self.lg.regular_btn()
            self.lg.search_btn()
            #self.sr.search_flight()
            self.sr.custom_range()
            self.sr.select_1_stop()
            self.sr.get_flight_data()
            self.driver.back()
        except Exception as ex:
            print("text_TC002 has encountered an exception:  ", ex)

    """Tear down method """
    def teardown_method(self):
        try:
            pass
           # self.driver.quit()
        except Exception as ex:
            print("Teardown method got as exception: ", ex)


"""**************************************** End *****************************************************"""