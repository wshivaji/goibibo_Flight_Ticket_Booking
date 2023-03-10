import time
from datetime import datetime as dt

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This is page object file and code for page all xpath are stored in respective object and 
    called those objects where ever needed"""


class Home_page:

    """This is XPATH section where we keep all the xpath of home page
    web elements. Each XPATH is store in an object, that can be used
    anywhere across the project framework."""

    front_cover_by_xpath = "//div[@data-cy='outsideModal']"
    flights_btn_by_xpath = "//li/div/a[@href='https://www.makemytrip.com/flights/']"
    hotel_btn_by_xpath = "//li/div/a[@href='https://www.makemytrip.com/hotels/']"
    oneWay_option_by_xpath = "//ul/li[@data-cy='oneWayTrip']"
    from_textbox_by_xpath = "//label[@for='fromCity']"
    from_city_by_xpath = "//input[@id='fromCity']"
    to_textbox_by_xpath = "//label[@for='toCity']"
    to_city_by_xpath = "//input[@placeholder='To']"
    departure_dropdown_by_xpath = "//label[@for='departure']"
    departure_date_by_xpath = "//div[@class='DayPicker-Day' and @aria-label='"
    traveller_dropdown_by_xpath = "//label[@for='travellers']"
    adult_by_xpath = "//li[@data-cy='adults-"
    children_by_xpath = "//li[@data-cy='children-"
    infant_by_xpath = "//li[@data-cy='infants-"
    economy_by_xpath = "//li[@data-cy='travelClass-0']"
    apply_btn_by_xpath = "//button[@type='button' and contains(text(),'APPLY')]"
    regular_option_by_xpath = "//ul/li/p[contains(text(), 'Regular')]"
    flight_search_by_xpath = "//div/p/a[contains(text(), 'Search')]"

    """This is initialization constructor where we receive objects and initialize local objects"""
    def __init__(self, driver, ex_wait, im_wait):
        self.driver = driver
        self.ex_wait = ex_wait
        self.im_wait = im_wait

    """this is click event on transparent front cover to make webelements clickable"""
    def click_front_cover(self):
        try:
            self.driver.find_element(By.XPATH, self.front_cover_by_xpath).click()
        except Exception as ex:
            print("click_front_cover: ", ex)

    """This is sample scroll up/down event to check control/access of webdriver to page"""

    def scroll(self):
        try:
            self.driver.execute_script("window.scrollTo(0, 600);")
            self.driver.execute_script("window.scrollTo(600, 0);")
        except Exception as ex:
            print("scroll: ", ex)

    """This is click event on flight btn"""

    def click_flight_btn(self):
        try:
            btn = self.driver.find_element(By.XPATH, self.flights_btn_by_xpath)
            self.ex_wait(5, btn)
            btn.click()
        except Exception as ex:
            print("click_flight_btn", ex)

    """This is click event on one way trip"""

    def click_oneWay_option(self):
        try:
            btn = self.driver.find_element(By.XPATH, self.oneWay_option_by_xpath)
            self.ex_wait(5, btn)
            btn.click()
        except Exception as ex:
            print("click_oneWay_option: ", ex)

    """This is click event, enter source and select required source location form dropdown"""

    def enter_from(self, source):
        try:
            txt = self.driver.find_element(By.XPATH, self.from_textbox_by_xpath)
            self.ex_wait(5, txt)
            print("Source: ", source, " element: ", txt)
            text_box = self.driver.find_element(By.XPATH, self.from_city_by_xpath)
            text_box.send_keys(source)
            time.sleep(2)
            source_list = self.driver.find_elements(By.XPATH, "//div//label[@for='fromCity']/parent::div//div//ul//li")

            id_1 = ""
            for element in source_list:
                if source in element.text:
                    print("Source: ", element.text)
                    id_1 = element.get_attribute("data-suggestion-index")
                    print("Source id: ", id_1)
                    print(element.get_attribute("id"))
                    element.click()
                    break
            print("Source id: ", id_1)

        except Exception as ex:
            print("enter_from: ", ex)

    """This is click event, enter destination and select required destination location form dropdown"""

    def enter_to(self, destination):
        try:
            txt1 = self.driver.find_element(By.XPATH, self.to_textbox_by_xpath)
            self.ex_wait(5, txt1)
            txt1.click()
            print("Destination: ", destination, " element: ", txt1)
            text1_to = self.driver.find_element(By.XPATH, self.to_city_by_xpath)
            text1_to.send_keys(destination)
            time.sleep(2)
            destination_list = self.driver.find_elements(By.XPATH, "//div//label[@for='toCity']/parent::div//div//ul//li")

            id_1 = ""
            for element in destination_list:
                if destination in element.text:
                    print("destination: ", element.text)
                    id_1 = element.get_attribute("data-suggestion-index")
                    print("destination id: ", id_1)
                    print(element.get_attribute("id"))
                    element.click()
                    break
            print("destination id: ", id_1)
            # self.driver.find_element(By.ID, id_1).click()
        except Exception as ex:
            print("enter_to", ex)

    """This is select departure date selection event """
    def dep_date(self, str_date):
        try:
            str_date = str(str_date)
            date_object = dt.strptime(str_date, "%d/%m/%Y")
            date = date_object.strftime("%a %b %d %Y")
            date_xpath = f"{self.departure_date_by_xpath}{date}']"
            date_pic = self.driver.find_element(By.XPATH, date_xpath)
            self.ex_wait(1, date_pic)
            date_pic.click()
            date = self.driver.find_element(By.XPATH, self.departure_date_by_xpath)

            date.click()
        except Exception as ex:
            print("dep_date: ", ex)

    def dep_date_1(self, str_date):
        try:

            date_object = dt.strptime(str_date, "%d/%m/%Y")
            date = date_object.strftime("%a %b %d %Y")
            date_xpath = f"{self.departure_date_by_xpath}{date}']"
            date = self.driver.find_element(By.XPATH, date_xpath)
            self.ex_wait(1, date)
            date.click()
        except Exception as ex:
            print("dep_date_1: ", ex)

    """This is select number of travellers event"""
    def travellers(self, adult, children, infant):
        try:
            self.driver.find_element(By.XPATH, self.traveller_dropdown_by_xpath).click()
            adult_xpath = f"{self.adult_by_xpath}{adult}']"
            self.driver.find_element(By.XPATH, adult_xpath).click()
            children_xpath = f"{self.children_by_xpath}{children}']"
            self.driver.find_element(By.XPATH, children_xpath).click()
            infant_xpath = f"{self.infant_by_xpath}{infant}']"
            self.driver.find_element(By.XPATH, infant_xpath).click()
            self.driver.find_element(By.XPATH, self.economy_by_xpath).click()
            self.driver.find_element(By.XPATH, self.apply_btn_by_xpath).click()
        except Exception as ex:
            print("travellers: ", ex)

    """This is regular option event"""

    def regular_btn(self):
        try:
            self.driver.find_element(By.XPATH, self.regular_option_by_xpath).click()
        except Exception as ex:
            print("regular_btn: ", ex)

    """THis is search button event"""

    def search_btn(self):
        try:
            self.driver.find_element(By.XPATH, self.flight_search_by_xpath).click()
        except Exception as ex:
            print("search_btn: ", ex)

"""***************************************** End ***********************************************"""