from selenium.webdriver.common.by import By

class WelcomePageLocators(object):
   LOGIN_BUTTON = (By.ID, "com.trello:id/log_in_button")

class LoginPageLocators(object):
   LOGIN_BUTTON = (By.ID, "com.trello:id/authenticate")
   EMAIL_INPUT = (By.ID, "com.trello:id/user")
   PASSWORD_INPUT = (By.ID, "com.trello:id/password")
   DIALOG_WINDOW = (By.ID, "com.trello:id/parentPanel")
   OK_MODAL_BUTTON = (By.ID, "android:id/button1")

class MainPageLocators(object):
   TOOLBAR = (By.ID, "com.trello:id/toolbar")
   HAMBURGER_BUTTON = (By.CLASS_NAME, "android.widget.ImageButton")
   TOOLBAR_TITLE = (By.CLASS_NAME, "android.widget.TextView")
   MENU = (By.ID, "com.trello:id/navigation_drawer")
   SETTINGS = (By.XPATH, "//*[@text='Settings']")
   BACKGROUND = (By.ID, "com.trello:id/decor_content_parent")


class SettingsPageLocators(MainPageLocators):
   LOG_OUT = (By.XPATH, "//*[@text='Log out']")
