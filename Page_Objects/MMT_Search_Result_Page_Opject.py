from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd


class search_result:
    """This is flight search result page object class where we store all the
     web element XPATH and other required objects. Each XPATH is stored in an
     object which can be used across the project framework"""

    df = pd.DataFrame(columns=['lock', 'i', 'company', 'flight_number', 'departure_time', 'source_city', 'travel_time',
                               'stops', 'arrival_time', 'days', 'destination_city', 'ticket_price', 'view', 'offer'])

    okay_btn_by_xpath = "//button[@class = 'button buttonSecondry buttonBig fontSize12 relative']"
    custom_range_slider = "//div[@class='rangeslider__handle']"
    one_stop_checkbox = "//span[@title='1 Stop']/preceding-sibling::span/span/span[@class='check']"
    flight_card = "//div[@class='listingCard']"

    def __init__(self, driver, ex_wait, im_wait):
        self.driver = driver
        self.ex_wait = ex_wait
        self.im_wait = im_wait

    """Click on search button to get list of flights available"""
    def search_flight(self):
        try:
            btn = self.driver.find_element(By.XPATH, self.okay_btn_by_xpath)
            self.ex_wait(1, btn)
            btn.click()
        except Exception as ex:
            print("search_flight: ", ex)

    """select and change custom range of ticket price"""
    def custom_range(self):
        try:
            range_slider = self.driver.find_element(By.XPATH, "//div[@class='rangeslider__handle']")
            self.ex_wait(1, range_slider)
            ActionChains(self.driver).drag_and_drop_by_offset(range_slider, -120, 0).perform()
        except Exception as ex:
            print("custom_range: ", ex)

    """this is select 1 stop flight check box to set preference"""
    def select_1_stop(self):
        try:
            check = self.driver.find_element(By.XPATH, self.one_stop_checkbox)
            self.ex_wait(1, check)
            check.click()
        except Exception as ex:
            print("select_1_stop: ", ex)

    """get all flight information and store flight information into all_flight_info.csv file """
    def get_flight_data(self):
        try:
            flights_card = self.driver.find_elements(By.XPATH, self.flight_card)
            flights_data = list()
            for card in flights_card:
                flights_data.append(card.text)
            for d in flights_data:
                x = list()
                x.append(d.split("\n"))
                if len(x) > 12:
                    x = x[:12]
                self.df = self.df.append(pd.DataFrame(x, columns=self.df.columns))
                print("List: ", x, " TYPE: ", type(x))
                print(self.df)
                # print("Flight Data: ", d, " Data Type: ", type(d))
            self.df.to_csv('All_Flights.csv')
        except Exception as ex:
            print("get_flight_gate: ", ex)

"""****************************************** End *************************************************"""
