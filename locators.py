from selenium.webdriver.common.by import By


class MainPage:
    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"
    # Кнопка "Булки"
    BUNS_SECTION = By.XPATH, "//span[text()='Булки']"
    # Кнопка "Соусы"
    SAUCES_SECTION = By.XPATH, "//span[text()='Соусы']"
    # Кнопка "Начинки"
    FILLINGS_SECTION = By.XPATH, "//span[text()='Начинки']"
    # Кнопка "Личный кабинет"
    ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"
    # Кнопка "Конструктор"
    CONSTRUCTOR_LINK = By.XPATH, "//p[text()='Конструктор']"
    # Булка 1
    BUN = By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"
    # Соус 1
    SAUCE = By.XPATH, "//p[text()='Соус Spicy-X']"
    # Начинка 1
    FILLING = By.XPATH, "//p[text()= 'Мясо бессмертных моллюсков Protostomia']"
    # Логотип Stellar Burgers
    LOGO = By.CLASS_NAME,"AppHeader_header__logo__2D0X2"
    # Заголовок Булки
    BUN_HEADDER = By.XPATH, ".//h2[text()='Булки']"
    # Заголовок Соусы
    SAUCE_HEADDER = By.XPATH, ".//h2[text()='Соусы']"
    # Заголовок Начинки
    FILLING_HEADDER = By.XPATH, ".//h2[text()='Начинки']"


class RegPage:
    # Кнопка регистрации
    REG_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']"
    # Поле Имя
    INPUT_NAME = By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input"
    # Поле email
    INPUT_EMAIL = By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input"
    # Поле Пароль
    INPUT_PASSWORD = By.XPATH, "//input[@name='Пароль']"
    # Перенаправление на ВХОД
    REDIRECT_LOGIN = By.XPATH, "//a[@href='/login']"
    # ERROR(Пароль)
    ERROR_MSG = By.CLASS_NAME, "input__error"
    # ERROR(Такой пользователь уже сущесвует)
    ERROR_MSG_ALREADY_REGISTER = By.XPATH, "//p[text()='Такой пользователь уже существует']" 

class LoginPage:
    #Поле email
    INPUT_EMAIL_LOGIN = By.XPATH, "//input[@name='name']"
    #Поле Пароль
    INPUT_PASSWORD_LOGIN = By.XPATH, "//input[@name='Пароль']"
    #Кнопка Войти
    ENTER_BUTTON = By.XPATH, "//button[text()='Войти']"
    #Перенаправление на РЕГИСТРАЦИЮ
    REDIRECT_REGISTRATION = By.XPATH, "//a[@href='/register']"
    #Перенаправление на ВОССТАНОВИТЬ ПАРОЛЬ
    REDIRECT_FORGOT_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']"
    #Выход из аккаунта
    EXIT_BUTTON = By.XPATH, "//button[text()='Выход']"
