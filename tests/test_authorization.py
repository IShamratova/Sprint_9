import allure
from pages.authorization_page import AuthorizationPage

@allure.suite('Авторизация пользователя')
@allure.feature('Функциональность авторизации')
class TestAuthorization:

    @allure.title('Проверка успешной авторизации')
    @allure.description('Тест проверяет, что пользователь успешно вводит учетные данные и заходит в аккаунт')
    def test_login_user(self, driver):

        authorization_page = AuthorizationPage(driver)

        with allure.step('Ввод учетных данных'):
            authorization_page.authorization()

        with allure.step('Проверка успешного входа'):
            authorization_page.check_login_url()


