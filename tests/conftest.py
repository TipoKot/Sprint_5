import pytest
import random
import string
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-save-password-bubble")  # на всякий случай

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def email():
    prefix = "user"
    domain = "@testmail.com"
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{prefix}_{random_part}{domain}"

@pytest.fixture
def wrong_email():
    prefix = "user"
    domain = "testmail.com"
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{prefix}_{random_part}{domain}"

@pytest.fixture
def existing_email():
    return "test@test.com"

@pytest.fixture
def existing_password():
    return "1234"