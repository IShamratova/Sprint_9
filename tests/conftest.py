import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data.data import TestData
import tempfile


@pytest.fixture
def driver():
    # Создаём уникальную временную директорию
    user_data_dir = tempfile.mkdtemp()

    # Настраиваем опции Chrome
    options = Options()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Настраиваем WebDriver
    driver = webdriver.Chrome(options=options)

    # Устанавливаем позицию окна в левый верхний угол
    driver.set_window_position(0, 0)

    # Устанавливаем размер окна
    driver.set_window_size(1280, 800)

    # Открываем страницу тестового стенда
    driver.get(TestData.BASE_URL)

    yield driver

    # Закрываем браузер после теста
    driver.quit()