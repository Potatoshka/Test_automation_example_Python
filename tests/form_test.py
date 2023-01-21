import allure

from pages.form_page import FormPage


class TestFormPage:

    @allure.story('Fill registration form test')
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_fields_and_submit()
        result = form_page.form_result()
        with allure.step("Check name:"):
            assert f'{person.first_name} {person.last_name}' == result[0]
        with allure.step('Check email:'):
            assert person.email == result[1]
        with allure.step('Check address'):
            assert person.current_address == result[8]
        with allure.step('Check tel number'):
            assert person.mobile == result[3]
