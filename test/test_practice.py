import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from test.conftest import Base
from test.google_page import Google

pytest.mark.usefixtures("setup")

# @ddt
class TestDemo(Base):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.g = Google()

    # @data(("stranger things","sam","coldplay"))
    # @unpack
    def test_01(self):
        self.driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("stranger things", Keys.ENTER)
        time.sleep(2)
        # self.driver.find_element(By.XPATH, "(//input[@name='btnK'])[2]").click
        time.sleep(3)
        # self.g.google_search("stranger things")
        assert self.driver.title == "stranger things - Google Search"

    def test_02(self):
        assert 2 + 2 == 4
