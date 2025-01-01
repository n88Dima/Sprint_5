from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from locators import LoginPage,MainPage
from data import Creds

class TestLogout:
    
 def test_logout_successful(self,driver: WebDriver):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.LOGIN_URL))
        driver.find_element(*LoginPage.INPUT_EMAIL_LOGIN).send_keys(Creds.EMAIL)
        driver.find_element(*LoginPage.INPUT_PASSWORD_LOGIN).send_keys(Creds.PASSWORD)
        driver.find_element(*LoginPage.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.BASE_URL))
        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        exit_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPage.EXIT_BUTTON))
        exit_button.click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.LOGIN_URL))
        assert driver.current_url == Creds.LOGIN_URL