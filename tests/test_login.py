from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from tests.conftest import driver
from pages.welcome_page import WelcomePage
from tests.test_base import TestBase
from appium import webdriver
import pytest

class TestLogin(TestBase):
  def test_login_success(self, driver):
    welcome_page = WelcomePage(driver)
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    assert welcome_page.is_opened()
    assert welcome_page.login()
    assert login_page.is_opened()
    assert login_page.proceed_with_email(TestBase.data()['existing_login'])
    assert login_page.proceed_with_password(TestBase.data()['existing_password'])
    assert login_page.login()
    assert login_page.is_login_suceed()
    assert main_page.logout()
    assert welcome_page.is_opened()
    
  def test_login_fail(self, driver):
    
    welcome_page = WelcomePage(driver)
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    assert welcome_page.is_opened()
    assert welcome_page.login()
    assert login_page.is_opened()
    assert login_page.proceed_with_email(TestBase.data()['not_existing_login'], attlasian=False)
    assert login_page.proceed_with_password(TestBase.data()['not_existing_password'], attlasian=False)
    assert login_page.login(attlasian=False)
    assert login_page.is_login_failed()
    assert login_page.close_dialog()