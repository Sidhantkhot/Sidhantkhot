import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from test.conftest import Base


class Google(Base):
    def __int__(self, driver):
        super().__int__(driver)

    def google_search(self, sname):
        self.driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys(sname, Keys.ENTER)
        time.sleep(2)
