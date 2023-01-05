import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login:
    front_cover_by_xpath = "//div[@data-cy='outsideModal']"
    flights_btn_by_xpath = "//li/div/a[@href='https://www.makemytrip.com/flights/']"
    hotel_btn_by_xpath = "//li/div/a[@href='https://www.makemytrip.com/hotels/']"
    oneWay_option_by_xpath = "//ul/li[@data-cy='oneWayTrip']"
    from_textbox_by_xpath = "//label[@for='fromCity']"
    from_city_by_xpath = "//input[@id='fromCity']"
    to_textbox_by_xpath = "//label[@for='toCity']"
    to_city_by_xpath = "//input[@placeholder='To']"
    departure_dropdown_by_xpath = "//label[@for='departure']"
    departure_date_by_xpath = "//div[@class='DayPicker-Day' and @aria-label='Mon Jan 23 2023']"
    traveller_dropdown_by_xpath = "//label[@for='travellers']"
    adult_by_xpath = "//li[@data-cy='adults-4']"
    children_by_xpath = "//li[@data-cy='children-2']"
    infant_by_xpath = "//li[@data-cy='infants-1']"
    economy_by_xpath = "//li[@data-cy='travelClass-0']"
    appply_btn_by_xpath = "//button[@type='button' and contains(text(),'APPLY')]"
    regular_option_by_xpath = "//ul/li/p[contains(text(), 'Regular')]"
    flight_search_by_xpath = "//div/p/a[contains(text(), 'Search')]"

    def __init__(self, driver, ex_wait, im_wait):
        self.driver = driver
        self.ex_wait = ex_wait
        self.im_wait = im_wait

    def click_front_cover(self):
        self.driver.find_element(By.XPATH, self.front_cover_by_xpath).click()

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 600);")
        self.driver.execute_script("window.scrollTo(600, 0);")

    def click_flight_btn(self):
        btn = self.driver.find_element(By.XPATH, self.flights_btn_by_xpath)
        self.ex_wait(10, btn)
        btn.click()

    def click_oneWay_option(self):
        btn = self.driver.find_element(By.XPATH, self.oneWay_option_by_xpath)
        self.ex_wait(10, btn)
        btn.click()

    def enter_from(self, source):
        txt = self.driver.find_element(By.XPATH, self.from_textbox_by_xpath)
        self.ex_wait(20, txt)
        print("Source: ", source, " element: ", txt)
        text_box = self.driver.find_element(By.XPATH, self.from_city_by_xpath)
        text_box.send_keys(source)
        time.sleep(2)
        source_list = self.driver.find_elements(By.XPATH, "//li[@role='option']")
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
        # self.driver.find_element(By.ID, id_1).click()

    def enter_to(self, destination):
        txt1 = self.driver.find_element(By.XPATH, self.to_textbox_by_xpath)
        txt1.click()
        print("Destination: ", destination, " element: ", txt1)
        text1_to = self.driver.find_element(By.XPATH, self.to_city_by_xpath)
        text1_to.send_keys(destination)
        time.sleep(2)
        destination_list = self.driver.find_elements(By.XPATH, "//li[@role='option']")
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

    def dep_date(self):
        self.driver.find_element(By.XPATH, self.departure_dropdown_by_xpath).click()

        self.driver.find_element(By.XPATH, self.departure_date_by_xpath).click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, self.done_btn_by_xpath).click()
        # time.sleep(2)

    def travellers(self):
        self.driver.find_element(By.XPATH, self.traveller_dropdown_by_xpath).click()
        self.driver.find_element(By.XPATH, self.adult_by_xpath).click()
        self.driver.find_element(By.XPATH, self.children_by_xpath).click()
        self.driver.find_element(By.XPATH, self.infant_by_xpath).click()
        self.driver.find_element(By.XPATH, self.economy_by_xpath).click()
        self.driver.find_element(By.XPATH, self.appply_btn_by_xpath).click()

    def regular_btn(self):
        self.driver.find_element(By.XPATH, self.regular_option_by_xpath).click()

    def search_btn(self):
        self.driver.find_element(By.XPATH, self.flight_search_by_xpath).click()
