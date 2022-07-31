from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1400,900')


class TestConstructor:

    def test_transition_to_the_buns_section(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 3)

        wait.until(EC.element_to_be_clickable((By.XPATH, './/div/span[text()="Начинки"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, './/h2[text()="Начинки"]')))

        wait.until(EC.element_to_be_clickable((By.XPATH, './/div/span[text()="Булки"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, './/h2[text()="Булки"]')))

        driver.quit()


    def test_transition_to_the_sauces_section(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 3)

        wait.until(EC.element_to_be_clickable((By.XPATH, './/div/span[text()="Соусы"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, './/h2[text()="Соусы"]')))

        driver.quit()


    def test_transition_to_the_fillings_section(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 3)

        wait.until(EC.element_to_be_clickable((By.XPATH, './/div/span[text()="Начинки"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, './/h2[text()="Начинки"]')))

        driver.quit()