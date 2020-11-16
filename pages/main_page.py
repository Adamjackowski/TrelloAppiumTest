from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import *
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    '''
    Method for logging out
    For some reason sometimes the alert window is displayed. Then we logout with this window
    '''

    def logout(self):
        self.open_menu()
        WebDriverWait(self.driver, 30).until(lambda driver: self.is_element_displayed(*MainPageLocators.SETTINGS))
        self.click(self.element(*MainPageLocators.SETTINGS))
        WebDriverWait(self.driver, 30).until(lambda driver: 
            self.scroll_to_element(locator=SettingsPageLocators.LOG_OUT, direction="DOWN"))
        self.click(self.element(*SettingsPageLocators.LOG_OUT))
        return True


    def open_menu(self):
        if not self.is_element_displayed(*MainPageLocators.MENU):
            self.click(self.hamburger_button())
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
                (MainPageLocators.MENU)))
        return self.is_element_displayed(*MainPageLocators.MENU)
    

    def hamburger_button(self):
        return self.element(*MainPageLocators.TOOLBAR).find_element(*MainPageLocators.HAMBURGER_BUTTON)
    

    def toolbar_title(self):
        return self.element(*MainPageLocators.TOOLBAR).find_element(*MainPageLocators.TOOLBAR_TITLE)