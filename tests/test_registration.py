import allure
from pages.registration_page import RegistrationPage

@allure.suite('Регистрация пользователя')
@allure.feature('Функциональность регистрации')
class TestRegistration:

    @allure.title('Проверка успешной регистрации')
    @allure.description('Тест проверяет, что пользователь успешно вводит учетные данные и заходит в аккаунт')
    def test_personal_account(self, driver):

        registration_page = RegistrationPage(driver)

        with allure.step('Генерация учетных данных'):
            registration_page.generation_user_data()

        with allure.step('Ввод учетных данных'):
            registration_page.registration()

        with allure.step('Проверка успешного входа'):
            registration_page.check_login_url()


