import os

import allure
from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        person = generated_person()
        path = generated_file()
        self.remove_footer()
        with allure.step('Fill in the first name input field'):
            self.element_is_visible(Locators.FIRST_NAME).send_keys(person.first_name)
        with allure.step('Fill in the last name input field'):
            self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        with allure.step('Fill in the email input field'):
            self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        with allure.step('Set up the Gender radiobutton'):
            self.element_is_visible(Locators.GENDER).click()
        with allure.step('Fill in the mobile number input field'):
            self.element_is_visible(Locators.MOBILE).send_keys(person.mobile)
        with allure.step('Fill in the subject input field'):
            subject = self.element_is_visible(Locators.SUBJECT)
            subject.send_keys(person.subject)
            subject.send_keys(Keys.RETURN)
        with allure.step('Check hobbies checkbox'):
            self.element_is_visible(Locators.HOBBIES).click()
        with allure.step('Send file'):
            self.element_is_visible(Locators.FILE_INPUT).send_keys(path)
            os.remove(path)
        with allure.step('Fill in the address input file'):
            self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys(person.current_address)
        with allure.step('Click the Submit button'):
            self.element_is_visible(Locators.SUBMIT).click()
        return person

    def form_result(self):
        results_list = self.elements_are_visible(Locators.RESULT_TABLE)
        results_text = []
        for i in results_list:
            results_text.append(i.text)

        return results_text
