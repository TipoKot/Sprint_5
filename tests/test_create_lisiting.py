from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from locators import (
    CREATE_LISTING_BUTTON,
    AUTHORIZE_POPUP,
    AUTHORIZE_TEXT,
    PRODUCT_NAME_INPUT,
    PRODUCT_DISCRIPTION_INPUT,
    PRODUCT_PRICE_INPUT,
    CHOOSE_CITY,
    CHOOSE_TYPE,
    CONDITION_USED,
    SUBMIT_PRODUCT_BUTTON,
    AVATAR_ICON,
    USER_PROFILE,
    PRODUCT_CARD,
    LOGIN_OR_REGISTER_BUTTON,
    LOGIN_POPUP,
    EMAIL_INPUT,
    LOGIN_BUTTON,
    PASSWORD_INPUT
)

# Создание объявления неавторизованным пользователем
def test_not_authorized_user_cant_create_listing(driver):
    driver.get('https://qa-desk.stand.praktikum-services.ru/')

    # Нажать кнопку «Разместить объявление».
    driver.find_element(*CREATE_LISTING_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AUTHORIZE_POPUP))
    
    # Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
    authorize_error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AUTHORIZE_TEXT)
    )
    assert authorize_error.text == "Чтобы разместить объявление, авторизуйтесь", "Заголовок не совпадает"

# Создание объявления авторизованным пользователем
def test_authorized_user_can_create_listing(driver, existing_email, existing_password):
    driver.get('https://qa-desk.stand.praktikum-services.ru/')

    # Авторизоваться под заранее созданным пользователем.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LOGIN_OR_REGISTER_BUTTON)
    )
    driver.find_element(*LOGIN_OR_REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_POPUP)
    )
    driver.find_element(*EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(LOGIN_POPUP)
    )

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(CREATE_LISTING_BUTTON)
    )
    button.click()

    # Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
    name_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(PRODUCT_NAME_INPUT)
    )
    name_input.send_keys("Название")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PRODUCT_DISCRIPTION_INPUT)
    )
    driver.find_element(*PRODUCT_DISCRIPTION_INPUT).send_keys("Описание")

    price_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PRODUCT_PRICE_INPUT)
    )
    price_input.send_keys("1000")

    # Выбрать из Dropdown «Категорию» и «Город».
    city_wrapper = driver.find_element(*CHOOSE_CITY)
    city_wrapper.find_element(By.CLASS_NAME, "dropDownMenu_arrowDown__pfGL1").click()
    city_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Санкт-Петербург']"))
    )
    city_button.click()

    type_wrapper = driver.find_element(*CHOOSE_TYPE)
    type_wrapper.find_element(By.CLASS_NAME, "dropDownMenu_arrowDown__pfGL1").click()
    type_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Хобби']"))
    )
    type_button.click()

    # Выбрать RabioButton «Состояние товара».
    driver.find_element(*CONDITION_USED).click()

    # Нажать кнопку «Опубликовать».
    driver.find_element(*SUBMIT_PRODUCT_BUTTON).click()

    # Перейти в профиль пользователя.
    driver.find_element(*AVATAR_ICON).click()

    # Проверить: в блоке «Мои объявления» отображается созданное объявление.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(USER_PROFILE)
    )
    product_card = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PRODUCT_CARD)
    )
    assert product_card.is_displayed(), "Карточка товара не отображается"