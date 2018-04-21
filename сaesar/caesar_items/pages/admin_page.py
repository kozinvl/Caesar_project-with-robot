from selenium.common.exceptions import StaleElementReferenceException, \
    ElementNotVisibleException
from selenium.webdriver.common.by import By
from caesar_items.locators.locators import AdminPageLocators, \
    CreateEditUsersLocators, CreateEditGroupsLocators, \
    CreateEditStudentsLocators
from caesar_items.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resource.error_handler import logger_exception


class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @logger_exception
    def tab_users(self):
        """ Go to the users tab."""
        tab_users = self.driver.find_element(*AdminPageLocators.TAB_USERS)
        tab_users.click()
        return self

    @logger_exception
    def tab_groups(self):
        """ Go to the groups tab."""
        tab_groups = self.driver.find_element(*AdminPageLocators.TAB_GROUPS)
        tab_groups.click()
        return self

    @logger_exception
    def tab_students(self):
        """ Go to the students tab."""
        tab_students = self.driver.find_element(
            *AdminPageLocators.TAB_STUDENTS)
        tab_students.click()
        return self

    @logger_exception
    def add_entity_user(self):
        """ Add user in table."""
        add_entity = self.driver.find_element(*AdminPageLocators.ADD_USER)
        add_entity.click()
        return self

    @logger_exception
    def add_entity_group(self):
        """ Add group in table."""
        add_entity = self.driver.find_element(*AdminPageLocators.ADD_GROUP)
        add_entity.click()
        return self

    @logger_exception
    def add_entity_student(self):
        """ Add student in table."""
        add_entity = self.driver.find_element(*AdminPageLocators.ADD_STUDENT)
        add_entity.click()
        return self

    @logger_exception
    def back_home(self):
        """ Click on the button that will return to the Group page."""
        back_home = self.driver.find_element(*AdminPageLocators.BUTTON_ESCAPE)
        back_home.click()

    @logger_exception
    def fill_user_name(self, name):
        """ Filling user name field."""
        first_name = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "firstName")))
        first_name.click()
        first_name.send_keys(name, Keys.ENTER)
        return self

    @logger_exception
    def fill_user_second_name(self, second_name):
        """ Filling user second name field."""
        last_name = self.driver.find_element(
            *CreateEditUsersLocators.LAST_NAME)
        last_name.click()
        last_name.send_keys(second_name)
        return self

    @logger_exception
    def fill_user_role_type(self, role_type):
        """ Filling type role field."""
        role = self.driver.find_element(
            *CreateEditUsersLocators.ROLE)
        role.click()
        Select(role).select_by_visible_text(role_type)
        return self

    @logger_exception
    def fill_user_city(self, city):
        """ Filling location field."""
        location = self.driver.find_element(
            *CreateEditUsersLocators.LOCATION)
        location.click()
        Select(location).select_by_visible_text(city)
        return self

    @logger_exception
    def fill_user_photo(self, photo):
        """ Filling path to photography."""
        photograph = self.driver.find_element(*CreateEditUsersLocators.PHOTO)
        photograph.click()
        photograph.send_keys(photo)
        return self

    @logger_exception
    def fill_user_login(self, log_in):
        """ Filling login field."""
        login = self.driver.find_element(
            *CreateEditUsersLocators.LOGIN_FIELD)
        login.click()
        login.send_keys(log_in)
        return self

    @logger_exception
    def fill_user_password(self, secret):
        """ Filling password field."""
        password = self.driver.find_element(
            *CreateEditUsersLocators.PASSWORD_FIELD)
        password.click()
        password.send_keys(secret)
        return self

    @logger_exception
    def is_enabled_submit_button(self):
        """ Checking button availability."""
        return self.driver.find_element(
            *AdminPageLocators.BUTTON_SUBMIT).is_enabled()

    @logger_exception
    def fill_group_name(self, group_name):
        """ Filling group name field."""
        name = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "name")))
        name.click()
        name.send_keys(group_name, Keys.ENTER)
        return self

    @logger_exception
    def fill_group_geography(self, geography):
        """ Filling group's by location."""
        location = self.driver.find_element(
            *CreateEditGroupsLocators.LOCATION)
        location.click()
        Select(location).select_by_visible_text(geography)
        return self

    @logger_exception
    def fill_group_owner(self, owner):
        """ Filling group's owner by location."""
        if owner:
            budget_owner = self.driver.find_element(
                *CreateEditGroupsLocators.BUDGET)
            budget_owner.click()
        return self

    @logger_exception
    def fill_group_direct(self, direct):
        """ Filling group's by direction."""
        direction = self.driver.find_element(
            *CreateEditGroupsLocators.DIRECTION)
        direction.click()
        Select(direction).select_by_visible_text(direct)
        return self

    @logger_exception
    def fill_group_first_date(self, first_date):
        """ Filling group's by start date."""
        start_date = self.driver.find_element(
            *CreateEditGroupsLocators.START_DATE)
        start_date.click()
        start_date.send_keys(first_date)
        return self

    @logger_exception
    def fill_group_second_date(self, second_date):
        """ Filling group's by finish date."""
        finish_date = self.driver.find_element(
            *CreateEditGroupsLocators.FINISH_DATE)
        finish_date.send_keys(second_date)
        return self

    @logger_exception
    def fill_group_teacher_name(self, teacher_name):
        """ Filling group's by teacher."""
        teachers = self.driver.find_element(
            *CreateEditGroupsLocators.TEACHERS)
        teachers.click()
        teachers.send_keys(teacher_name)
        return self

    @logger_exception
    def fill_group_experts_name(self, experts_name):
        """ Filling group's by expert name."""
        expert = self.driver.find_element(
            *CreateEditGroupsLocators.EXPERTS)
        expert.click()
        expert.send_keys(experts_name)
        return self

    @logger_exception
    def fill_group_stage_level(self, stage_level):
        """ Filling group's by stage level."""
        stage = self.driver.find_element(
            *CreateEditGroupsLocators.STAGE)
        Select(stage).select_by_visible_text(stage_level)
        stage.click()
        return self

    @logger_exception
    def fill_student_group_id(self, group):
        """ Filling group's by stage level."""
        group_id = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "groupId")))
        group_id.click()
        group_id.send_keys(group, Keys.ENTER)
        return self

    @logger_exception
    def fill_student_name(self, first_name):
        """ Filling student's name."""
        name = self.driver.find_element(
            *CreateEditStudentsLocators.NAME)
        name.click()
        name.send_keys(first_name)
        return self

    @logger_exception
    def fill_student_last_name(self, second_name):
        """ Filling student's last name."""
        last_name = self.driver.find_element(
            *CreateEditStudentsLocators.LAST_NAME)
        last_name.click()
        last_name.send_keys(second_name)
        return self

    @logger_exception
    def fill_student_english_level(self, english):
        """ Filling student's english level."""
        english_level = self.driver.find_element(
            *CreateEditStudentsLocators.ENGLISH_LEVEL)
        english_level.click()
        Select(english_level).select_by_visible_text(english)
        return self

    @logger_exception
    def fill_student_cv_url(self, curriculum_vitae):
        """ Filling path to cv by url."""
        cv_url = self.driver.find_element(
            *CreateEditStudentsLocators.CV_URL)
        cv_url.click()
        cv_url.send_keys(curriculum_vitae)
        return self

    @logger_exception
    def fill_student_image(self, image_path):
        """ Filling path to image."""
        image = self.driver.find_element(
            *CreateEditStudentsLocators.IMAGE)
        image.click()
        image.send_keys(image_path)
        return self

    @logger_exception
    def fill_student_entry_score(self, score):
        """ Filling student's entry score."""
        entry_score = self.driver.find_element(
            *CreateEditStudentsLocators.ENTRY_SCORE)
        entry_score.click()
        entry_score.send_keys(score)
        return self

    @logger_exception
    def fill_student_approved_by(self, approved):
        """ Filling student's field where
        you will see who approved the student."""
        approved_by = self.driver.find_element(
            *CreateEditStudentsLocators.APPROVED_BY)
        approved_by.click()
        approved_by.send_keys(approved)
        return self

    @logger_exception
    def get_table(self, table_name: str):
        """ Getting all rows from table."""
        WebDriverWait(self.driver, 20,
                      ignored_exceptions=StaleElementReferenceException). \
            until(EC.presence_of_element_located((
            By.XPATH, AdminPageLocators.get_request_table(table_name))))
        CreateEditUsersLocators.wait_all_table()
        web_table = self.driver.find_elements(
            By.XPATH, AdminPageLocators.get_request_table(table_name))
        table_text = [web_element.text for web_element in web_table]
        table = [each.split(',') for each in table_text]
        return table

    @logger_exception
    def delete_last_entity(self):
        """ Deleting last entity who has been added recently"""
        button_path = self.get_last_delete_button()
        self.driver.find_element_by_xpath(button_path).click()
        return self

    @logger_exception
    def get_last_delete_button(self):
        """ Path to entity delete button who has been created recently."""
        WebDriverWait(self.driver, 20,
                      ignored_exceptions=ElementNotVisibleException). \
            until(EC.visibility_of_element_located
                  ((By.XPATH, CreateEditUsersLocators.DELETE_BUTTONS)))
        buttons = self.driver.find_elements(
            By.XPATH, CreateEditUsersLocators.DELETE_BUTTONS)
        number_delete_buttons = \
            len([element_btn.text for element_btn in buttons
                 if element_btn.text == 'Delete'])
        return CreateEditUsersLocators.DELETE_BUTTONS + "[{}]". \
            format(number_delete_buttons)

    @logger_exception
    def submit(self):
        """ Confirmation of entered data."""
        submit = self.driver.find_element(
            *AdminPageLocators.BUTTON_SUBMIT)
        submit.click()
        return self
