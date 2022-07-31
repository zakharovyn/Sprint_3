from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1400,900')

# Переход в личный кабинет проверяется при тесте авторизации для подтвеждения корректности входа в аккаунт, можно добавить,
# но тесты идентичны, смысла дублировать не вижу

class TestTransition:

    def test_click_on_the_constructor_button_from_your_personal_account(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 3)

        wait.until(EC.presence_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, './/fieldset[1]//input'))).send_keys('zakharovyan1003@yandex.ru')
        wait.until(EC.element_to_be_clickable((By.XPATH, './/fieldset[2]//input'))).send_keys('Qwerty123')
        wait.until(EC.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]'))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, './/a[@href="/account"]'))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, './/li/a[@href="/"]'))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, '.// h1[text() = "Соберите бургер"]')))
        assert driver.current_url==f"https://stellarburgers.nomoreparties.site/"

        driver.quit()


    def test_transition_by_clicking_on_the_Stellar_Burgers_logo(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 3)

        wait.until(EC.presence_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, './/fieldset[1]//input'))).send_keys('zakharovyan1003@yandex.ru')
        wait.until(EC.element_to_be_clickable((By.XPATH, './/fieldset[2]//input'))).send_keys('Qwerty123')
        wait.until(EC.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]'))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, './/a[@href="/account"]'))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, './/div/a[@href="/"]'))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, '.// h1[text() = "Соберите бургер"]')))
        assert driver.current_url==f"https://stellarburgers.nomoreparties.site/"

        driver.quit()