from pathlib import Path


class TestData:
    # Папка корня проекта
    BASE_DIR = Path(__file__).resolve().parent.parent

    # URL тестового стенда
    BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru"
    BASE_REGISTRATION_URL = BASE_URL + "/signup"
    BASE_LOGIN_URL = BASE_URL + "/signin"
    BASE_RECIPES_URL = BASE_URL + "/recipes"


    # Список имен
    NAMES = ["Ivan", "Anna", "Maria", "Petr", "Olga", "Artyom"]

    # Список фамилий
    SURNAMES = ["Ivanov", "Petrov", "Sidorov", "Smirnov", "Komarov", "Mikhaylov"]

    # Список доменов почтовых служб
    EMAIL_DOMAINS = ["yandex.ru", "mail.ru", "gmail.com", "example.com", "test.com"]

    # Тестовые данные для входа зарегистрированного пользователя
    NAME = "Ivan"
    SURNAME = "Ivanov"
    USER_NAME = "IvIv"
    EMAIL = "ivan-ivanov6969@yandex.ru"
    PASSWORD = "Iv696969"

    # Тестовые данные ингредиентов
    NAME_RECIPE_TEXT = "Бодрый завтрак"
    INGREDIENTS_TEXT = "яйца"
    INGREDIENTS_GRAM_TEXT = "200"
    COOKING_TIME_TEXT = "15"
    RECIPE_DESCRIPTION_TEXT = "Сварить яйца"
    PHOTO_1 = BASE_DIR / "data" / "shell.png"


