from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Utilities.Read_Config_Info import Read_Config as Rc
import Page_Objects.MMT_Home_Page_Object
from Test_Cases.Base_Class import initialization



class Test_Case1(initialization):

    def test_get_list_source(self):
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(options=chrome_options)

            #------------------------------------

            self.lg = Page_Objects.goibibo_Home_Page_Object.login(self.driver, self.Explicit_wait, self.Implicit_wait)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(50)
            self.driver.set_script_timeout(30)
            self.driver.implicitly_wait(30)
            self.driver.get(Rc.read_url())

            #------------------------------------


            self.lg.click_front_cover()
            self.lg.scroll()
            self.lg.click_flight_btn()
            self.lg.click_oneWay_option()
            self.lg.enter_from("Aurangabad")

            source_list = self.driver.find_elements(By.XPATH, "//li[@role='option']")
            print(source_list)

            for element in source_list:
                if "Aurangabad" in element.text:
                    element.click()
                    break



        except Exception as ex:
            print("Exception in test_get_list_source class", ex)



        pass

