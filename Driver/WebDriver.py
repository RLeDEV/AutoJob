import yaml
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class WebDriver:

    class __WebDriver:
        def __init__(self):
            options = Options()
            options.headless = True
            with open("./Driver/config.yml", "r") as yml:
                cfg = yaml.load(yml, Loader=yaml.FullLoader)
            self.driver = webdriver.Firefox(options=options,executable_path=cfg["selenium"]["geckodriver_path"])
            
    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver