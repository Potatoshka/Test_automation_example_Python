from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME = (By.CSS_SELECTOR, '#userName')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login')
