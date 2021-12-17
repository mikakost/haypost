from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def track_shipment(self, track_number):
        track_trace = self.browser.find_element(*MainPageLocators.TRACK_NUMBER)
        track_trace.send_keys(track_number)
        track_trace.send_keys(Keys.ENTER)
