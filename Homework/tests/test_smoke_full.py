import time

from selenium import webdriver

from pages_test.login_page import Login_page
from pages_test.main_page import Main_page


def test_auto():
    driver = webdriver.Chrome(executable_path='D:\\Хом драйвер и геко\\chromedriver_win32\\chromedriver.exe')

    print("Начало теста")

    en = Main_page(driver)
    en.main()

    login = Login_page(driver)
    login.authorization()

    print("Конец")
    time.sleep(5)
    driver.quit()
