from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class search_result:
    okay_btn_by_xpath = "//button[@class = 'button buttonSecondry buttonBig fontSize12 relative']"
    custom_range_slider = "//div[@class='rangeslider__handle']"
    one_stop_checkbox = "//span[@title='1 Stop']/preceding-sibling::span/span/span[@class='check']"
    flight_card = "//div[@class='listingCard']"

    def __init__(self, driver, ex_wait, im_wait):
        self.driver = driver
        self.ex_wait = ex_wait
        self.im_wait = im_wait

    def search_flight(self):
        self.driver.find_element(By.XPATH, self.okay_btn_by_xpath).click()

    def custom_range(self):
        range_slider = self.driver.find_element(By.XPATH, "//div[@class='rangeslider__handle']")
        ActionChains(self.driver).drag_and_drop_by_offset(range_slider, -120, 0).perform()

    def select_1_stop(self):
        self.driver.find_element(By.XPATH, self.one_stop_checkbox).click()

    def get_flight_data(self):
        flights_card = self.driver.find_elements(By.XPATH, self.flight_card)
        flights_data = list()
        for card in flights_card:
            flights_data.append(card.text)
        for d in flights_data:
            print("Flight Data: ", d)
