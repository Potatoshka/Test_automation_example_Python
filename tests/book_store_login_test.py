import allure

from pages.bookstore_login_page import LoginPage


class TestLogin:
    @allure.story('New user register test')
    def test_login(self, driver):
        login_page = LoginPage(driver, 'https://demoqa.com/login')
        login_page.open()
        login_page.login_user()
        profile_page_url = 'https://demoqa.com/profile'
        current_url = driver.current_url
        assert profile_page_url == current_url
