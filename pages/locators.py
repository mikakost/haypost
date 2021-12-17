from selenium.webdriver.common.by import By


class BasePageLocators:
    LINK_CAREER = (By.CLASS_NAME, "submenu_btn:nth-child(1)")
    LINK_OUR_NETWORK = (By.CLASS_NAME, "submenu_btn:nth-child(2)")
    LINK_CONTACT_US = (By.CLASS_NAME, "submenu_btn:nth-child(3)")
    LINK_NEWS = (By.CLASS_NAME, "submenu_btn:nth-child(4)")


class MainPageLocators:
    TRACK_ERROR = (By.CLASS_NAME, "error_message")
    TRACK_INFO = (By.CLASS_NAME, "tracking_details")
    TRACK_NUMBER = (By.ID, "trackingNumber")
    TRACK_NO_FOUND = (By.CLASS_NAME, "track_hint")
