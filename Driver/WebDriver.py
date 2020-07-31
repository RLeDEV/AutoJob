import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class WebDriver:

    class __WebDriver:
        def __init__(self):
            options = Options()
            options.headless = True
            self.driver = webdriver.Firefox(options=options,executable_path=r'./geckodriver.exe')

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver