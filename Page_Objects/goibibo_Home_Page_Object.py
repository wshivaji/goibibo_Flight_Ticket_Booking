import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login:
    flights_btn_by_xpath = "//a[@class='nav-link active' or @href='/flights/']"
    oneWay_option_by_xpath = "//span[text()='One-way']"
    from_textbox_by_xpath = "//div//span[text()='From']/following-sibling::p"
    to_textbox_by_xpath = "//div//span[text()='To']/following-sibling::p"
    departure_dropdown_by_xpath = "//div//span[text()='Departure']/following-sibling::p"
    departure_date_by_xpath = "//div[@class='DayPicker-Day' and @aria-label='Mon Jan 09 2023']"
    done_btn_by_xpath = "//span[@class='fswTrvl__done' and text()='Done']"
    regular_fare_option_by_xpath = "//li/span[text()='regular']"
    traveller_dropdown_by_xpath = "//div//span[text()='Travellers & Class']/following-sibling::p"
    adult_plus_by_xpath = "//div//p[text()='(Aged 12+ yrs)']/parent::div/div/span/following-sibling::span[@class='sc-ehCJOs kujlZU']"
    economy_by_xpath = "//li[text()='economy']"
    traveller_done_btn_by_xpath = "//div/a[text()='Done']"
    search_btn_by_xpath = "//div/span[contains(text(),'SEARCH FLIGHTS')]"
    stop1_btn_by_xpath = "//div[text()='Stops']/following-sibling::div//label/span[text()=' Stop']"

    def __init__(self, driver, ex_wait, im_wait):
        self.driver = driver
        self.ex_wait = ex_wait
        self.im_wait = im_wait

    def click_flight_btn(self):
        btn = self.driver.find_element(By.XPATH, self.flights_btn_by_xpath)
        # self.ex_wait(10, btn)
        btn.click()
        time.sleep(2)

    def click_oneWay_option(self):
        btn = self.driver.find_element(By.XPATH, self.oneWay_option_by_xpath)
        # self.ex_wait(10, btn)
        btn.click()
        time.sleep(2)

    def enter_from(self, source):
        txt = self.driver.find_element(By.XPATH, self.from_textbox_by_xpath)
        print("Source: ", source, " element: ", txt)
        txt.click()
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(source)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div//ul//li//span[text()='Aurangabad, India']").click()
        time.sleep(2)

    def enter_to(self, destination):
        self.driver.find_element(By.XPATH, "//div//div//input[@type='text']").send_keys(destination)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div//p//span[text()='New Delhi, India']").click()
        time.sleep(2)

    def dep_date(self):
        self.driver.find_element(By.XPATH, self.departure_date_by_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.done_btn_by_xpath).click()
        time.sleep(2)

    def travellers(self):
        self.driver.find_element(By.XPATH, self.adult_plus_by_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.economy_by_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.traveller_done_btn_by_xpath).click()
        time.sleep(2)

    def search_flights(self):
        self.driver.find_element(By.XPATH, self.search_btn_by_xpath).click()
        #page = self.driver.find_element(By.XPATH, "//div[@class='seo-srp-layoutstyles__RightWrap-sc-11ypfer-3 cerDMj']")
        page = self.driver.find_element(By.XPATH, "//div[@class='srp-card-uistyles__SeoCard-sc-3flq99-4 iawtfg']")
        wait = WebDriverWait(self.driver, 30)
        page = wait.until(EC.element_to_be_clickable(page))


        #self.driver.set_page_load_timeout(40)
        #time.sleep(60)
        #self.driver.refresh()
        #btn1 = self.driver.find_element(By.XPATH, "//div[text()='Stops']/following-sibling::div//label/span[text()=' Stop']")
        #btn1.click()
        #time.sleep(4)


