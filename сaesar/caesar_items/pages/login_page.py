from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from caesar_items.pages.base_page import BasePage
from caesar_items.locators.locators import LogInLocators, GroupPageLocators
from caesar_items.pages.groups_page import GroupsPage


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_login_field_text(self, user_login=''):
        """ Enter user login in login field."""
        login_field = self.driver.find_element(*LogInLocators.LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(user_login)

    def set_password_field_text(self, user_password=''):
        """ Enter user password in password field."""
        password_field = self.driver.\
            find_element(*LogInLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(user_password)

    def get_message_text(self):
        """ Get error message above login field."""
        return self.driver.find_element(*LogInLocators.FIELD_MESSAGE).text

    def submit_button(self):
        """ Get submit button web element."""
        return self.driver.find_element(*LogInLocators.CONFIRM_ACTION)

    def click_submit_button(self):
        """ Click on submit button and wait for user photo."""
        self.driver.find_element(*LogInLocators.CONFIRM_ACTION).click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(GroupPageLocators.USER_PHOTO))
            return GroupsPage(self.driver)
        except Exception:
            return self

    def auto_login(self, user):
        """ Custom function to login on site."""
        self.set_login_field_text(user.login)
        self.set_password_field_text(user.password)
        return self.click_submit_button()

    def login_use_tab_n_enter_keys(self, user):
        """ Login on site using Enter and Tab keys."""
        ActionChains(self.driver).send_keys(user.login).send_keys(Keys.TAB) \
            .send_keys(user.password).send_keys(Keys.ENTER).perform()
        WebDriverWait(self.driver, 5).\
            until(EC.visibility_of_element_located(GroupPageLocators.USER_PHOTO))
        return GroupsPage(self.driver)


