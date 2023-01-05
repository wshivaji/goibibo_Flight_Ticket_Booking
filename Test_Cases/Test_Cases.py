import time
import pytest
import Page_Objects.MMT_Home_Page_Object
import Page_Objects.MMT_Search_Result_Page_Opject
from Utilities.Read_Config_Info import Read_Config as Rc
from Utilities.Custom_Logger import log_gen as logger
from Test_Cases.Base_Class import initialization
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class Test_Cases(initialization):

    def test_TC001(self):
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(options=chrome_options)

            #------------------------------------

            self.lg = Page_Objects.MMT_Home_Page_Object.login(self.driver, self.Explicit_wait, self.Implicit_wait)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(50)
            self.driver.set_script_timeout(30)
            self.driver.implicitly_wait(30)
            self.driver.get(Rc.read_url())

            self.sr = Page_Objects.MMT_Search_Result_Page_Opject.search_result(self.driver, self.Explicit_wait, self.Implicit_wait)


            #------------------------------------

            self.lg.click_front_cover()
            self.lg.scroll()
            self.lg.click_flight_btn()
            self.lg.click_oneWay_option()
            self.lg.enter_from("Aurangabad")
            self.lg.enter_to("mumbai")
            self.lg.dep_date()
            self.lg.travellers()
            self.lg.regular_btn()
            self.lg.search_btn()

            self.sr.search_flight()
            self.sr.custom_range()
            self.sr.select_1_stop()
            self.sr.get_flight_data()

        except Exception as ex:
            print("test_TC001 exception generated ", ex)
