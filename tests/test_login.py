from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from locators import (
    LOGIN_OR_REGISTER_BUTTON,
    LOGIN_BUTTON, 
    LOGIN_POPUP, 
    EMAIL_INPUT, 
    PASSWORD_INPUT, 
    USER_NAME, 
    AVATAR_ICON,
    EXIT_BUTTON
)


# Login пользователя
def test_user_can_login(driver, existing_email, existing_password):
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

    # Заполнить все поля формы авторизации и нажать кнопку «Войти».
    driver.find_element(*EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*LOGIN_BUTTON).click()

    # Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(USER_NAME)
    )
    user_name = driver.find_element(*USER_NAME)
    assert user_name.text == "User.", "Имя пользователя не отображается"

    avatar = driver.find_element(*AVATAR_ICON)
    assert avatar.is_displayed(), "Аватар не отображается"

# Logout пользователя
def test_user_can_logout(driver, existing_email, existing_password):
    driver.get('https://qa-desk.stand.praktikum-services.ru/')

    # Авторизоваться под заранее созданным пользователем.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LOGIN_OR_REGISTER_BUTTON)
    )
    driver.find_element(*LOGIN_OR_REGISTER_BUTTON).click()

    # Ждем, пока поп-ап откроется
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_POPUP)
    )

    # Заполнить все поля формы авторизации и нажать кнопку «Войти».
    driver.find_element(*EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*LOGIN_BUTTON).click()

    # Нажать кнопку «Выйти».
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(EXIT_BUTTON)
    )
    driver.find_element(*EXIT_BUTTON).click()

    # Проверить: аватар пользователя и имя User больше не отображается в правом верхнем углу около кнопки «Разместить объявление», там теперь отображается кнопка «Вход и регистрация».
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_OR_REGISTER_BUTTON)
    )
    login_or_register_button = driver.find_element(*LOGIN_OR_REGISTER_BUTTON)
    assert login_or_register_button.is_displayed(), "Кнопка 'Вход и регистрация' не отображается после выхода"

    
    try:
        avatar = driver.find_element(*AVATAR_ICON)
        assert not avatar.is_displayed(), "Аватар всё ещё отображается"
    except NoSuchElementException:
        pass

    try:
        user_name = driver.find_element(*USER_NAME)
        assert not user_name.text == "User.", "Имя пользователя отображается"
    except NoSuchElementException:
        pass
