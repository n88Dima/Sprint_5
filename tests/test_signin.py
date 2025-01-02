from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from locators import LoginPage,MainPage, RegPage
from data import Creds

class TestSignIn:
    
    def test_signin_login_button_successful(self,driver: WebDriver):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.LOGIN_URL))
        driver.find_element(*LoginPage.INPUT_EMAIL_LOGIN).send_keys(Creds.EMAIL)
        driver.find_element(*LoginPage.INPUT_PASSWORD_LOGIN).send_keys(Creds.PASSWORD)
        driver.find_element(*LoginPage.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.BASE_URL))
        assert driver.current_url == Creds.BASE_URL
    
    def test_signin_profile_button_successful(self,driver: WebDriver):
        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.LOGIN_URL))
        driver.find_element(*LoginPage.INPUT_EMAIL_LOGIN).send_keys(Creds.EMAIL)
        driver.find_element(*LoginPage.INPUT_PASSWORD_LOGIN).send_keys(Creds.PASSWORD)
        driver.find_element(*LoginPage.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.BASE_URL))
        assert driver.current_url == Creds.BASE_URL
    
    def test_signin_redirect_from_registration_button_successful(self,driver: WebDriver):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver,3).until(EC.url_to_be(Creds.LOGIN_URL))
        driver.find_element(*LoginPage.REDIRECT_REGISTRATION).click()
        driver.find_element(*RegPage.REDIRECT_LOGIN).click()
        WebDriverWait(driver,3).until(EC.url_to_be(Creds.LOGIN_URL))
        driver.find_element(*LoginPage.INPUT_EMAIL_LOGIN).send_keys(Creds.EMAIL)
        driver.find_element(*LoginPage.INPUT_PASSWORD_LOGIN).send_keys(Creds.PASSWORD)
        driver.find_element(*LoginPage.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.BASE_URL))
        assert driver.current_url == Creds.BASE_URL
    
    def test_signin_forgot_password_button_successful(self,driver: WebDriver):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.LOGIN_URL))
        driver.find_element(*LoginPage.REDIRECT_FORGOT_PASSWORD).click()
        driver.find_element(*RegPage.REDIRECT_LOGIN).click()
        driver.find_element(*LoginPage.INPUT_EMAIL_LOGIN).send_keys(Creds.EMAIL)
        driver.find_element(*LoginPage.INPUT_PASSWORD_LOGIN).send_keys(Creds.PASSWORD)
        driver.find_element(*LoginPage.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Creds.BASE_URL))
        assert driver.current_url == Creds.BASE_URL