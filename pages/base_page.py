import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента по XPATH')
    def find_element_by_xpath(self, xpath):
        # Поиск и выдача элемента
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step('Явное ожидание появления элемента по XPATH с заданным таймаутом')
    def wait_for_visibility_of_element_by_xpath_by_timeout(self, xpath, timeout):
        # Явное ожидание для загрузки страницы
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )

    @allure.step('Явное ожидание загрузки ресурса с заданным таймаутом')
    def wait_for_loading_url_by_timeout(self, url, timeout):
        # Явное ожидание для загрузки URL
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )

    @allure.step('Прокрутка страницы до элемента по XPATH')
    def scroll_to_element_by_xpath(self, xpath):
        # Поиск элемента
        element = self.driver.find_element(By.XPATH, xpath)

        # Прокрутка страницы до элемента
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик по элементу по XPATH')
    def click_element_by_xpath(self, xpath):
        # Поиск элемента и клик по нему
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step('Клик по элементу через скрипт по XPATH')
    def click_element_by_script_by_xpath(self, xpath):
        # Поиск элемента
        element = self.driver.find_element(By.XPATH, xpath)

        # Клик по элементу
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод текста в поле по XPATH')
    def set_text_to_field_by_xpath(self, xpath, text):
        # Поиск поля и ввод данных в него
        self.driver.find_element(By.XPATH, xpath).send_keys(text)

    @allure.step('Проверка адреса страницы')
    def check_url(self, url):
        # Явное ожидание для загрузки новой страницы
        self.wait_for_loading_url_by_timeout(url, 10)

        # Сравнение текущего URL с переданным
        assert self.driver.current_url == url

    @allure.step('Ввод данных в поле по XPATH')
    def set_data_to_field_by_xpath(self, xpath, data, timeout=3):
        # поиск поля и ввод данных
        self.wait_for_visibility_of_element_by_xpath_by_timeout(xpath, timeout)
        self.driver.find_element(By.XPATH, xpath).send_keys(str(data))


