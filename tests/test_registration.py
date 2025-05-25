from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    LOGIN_OR_REGISTER_BUTTON, 
    LOGIN_POPUP, 
    NO_ACCOUNT_BUTTON, 
    EMAIL_INPUT, 
    PASSWORD_INPUT, 
    REPEAT_PASSWORD_INPUT, 
    CREATE_ACCOUNT_BUTTON, 
    USER_NAME, 
    AVATAR_ICON, 
    EMAIL_ERROR_TEXT, 
    EMAIL_BORDER, 
    PASSWORD_BORDER, 
    REPEAT_PASSWORD_BORDER
)

# Регистрация пользователя
def test_user_can_register(driver, email):
    driver.get('https://qa-desk.stand.praktikum-services.ru/')

    # Нажать кнопку «Вход и регистрация».
    # Ожидание, что кнопка станет кликабельной, не больше 3 секунд
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LOGIN_OR_REGISTER_BUTTON)
    )
    driver.find_element(*LOGIN_OR_REGISTER_BUTTON).click()

    # Ждем, пока поп-ап откроется
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_POPUP)
    )

    # Нажать кнопку «Нет аккаунта».
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)
    )
    driver.find_element(*NO_ACCOUNT_BUTTON).click()

    # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys("1234")
    driver.find_element(*REPEAT_PASSWORD_INPUT).send_keys("1234")
    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    # Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(USER_NAME)
    )
    user_name = driver.find_element(*USER_NAME)
    assert user_name.text == "User.", "Имя пользователя не отображается"

    avatar = driver.find_element(*AVATAR_ICON)
    assert avatar.is_displayed(), "Аватар не отображается"

# Регистрация пользователя c email не по маске  *******@*******.***
def test_user_cant_register_with_wrong_email(driver, wrong_email):
    driver.get('https://qa-desk.stand.praktikum-services.ru/')

    # Нажать кнопку «Вход и регистрация».
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LOGIN_OR_REGISTER_BUTTON)
    )
    driver.find_element(*LOGIN_OR_REGISTER_BUTTON).click()

    # Ждем, пока поп-ап откроется
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_POPUP)
    )

    # Нажать кнопку «Нет аккаунта».
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)
    )
    driver.find_element(*NO_ACCOUNT_BUTTON).click()

    # Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт».
    driver.find_element(*EMAIL_INPUT).send_keys(wrong_email)
    driver.find_element(*PASSWORD_INPUT).send_keys("1234")
    driver.find_element(*REPEAT_PASSWORD_INPUT).send_keys("1234")
    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    

    # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
    error_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(EMAIL_ERROR_TEXT)
    )
    assert error_text.text == "Ошибка", "Сообщение 'Ошибка' не отображается под полем Email"

    email_wrapper = driver.find_element(*EMAIL_BORDER)
    assert "input_inputError" in email_wrapper.get_attribute("class"), "Поле Email не выделено красным"

    password_wrapper = driver.find_element(*PASSWORD_BORDER)
    assert "input_inputError" in password_wrapper.get_attribute("class"), "Поле Password не выделено красным"

    submitPassword_wrapper = driver.find_element(*REPEAT_PASSWORD_BORDER)
    assert "input_inputError" in submitPassword_wrapper.get_attribute("class"), "Поле submitPassword не выделено красным"

# Регистрация уже существующего пользователя
def test_user_cant_register_with_the_same_credentials(driver, existing_email):
    driver.get('https://qa-desk.stand.praktikum-services.ru/')

    # Нажать кнопку «Вход и регистрация».
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LOGIN_OR_REGISTER_BUTTON)
    )
    driver.find_element(*LOGIN_OR_REGISTER_BUTTON).click()

    # Ждем, пока поп-ап откроется
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_POPUP)
    )

    # Нажать кнопку «Нет аккаунта».
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)
    )
    driver.find_element(*NO_ACCOUNT_BUTTON).click()

    # Заполнить все поля формы регистрации данными уже существующего в системе пользователя и нажать кнопку «Создать аккаунт».
    driver.find_element(*EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*PASSWORD_INPUT).send_keys("1234")
    driver.find_element(*REPEAT_PASSWORD_INPUT).send_keys("1234")
    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
    error_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(EMAIL_ERROR_TEXT)
    )
    assert error_text.text == "Ошибка", "Сообщение 'Ошибка' не отображается под полем Email"

    email_wrapper = driver.find_element(*EMAIL_BORDER)
    assert "input_inputError" in email_wrapper.get_attribute("class"), "Поле Email не выделено красным"

    password_wrapper = driver.find_element(*PASSWORD_BORDER)
    assert "input_inputError" in password_wrapper.get_attribute("class"), "Поле Password не выделено красным"

    submitPassword_wrapper = driver.find_element(*REPEAT_PASSWORD_BORDER)
    assert "input_inputError" in submitPassword_wrapper.get_attribute("class"), "Поле submitPassword не выделено красным"