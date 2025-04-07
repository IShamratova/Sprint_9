import allure
from data.data import TestData
from locators.create_recipe_page_locators import CreateRecipePageLocators
from pages.base_page import BasePage


class CreateRecipePage(BasePage):


    @allure.step('Ввод учётных данных и клик по кнопке "Создать аккаунт"')
    def create_recipe(self):
        # Явное ожидание для загрузки раздела "Создать рецепт"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            CreateRecipePageLocators.LINK_CREATE_RECIPE,
            10)

        # Клик по ссылке "Создать рецепт"
        self.click_element_by_script_by_xpath(
            CreateRecipePageLocators.LINK_CREATE_RECIPE
        )

        # Явное ожидание для загрузки страницы "Создание рецепта"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            CreateRecipePageLocators.HEADER_CREATING_RECIPE, 3
        )

        # Ввод данных для рецепта
        self.set_text_to_field_by_xpath(
            CreateRecipePageLocators.INPUT_NAME_RECIPE, TestData.NAME_RECIPE_TEXT
        )

        # Явное ожидание для загрузки чек-бокса "Завтрак"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            CreateRecipePageLocators.BUTTON_CHECK_BOX_BREAKFAST, 3
        )

        # Клик по чек-боксу "Завтрак"
        self.click_element_by_script_by_xpath(
            CreateRecipePageLocators.BUTTON_CHECK_BOX_BREAKFAST
        )

        self.set_text_to_field_by_xpath(
            CreateRecipePageLocators.INPUT_INGREDIENTS, TestData.INGREDIENTS_TEXT
        )

        # Явное ожидание для загрузки поля "яйца куриные"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            CreateRecipePageLocators.CHICKEN_EGGS, 3
        )

        # Клик по полю "яйца куриные"
        self.click_element_by_script_by_xpath(
            CreateRecipePageLocators.CHICKEN_EGGS
        )

        # Ввод данных в поле с граммами
        self.set_text_to_field_by_xpath(
            CreateRecipePageLocators.INGREDIENTS_GRAM, TestData.INGREDIENTS_GRAM_TEXT
        )

        # Клик по кнопке "Добавить ингредиент"
        self.click_element_by_script_by_xpath(
            CreateRecipePageLocators.BUTTON_ADD_INGREDIENT
        )

        # Ввод данных в поле "Время приготовления"
        self.set_text_to_field_by_xpath(
            CreateRecipePageLocators.COOKING_TIME, TestData.COOKING_TIME_TEXT
        )

        # Ввод данных в поле "Описание рецепта"
        self.set_text_to_field_by_xpath(
            CreateRecipePageLocators.RECIPE_DESCRIPTION, TestData.RECIPE_DESCRIPTION_TEXT
        )

    @allure.step('Загрузка фотографий')
    def upload_photos(self):
        self.scroll_to_element_by_xpath(CreateRecipePageLocators.BUTTON_CREATE_RECIPE)
        file_input = self.find_element_by_xpath(CreateRecipePageLocators.INPUT_PHOTO)
        self.driver.execute_script("arguments[0].style.display = 'block';", file_input)
        self.set_data_to_field_by_xpath(CreateRecipePageLocators.INPUT_PHOTO, TestData.PHOTO_1)

    @allure.step('Сохранение введенных данных')
    def save_form(self):
        self.click_element_by_xpath(CreateRecipePageLocators.BUTTON_CREATE_RECIPE)

    @allure.step('Проверка названия рецепта')
    def check_name_recipe(self):
        # Явное ожидание для загрузки карточки, созданного рецепта
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            CreateRecipePageLocators.HEADER_RECIPE,
            10)
        # Проверка URL-адреса на соответствие страницы логина
        return self.find_element_by_xpath(CreateRecipePageLocators.HEADER_RECIPE).text