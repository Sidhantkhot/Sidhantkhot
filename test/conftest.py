
import pytest
from selenium import webdriver

# def test_1(setup):
#     assert 3 + 5 == 8
#
#
# def test_2(setup):
#     assert 4 + 6 == 10
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or edge")


class Base:
    pass


@pytest.fixture(scope="class", autouse=True)
def setup(browser, request):
    if browser == "chrome":
        print("chrome")
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "edge":
        print("edge")
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        pass

    driver.get("https://google.com/")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


class Base():
    def __int__(self, driver):
        self.driver = driver
