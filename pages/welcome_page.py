from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators, LoginPageLocators, MainPageLocators, WelcomePageLocators

class WelcomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    '''
    Method check is page open
    '''
    def is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            WelcomePageLocators.LOGIN_BUTTON))
        return self.is_element_displayed(*WelcomePageLocators.LOGIN_BUTTON)

    '''
    Method for login in.
    '''
    def login(self):
        self.click(self.element(*WelcomePageLocators.LOGIN_BUTTON))
        return True
    