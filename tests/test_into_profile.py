from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from locators import LoginPage,MainPage, RegPage
from data import Creds

class TestIntoProfile:
    
    def test_into_profile(self, driver: WebDriver):
        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPage.INPUT_EMAIL_LOGIN).send_keys(Creds.EMAIL)
        driver.find_element(*LoginPage.INPUT_PASSWORD_LOGIN).send_keys(Creds.PASSWORD)
        driver.find_element(*LoginPage.ENTER_BUTTON).click()
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.BASE_URL))
        driver.find_element(*MainPage.ACCOUNT_BUTTON).click
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.ACCOUNT_URL))
        assert driver.current_url == Creds.ACCOUNT_URL
