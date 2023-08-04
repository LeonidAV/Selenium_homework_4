import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from base.base_class import Base

user_list = ["standard_user",
             "locked_out_user",
             "problem_user",
             "performance_glitch_user",
             ]


class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    login = "//*[@id='user-name']"
    password = "//input[@name='password']"
    enter = "//*[@id='login-button']"
    menu = "//*[@id='react-burger-menu-btn']"
    logout = "//*[@id='logout_sidebar_link']"

    """Getters"""

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_logout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.logout)))

    """Actions"""

    def input_login(self, login):
        self.get_login().clear()
        time.sleep(1)
        self.get_login().send_keys(login)
        print("Ввод логина")

    def input_password(self, password):
        self.get_password().clear()
        time.sleep(1)
        self.get_password().send_keys(password)
        print("Ввод пароля")

    def click_enter(self):
        self.get_enter().click()
        print("Нажатие кнопки войти")

    def click_menu(self):
        self.get_menu().click()
        print("Нажатие кнопки меню")

    def click_logout(self):
        self.get_logout().click()
        print("Нажатие кнопки выхода")

    """Methods"""

    def authorization(self, user_list):
        for name in user_list:
            try:
                self.input_login(name)
                self.input_password("secret_sauce")
                self.click_enter()
                self.click_menu()
                self.click_logout()
                time.sleep(2)
            except TimeoutException:
                message = 'Epic sadface: Sorry, this user has been locked out.'
                print(message)
