from selenium.webdriver.common.by import By

# Кнопки
LOGIN_OR_REGISTER_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
EXIT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
CREATE_LISTING_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
SUBMIT_PRODUCT_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

# Окна
LOGIN_POPUP = (By.CLASS_NAME, "homePage_modal__zSdUB")
AUTHORIZE_POPUP = (By.CLASS_NAME, "popUp_shell__LuyqR")

# Поля формы
EMAIL_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.NAME, "password")
REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")
PRODUCT_NAME_INPUT = (By.NAME, "name")
PRODUCT_DISCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
PRODUCT_PRICE_INPUT = (By.NAME, "price")
CONDITION_NEW = (By.XPATH, "//input[@name='condition' and @value='Новый']")
CONDITION_USED = (By.XPATH, "//label[text()='Б/У']")

# Drop-down списки
CHOOSE_CITY = (By.XPATH, "//input[@name='city']/ancestor::div[contains(@class, 'dropDownMenu_dropMenu')]")
CHOOSE_TYPE = (By.XPATH, "//input[@name='category']/ancestor::div[contains(@class, 'dropDownMenu_dropMenu')]")

# Элементы для проверки
USER_NAME = (By.XPATH, "//h3[@class='profileText name']")
USER_PROFILE = (By.XPATH, "//h1[text()='Мои объявления']")
AVATAR_ICON = (By.CLASS_NAME, "circleSmall")
EMAIL_ERROR_TEXT = (By.XPATH, "//input[@name='email']/ancestor::div/following-sibling::span")
EMAIL_BORDER = (By.XPATH, "//input[@name='email']/parent::div")
PASSWORD_BORDER = (By.XPATH, "//input[@name='password']/parent::div")
REPEAT_PASSWORD_BORDER = (By.XPATH, "//input[@name='submitPassword']/parent::div")
AUTHORIZE_TEXT = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
PRODUCT_CARD = (By.CLASS_NAME, "card")
PRODUCT_NAME = (By.XPATH, "//h2[@class='about']")
PRODUCT_DISCRIPTION = (By.XPATH, "//h3[@class='about']")