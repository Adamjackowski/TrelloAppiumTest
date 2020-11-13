from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators, LoginPageLocators, MainPageLocators

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    '''
    Method check is page open
    '''
    def is_opened(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            LoginPageLocators.LOGIN_BUTTON))
        return self.is_element_displayed(*LoginPageLocators.LOGIN_BUTTON)

    '''
    Method for login in.
    '''
    def proceed_with_email(self, email):
        self.type(self.element(*LoginPageLocators.EMAIL_INPUT), email)
        self.click(self.element(*LoginPageLocators.LOGIN_BUTTON))
        return True
    
    def proceed_with_password(self, password):
        self.type(self.element(*LoginPageLocators.PASSWORD_INPUT), password)
        return True
    

    def login(self):
        self.click(self.element(*LoginPageLocators.LOGIN_BUTTON))
        return True
    

    def is_login_suceed(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            MainPageLocators.TOOLBAR))
        return self.is_element_displayed(*MainPageLocators.TOOLBAR)
    
    def is_login_failed(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            LoginPageLocators.DIALOG_WINDOW))
        return self.is_element_displayed(*LoginPageLocators.DIALOG_WINDOW)
    
    
    def close_dialog(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            LoginPageLocators.DIALOG_WINDOW))
        self.click(self.element(*LoginPageLocators.OK_MODAL_BUTTON))
        return self.is_opened()


    