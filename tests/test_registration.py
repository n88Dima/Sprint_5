
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from locators import LoginPage,MainPage,RegPage
from data import Creds
from helpers import generate_email, generate_password, generate_username


class TestRegistration:

    def test_register_success(self,driver: WebDriver):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        driver.find_element(*LoginPage.REDIRECT_REGISTRATION).click()
        driver.find_element(*RegPage.INPUT_NAME).send_keys(generate_username())
        driver.find_element(*RegPage.INPUT_EMAIL).send_keys(generate_email())
        driver.find_element(*RegPage.INPUT_PASSWORD).send_keys(generate_password())
        driver.find_element(*RegPage.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
        assert driver.current_url == Creds.LOGIN_URL
    
    def test_register_witout_name(self,driver: WebDriver):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        driver.find_element(*LoginPage.REDIRECT_REGISTRATION).click()
        driver.find_element(*RegPage.INPUT_EMAIL).send_keys(generate_email())
        driver.find_element(*RegPage.INPUT_PASSWORD).send_keys(generate_password())
        driver.find_element(*RegPage.REG_BUTTON).click()
        assert driver.current_url == Creds.REGISTER_URL

    def test_register_invalid_password(self, driver: WebDriver):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        driver.find_element(*LoginPage.REDIRECT_REGISTRATION).click()
        driver.find_element(*RegPage.INPUT_NAME).send_keys(generate_username())
        driver.find_element(*RegPage.INPUT_EMAIL).send_keys(generate_email())
        driver.find_element(*RegPage.INPUT_PASSWORD).send_keys(*Creds.INVALID_PASSWORD)
        driver.find_element(*RegPage.REG_BUTTON).click()
        err = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegPage.ERROR_MSG))
        assert err.text == "Некорректный пароль"

    def test_register_invalid_email(self, driver : WebDriver):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        driver.find_element(*LoginPage.REDIRECT_REGISTRATION).click()
        driver.find_element(*RegPage.INPUT_NAME).send_keys(generate_username())
        driver.find_element(*RegPage.INPUT_EMAIL).send_keys(*Creds.INVALID_EMAIL)
        driver.find_element(*RegPage.INPUT_PASSWORD).send_keys(generate_password())
        driver.find_element(*RegPage.REG_BUTTON).click()
        err = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegPage.ERROR_MSG_ALREADY_REGISTER))
        assert err.text == "Такой пользователь уже существует"

    def test_register_already_registered_user(self,driver: WebDriver):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        driver.find_element(*LoginPage.REDIRECT_REGISTRATION).click()
        driver.find_element(*RegPage.INPUT_NAME).send_keys(*Creds.USERNAME)
        driver.find_element(*RegPage.INPUT_EMAIL).send_keys(*Creds.EMAIL)
        driver.find_element(*RegPage.INPUT_PASSWORD).send_keys(*Creds.PASSWORD)
        driver.find_element(*RegPage.REG_BUTTON).click()
        err = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegPage.ERROR_MSG_ALREADY_REGISTER))
        assert err.text == "Такой пользователь уже существует"
