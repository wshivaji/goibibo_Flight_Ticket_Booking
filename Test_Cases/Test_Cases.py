import time
import pytest
import Page_Objects.goibibo_Home_Page_Object
from Utilities.Read_Config_Info import Read_Config as Rc
from Utilities.Custom_Logger import log_gen as logger
from Test_Cases.Base_Class import initialization


class Test_Cases(initialization):

    def test_TC001(self):
        try:
            self.lg = Page_Objects.goibibo_Home_Page_Object.login(self.driver, self.Explicit_wait, self.Implicit_wait)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            self.driver.set_script_timeout(30)
            self.driver.get(Rc.read_url())
            #self.lg.click_flight_btn()
            #self.lg.click_oneWay_option()
            self.lg.enter_from("aurangabad")
            self.lg.enter_to("delhi")
            self.lg.dep_date()
            self.lg.travellers()
            self.lg.search_flights()


        except Exception as ex:
            print("test_TC001 exception generated ", ex)
