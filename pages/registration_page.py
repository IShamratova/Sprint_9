import allure
from data.data import TestData
from faker import Faker
from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    fake = Faker()

    @allure.step('Генерация случайных данных пользователя')
    def generation_user_data(self):
        # Создание нового пользователя без авторизации и выдача его данных
        first_name = self.fake.first_name()
        surname = self.fake.last_name()
        user_name = self.fake.user_name()
        email = f"{self.fake.random_int()}_{self.fake.email()}"  # Генерируем уникальный email
        password = self.fake.password()

        return {
            "name": first_name,
            "surname": surname,
            "user_name": user_name,
            "email": email,
            "password": password,
        }

    @allure.step('Ввод учётных данных и клик по кнопке "Создать аккаунт"')
    def registration(self):
        # Явное ожидание для загрузки кнопки "Создать аккаунт"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            RegistrationPageLocators.LINK_CREATE_ACCOUNT,
            3)

        # Клик по кнопке "Создать аккаунт"
        self.click_element_by_script_by_xpath(
            RegistrationPageLocators.LINK_CREATE_ACCOUNT
        )

        # Явное ожидание для загрузки страницы "Регистрация"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            RegistrationPageLocators.HEADER_REGISTRATION, 3
        )

        user = self.generation_user_data()

        # Ввод персональных данных
        self.set_text_to_field_by_xpath(
            RegistrationPageLocators.INPUT_NAME, user['name']
        )
        self.set_text_to_field_by_xpath(
            RegistrationPageLocators.INPUT_SURNAME, user['surname']
        )
        self.set_text_to_field_by_xpath(
            RegistrationPageLocators.INPUT_USER_NAME, user['user_name']
        )
        self.set_text_to_field_by_xpath(
            RegistrationPageLocators.INPUT_EMAIL, user['email']
        )
        self.set_text_to_field_by_xpath(
            RegistrationPageLocators.INPUT_PASSWORD, user['password']
        )

        # Клик по кнопке "Создать аккаунт"
        self.click_element_by_xpath(
            RegistrationPageLocators.BUTTON_CREATE_ACCOUNT
        )

        # Явное ожидание для загрузки кнопки "Войти"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            RegistrationPageLocators.BUTTON_ENTER,
            3
        )

    @allure.step('Проверка URL-адреса на соответствие странице логина')
    def check_login_url(self):
        # Проверка URL-адреса на соответствие страницы логина
        self.check_url(
            TestData.BASE_LOGIN_URL
        )