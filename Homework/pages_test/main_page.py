from base.base_class import Base


class Main_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def main(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
