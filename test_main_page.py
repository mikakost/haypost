import time
from pages.main_page import MainPage
from pages.locators import MainPageLocators


class TestTrackingNumber:
    def test_correct_track_number(self, browser):
        link = "https://www.haypost.am/en/"
        track_number = "RA146678480LV"
        page = MainPage(browser, link)
        page.open()
        page.track_shipment(track_number)
        time.sleep(5)
        assert page.is_element_present(*MainPageLocators.TRACK_INFO), (
            "Track info not found")

    def test_wrong_track_number(self, browser):
        link = "https://www.haypost.am/en/"
        track_number = "RA"
        page = MainPage(browser, link)
        page.open()
        page.track_shipment(track_number)
        assert page.is_element_present(*MainPageLocators.TRACK_NO_FOUND), (
            "Track info found")

    def test_empty_track_info(self, browser):
        link = "https://www.haypost.am/en/"
        track_number = ""
        page = MainPage(browser, link)
        page.open()
        page.track_shipment(track_number)
        assert page.is_element_present(*MainPageLocators.TRACK_ERROR), (
            "Track number is present")
