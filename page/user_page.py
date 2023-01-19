import random
import time

import pyautogui

import login
from generator.generator import generated_person
from locators.shop_page_locators import UserPageLocators
from page.base_page import BasePage
from utilities.logger import Logger


class UserFormPage(BasePage):
    locators = UserPageLocators()

    # Getters

    def get_phone_number(self):
        return self.element_is_visible(self.locators.PHONE_NUMBER).get_attribute('defaultvalue')

    def get_nick_name(self):
        return self.element_is_visible(self.locators.INPUT_NICK_NAME).get_attribute('defaultvalue')

    def get_first_name(self):
        return self.element_is_visible(self.locators.INPUT_FIRST_NAME).get_attribute('defaultvalue')

    def get_last_name(self):
        return self.element_is_visible(self.locators.INPUT_LAST_NAME).get_attribute('defaultvalue')

    def get_current_date(self):
        return self.element_is_visible(self.locators.SELECT_USER_DATE).get_attribute('defaultvalue')

    def get_current_month(self):
        return self.element_is_visible(self.locators.SELECT_USER_MONTH).get_attribute('defaultvalue')

    def get_current_month_text(self):
        index = self.element_is_visible(self.locators.SELECT_USER_MONTH).get_attribute('defaultvalue')
        int_index = int(index)
        month_list = self.element_is_visible(self.locators.SELECT_USER_MONTH).text
        m = month_list.split('\n')
        return m[int_index]

    def get_current_year(self):
        return self.element_is_visible(self.locators.SELECT_USER_YEAR).get_attribute('defaultvalue')

    def get_current_gender(self):
        return self.element_is_visible(self.locators.SELECTED_USER_GENDER).text

    def get_save_button(self):
        self.go_to_element(self.elements_is_clickable(self.locators.SAVE_BUTTON))
        return self.elements_is_clickable(self.locators.SAVE_BUTTON)

    def get_save_text(self):
        save_text = self.element_is_visible(self.locators.SAVE_DONE).text
        return save_text

    def wait_current_data(self):
        phone_number = self.element_is_visible(self.locators.PHONE_NUMBER).get_attribute('defaultvalue')
        while phone_number == None:
            self.driver.implicitly_wait(5)
            break
        print(f'Phone: {phone_number}')

    def enter_user_page(self):
        Logger.add_start_step(method='enter_user_page')
        self.element_is_visible(self.locators.USER_ENTER).click()
        print('Click icon enter')
        self.element_is_visible(self.locators.EMAIL_TAB).click()
        print('Click Email')
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(login.LoginData.email)
        print(f'Enter your email address')
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(login.LoginData.password)
        print('Enter your password')
        self.element_is_visible(self.locators.ENTER_BUTTON).click()
        print('Click Button Enter')
        self.element_is_visible(self.locators.USER_ICON).click()
        print('Click User Icon')
        self.element_is_visible(self.locators.SETTINGS).click()
        print('Click Settings')
        Logger.add_end_step(url=self.driver.current_url, method='enter_user_page')

    def generate_new_user_data(self):
        Logger.add_start_step(method='generate_new_user_data')
        person_info = next(generated_person())
        # nick_name = person_info.first_name
        first_name = person_info.first_name
        last_name = person_info.last_name
        # self.element_is_visible(self.locators.INPUT_NICK_NAME).clear()
        self.element_is_visible(self.locators.INPUT_FIRST_NAME).clear()
        print('Clear field first name')
        self.element_is_visible(self.locators.INPUT_LAST_NAME).clear()
        print('Clear field last name')
        # self.element_is_visible(self.locators.INPUT_NICK_NAME).send_keys(nick_name)
        self.element_is_visible(self.locators.INPUT_FIRST_NAME).send_keys(first_name)
        print('Enter the generated name')
        self.element_is_visible(self.locators.INPUT_LAST_NAME).send_keys(last_name)
        print('Enter the generated last name')
        Logger.add_end_step(url=self.driver.current_url, method='generate_new_user_data')
        return first_name, last_name

    def change_user_date(self):
        Logger.add_start_step(method='change_user_date')
        date_list = self.elements_are_visible(self.locators.LIST_DATE)
        data_day = []
        for day in date_list:
            data_day.append(day.text)
        month_list = self.elements_are_visible(self.locators.LIST_MONTH)
        data_month = []
        for month in month_list:
            data_month.append(month.text)
        year_list = self.elements_are_visible(self.locators.LIST_YEAR)
        data_year = []
        for year in year_list:
            data_year.append(year.text)
        self.element_is_visible(self.locators.DATE).click()
        date = random.choice(data_day)
        pyautogui.typewrite(f'{date}')
        pyautogui.press("return")
        print('Enter random date')
        self.element_is_visible(self.locators.MONTH).click()
        month = random.choice(data_month)
        pyautogui.typewrite(f'{month}')
        pyautogui.press("return")
        print('Enter random month')
        self.element_is_visible(self.locators.YEAR).click()
        year = random.choice(data_year)
        pyautogui.typewrite(f'{year}')
        pyautogui.press("return")
        print('Enter random year')
        Logger.add_end_step(url=self.driver.current_url, method='change_user_date')
        return date, month, year

    # Methods

    def change_user_data(self):
        Logger.add_start_step(method='change_user_data')
        self.wait_current_data()
        current_day = self.get_current_date()
        current_month = self.get_current_month_text()
        current_year = self.get_current_year()
        date, month, year = self.change_user_date()
        current_nick = self.get_nick_name()
        current_first_name = self.get_first_name()
        current_last_name = self.get_last_name()
        new_first_name, new_last_name = self.generate_new_user_data()
        print('Current Nick:', current_nick, '\nCurrent Name:', current_first_name, '\nCurrent Last Name:',
              current_last_name)
        print('New Name:', new_first_name, '\nNew Last Name:', new_last_name)
        self.get_save_button().click()
        print('Click Button Save')
        change_done = self.get_save_text()
        assert change_done == 'Личные данные сохранены', 'Changes were not saved'
        assert (f'{current_first_name}{current_last_name}') != (
            f'{new_first_name}{new_last_name}'), 'First Name and Last Name has not been changed'
        print('Date before : ', int(current_day), current_month, int(current_year))
        print('Date after : ', int(date), month, int(year))
        assert (int(current_day), current_month, int(current_year)) != \
               (int(date), month, int(year))
        print(f'{change_done}')
        Logger.add_end_step(url=self.driver.current_url, method='change_user_data')

    def change_gender(self):
        Logger.add_start_step(method='change_gender')
        cur_gender = self.get_current_gender()
        if cur_gender == self.element_is_visible(self.locators.USER_GENDER_M).text:
            print('Current gender man')
            self.element_is_visible(self.locators.USER_GENDER_W).click()
            print('Click gender woman')
        else:
            print('Current gender woman')
            self.element_is_visible(self.locators.USER_GENDER_M).click()
            print('Click gender man')
        print(self.get_current_gender())
        self.get_save_button().click()
        print('Click Button Save')
        self.get_save_text()
        Logger.add_end_step(url=self.driver.current_url, method='change_gender')
        return cur_gender

    def change_password(self):
        Logger.add_start_step(method='change_password')
        self.element_is_visible(self.locators.CHANGE_PASSWORD).click()
        print('Click change password')
        new = self.element_is_visible(self.locators.NEW_PASSWORD).send_keys('123456789')
        repeat = self.element_is_visible(self.locators.REPEAT_PASSWORD).send_keys('123456789')
        self.elements_is_clickable(self.locators.BUTTON_SAVE_PASSWORD).click()
        message = self.element_is_visible(self.locators.MESSAGE).text
        Logger.add_end_step(url=self.driver.current_url, method='change_password')
        return message

    def enter_short_password(self):
        Logger.add_start_step(method='enter_short_password')
        self.element_is_visible(self.locators.CHANGE_PASSWORD).click()
        print('Click change password')
        new = self.element_is_visible(self.locators.NEW_PASSWORD).send_keys('1234567')
        print(f'Enter short password {new}')
        repeat = self.element_is_visible(self.locators.REPEAT_PASSWORD).send_keys('1234567')
        print(f'Repeat short password {repeat}')
        self.elements_is_clickable(self.locators.BUTTON_SAVE_PASSWORD).click()
        print('Click Button Save')
        message = self.element_is_visible(self.locators.MESSAGE).text
        print(message)
        Logger.add_end_step(url=self.driver.current_url, method='enter_short_password')
        return message

    def enter_without_email(self):
        Logger.add_start_step(method='enter_without_email')
        self.element_is_visible(self.locators.USER_ENTER).click()
        self.element_is_visible(self.locators.EMAIL_TAB).click()
        self.element_is_visible(self.locators.INPUT_EMAIL).clear()
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(login.LoginData.password)
        self.element_is_visible(self.locators.ENTER_BUTTON).click()
        alert = self.element_is_visible(self.locators.ALERT_MESSAGE).text
        print(alert)
        Logger.add_end_step(url=self.driver.current_url, method='enter_without_email')
        return alert

    def enter_without_password(self):
        Logger.add_start_step(method='enter_without_password')
        self.element_is_visible(self.locators.USER_ENTER).click()
        self.element_is_visible(self.locators.EMAIL_TAB).click()
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(login.LoginData.email)
        self.element_is_visible(self.locators.INPUT_PASSWORD).clear()
        self.element_is_visible(self.locators.ENTER_BUTTON).click()
        alert = self.element_is_visible(self.locators.ALERT_MESSAGE).text
        print(alert)
        Logger.add_end_step(url=self.driver.current_url, method='enter_without_password')
        return alert
