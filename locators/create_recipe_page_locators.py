class CreateRecipePageLocators:

    # Заголовок «Рецепты»
    HEADER_REGISTRATION = '//h1[text()="Рецепты"]'
    # Раздел «Создать рецепт»
    LINK_CREATE_RECIPE = '//a[text()="Создать рецепт"]'
    # Заголовок «Создание рецепта»
    HEADER_CREATING_RECIPE = '//h1[text()="Создание рецепта"]'
    # Поле ввода «Название рецепта»
    INPUT_NAME_RECIPE = '//div[text()="Название рецепта"]/following-sibling::input'
    # Чек-бокс «Завтрак»
    BUTTON_CHECK_BOX_BREAKFAST = '//span[text()="Завтрак"]/preceding-sibling::button'
    # Поле ввода «Ингредиенты»
    INPUT_INGREDIENTS = '//div[text()="Ингредиенты"]/following-sibling::input'
    # Поле «Яйца куриные»
    CHICKEN_EGGS = '//div[text()="яйца куриные"]'
    # Поле «г»
    INGREDIENTS_GRAM = '//div[contains(@class, "ingredientsAmountInputContainer")]//input'
    # Кнопка «Добавить ингредиент»
    BUTTON_ADD_INGREDIENT = '//div[text()="Добавить ингредиент"]'
    # Поле ввода «Время приготовления»
    COOKING_TIME = '//div[text()="Время приготовления"]/following-sibling::input'
    # Поле ввода «Описание рецепта»
    RECIPE_DESCRIPTION = '//div[text()="Описание рецепта"]/following-sibling::textarea'
    # Поле загрузки фото
    INPUT_PHOTO = '//label[text()="Загрузить фото"]/following-sibling::input'
    # Кнопка «Создать рецепт»
    BUTTON_CREATE_RECIPE = '//button[text()="Создать рецепт"]'
    # Заголовок «Создание рецепта»
    HEADER_RECIPE = '//h1[text()="Бодрый завтрак"]'




    # Поле ввода «Фамилия»
    INPUT_SURNAME = '//div[text()="Фамилия"]/following-sibling::input'
    # Поле ввода «Имя пользователя»
    INPUT_USER_NAME = '//div[text()="Фамилия"]/following-sibling::input'
    # Поле ввода «Арес электронной почты»
    INPUT_EMAIL = '//div[text()="Адрес электронной почты"]/following-sibling::input'
    # Поле ввода «Пароль»
    INPUT_PASSWORD = '//div[text()="Пароль"]/following-sibling::input'


    # Модальное окно
    #MODAL_WINDOW = [
        #'.//section[contains(@class, "Modal_modal__P3_V5")]',
        #'.//div[contains(@class, "Modal_modal_overlay__x2ZCr")]'
    #]
    # Секция истории заказов
    #SECTION_ORDER_HISTORY = './/div[contains(@class, "OrderHistory")]'





