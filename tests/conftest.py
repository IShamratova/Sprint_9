import pytest
from selenium import webdriver
from data.data import TestData


@pytest.fixture
def driver():
    # Настроим WebDriver
    driver = webdriver.Chrome()

    # Устанавливаем позицию окна в левый верхний угол
    driver.set_window_position(0, 0)

    # Устанавливаем размер окна
    driver.set_window_size(1280, 800)

    # Открытие страницы тестового стенда
    driver.get(TestData.BASE_URL)

    yield driver

    # Закрытие браузера после теста
    driver.quit()