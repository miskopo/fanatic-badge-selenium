from os import environ
from time import sleep

from selenium.webdriver import Firefox

from .logger import logger

environ['MOZ_HEADLESS'] = '1'


class FanaticBadge:
    def __init__(self):
        self.driver = Firefox()
        self.url = "https://stackoverflow.com/users/6215116/michal-polovka"
        self.credentials = self.load_login_credentials_from_environ()

    @staticmethod
    def load_login_credentials_from_environ() -> (str, str):
        try:
            login = environ['SO_LOGIN']
            password = environ['SO_PASSWORD']
        except KeyError:
            logger.error("Credentials not found in env")
            exit(1)
        else:
            return login, password

    def navigate_to_user_page(self):
        logger.info("Navigating to login page")
        self.driver.get("https://stackoverflow.com/users/login")

        logger.info("Filling in email")
        email = self.driver.find_element_by_id("email")
        email.send_keys(self.credentials[0])

        logger.info("Filling in password")
        password = self.driver.find_element_by_id("password")
        password.send_keys(self.credentials[1])

        logger.info("Sending form")
        submit = self.driver.find_element_by_id("submit-button")
        submit.submit()

        logger.info("Navigating to user page")
        self.driver.get(self.url)
        sleep(5)

        logger.info("Navigating to profile page")
        self.driver.get("{}?tab=profile".format(self.url))
        sleep(5)

        logger.info("Done")

