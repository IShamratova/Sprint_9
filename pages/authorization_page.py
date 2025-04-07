import allure
from data.data import TestData
from locators.authorization_page_locators import AuthorizationPageLocators
from pages.base_page import BasePage


class AuthorizationPage(BasePage):

    @allure.step('Ввод учётных данных и клик по кнопке "Войти"')
    def authorization(self):
        # Явное ожидание для загрузки кнопки "Войти"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            AuthorizationPageLocators.LINK_ENTER,
            3)

        # Клик по кнопке "Войти"
        self.click_element_by_script_by_xpath(
            AuthorizationPageLocators.LINK_ENTER
        )

        # Явное ожидание для загрузки кнопки "Войти"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            AuthorizationPageLocators.BUTTON_ENTER, 3
        )

        # Ввод персональных данных
        self.set_text_to_field_by_xpath(
            AuthorizationPageLocators.INPUT_EMAIL_FOR_LOGIN, TestData.EMAIL
        )
        self.set_text_to_field_by_xpath(
            AuthorizationPageLocators.INPUT_PASSWORD_FOR_LOGIN, TestData.PASSWORD
        )

        # Клик по кнопке "Создать аккаунт"
        self.click_element_by_xpath(
            AuthorizationPageLocators.BUTTON_ENTER
        )

        # Явное ожидание для загрузки кнопки "Выход"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            AuthorizationPageLocators.LINK_EXIT,
            3
        )

    @allure.step('Проверка URL-адреса на соответствие странице логина')
    def check_login_url(self):
        # Проверка URL-адреса на соответствие страницы логина
        self.check_url(
            TestData.BASE_RECIPES_URL
        )