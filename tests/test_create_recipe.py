import allure
from data.data import TestData
from pages.create_recipe_page import CreateRecipePage
from pages.authorization_page import AuthorizationPage

@allure.suite('Создание рецепта')
@allure.feature('Функциональность создания рецепта')
class TestCreateRecipe:

    @allure.title('Проверка успешного создания рецепта')
    @allure.description('Тест проверяет, что пользователь успешно вводит все данные и создает рецепт')
    def test_create_recipe(self, driver):
        authorization_page = AuthorizationPage(driver)

        with allure.step('Ввод учетных данных'):
            authorization_page.authorization()

        create_recipe_page = CreateRecipePage(driver)

        with allure.step('Ввод данных'):
            create_recipe_page.create_recipe()

        with allure.step('Загрузка фотографии'):
            create_recipe_page.upload_photos()

        with allure.step('Сохранение введенных данных'):
            create_recipe_page.save_form()

        with allure.step('Проверка названия рецепта'):
            assert create_recipe_page.check_name_recipe() == TestData.NAME_RECIPE_TEXT



