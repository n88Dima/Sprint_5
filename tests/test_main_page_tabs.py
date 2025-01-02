from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from locators import MainPage
from data import Creds

class TestMainPageTabs:
    
    def test_redirect_to_main_page_from_logo_Stellar_Burger(self, driver: WebDriver):
        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        driver.find_element(*MainPage.LOGO).click()
        WebDriverWait(driver,3).until(EC.url_to_be(Creds.BASE_URL))
        assert driver.current_url == Creds.BASE_URL

    def test_redirect_to_main_page_from_constructor_button(self, driver: WebDriver):
        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        driver.find_element(*MainPage.CONSTRUCTOR_LINK).click()
        WebDriverWait(driver,3).until(EC.url_to_be(Creds.BASE_URL))
        assert driver.current_url == Creds.BASE_URL
