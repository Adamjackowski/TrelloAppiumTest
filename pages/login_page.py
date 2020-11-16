from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import LoginPageAttlassianLocators, LoginPageLocators, LoginPageLocators, MainPageLocators

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
    def proceed_with_email(self, email, attlasian=True):
        self.type(self.element(*LoginPageLocators.EMAIL_INPUT), email)
        self.click(self.element(*LoginPageLocators.LOGIN_BUTTON))
        if attlasian:
            WebDriverWait(self.driver, 60).until(lambda driver: len(self.driver.contexts) > 1)
            self.driver.switch_to.context(self.driver.contexts[1])
        return True
    
    def proceed_with_password(self, password, attlasian=True, first_login=False):
        if attlasian:
            if not first_login:
                WebDriverWait(self.driver, 30).until(lambda driver: self.is_element_displayed(*LoginPageAttlassianLocators.ADD_ANOTHER_BUTTON))
                self.click(self.element(*LoginPageAttlassianLocators.ADD_ANOTHER_BUTTON))
            WebDriverWait(self.driver, 30).until(lambda driver: self.is_element_displayed(*LoginPageAttlassianLocators.LOGIN_BUTTON))
            self.click(self.element(*LoginPageAttlassianLocators.LOGIN_BUTTON))
            self.type(self.element(*LoginPageAttlassianLocators.PASSWORD_INPUT), password)
        else:
            self.type(self.element(*LoginPageLocators.PASSWORD_INPUT), password)
        return True
    

    def login(self, attlasian=True):
        if attlasian:
            self.click(self.element(*LoginPageAttlassianLocators.LOGIN_BUTTON))
            #WebDriverWait(self.driver, 60).until(lambda driver: len(self.driver.contexts) == 1)
            self.driver.switch_to.context(self.driver.contexts[0])
        else:
            self.click(self.element(*LoginPageLocators.LOGIN_BUTTON))
        return True
    

    def is_login_suceed(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
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
        return True


    