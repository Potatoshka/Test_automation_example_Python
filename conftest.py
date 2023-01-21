import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def driver():
    driver_service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=driver_service)
    yield driver
    driver.quit()
