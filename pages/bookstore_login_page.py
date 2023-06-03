import allure

from locators.bookstore_login_page_locators import LoginPageLocators as login_locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def login_user(self):
        with allure.step('Fill in User Name field'):
            self.element_is_visible(login_locators.USER_NAME).send_keys('Pooper')
        with allure.step('Fill in Password'):
            self.element_is_visible(login_locators.PASSWORD).send_keys('LadaRiva2107!')
        with allure.step('Click LogIn button'):
            self.element_is_visible(login_locators.LOGIN_BUTTON).click()


