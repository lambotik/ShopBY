import random
import time

import pyautogui

import login
from generator.generator import generated_person
from locators.shop_page_locators import UserPageLocators
from page.base_page import BasePage


class UserFormPage(BasePage):
    locators = UserPageLocators()

    def enter_user_page(self):
        self.element_is_visible(self.locators.USER_ENTER).click()
        self.element_is_visible(self.locators.EMAIL_TAB).click()
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(login.LoginData.email)
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(login.LoginData.password)
        self.element_is_visible(self.locators.ENTER_BUTTON).click()
        self.element_is_visible(self.locators.USER_ICON).click()
        self.element_is_visible(self.locators.SETTINGS).click()

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
        return self.elements_is_clickable(self.locators.SAVE_BUTTON)

    def get_save_text(self):
        save_text = self.element_is_visible(self.locators.SAVE_DONE)
        print(save_text.text)
        return save_text

    def wait_current_data(self):
        phone_number = self.element_is_visible(self.locators.PHONE_NUMBER).get_attribute('defaultvalue')
        while phone_number == None:
            self.driver.implicitly_wait(5)
            break
        print(f'Phone: {phone_number}')

    def generate_new_user_data(self):
        person_info = next(generated_person())
        # nick_name = person_info.first_name
        first_name = person_info.first_name
        last_name = person_info.last_name
        # self.element_is_visible(self.locators.INPUT_NICK_NAME).clear()
        self.element_is_visible(self.locators.INPUT_FIRST_NAME).clear()
        self.element_is_visible(self.locators.INPUT_LAST_NAME).clear()
        # self.element_is_visible(self.locators.INPUT_NICK_NAME).send_keys(nick_name)
        self.element_is_visible(self.locators.INPUT_FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.INPUT_LAST_NAME).send_keys(last_name)
        return first_name, last_name

    def change_user_date(self):
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
        self.element_is_visible(self.locators.MONTH).click()
        month = random.choice(data_month)
        pyautogui.typewrite(f'{month}')
        pyautogui.press("return")
        self.element_is_visible(self.locators.YEAR).click()
        year = random.choice(data_year)
        pyautogui.typewrite(f'{year}')
        pyautogui.press("return")
        return date, month, year

    # Methods

    def change_user_data(self):
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
        change_done = self.get_save_text()
        assert change_done == 'Личные данные сохранены', 'Changes were not saved'
        assert (current_first_name, current_last_name) != (
            new_first_name, new_last_name), 'First Name and Last Name has not been changed'
        print(int(current_day), current_month, int(current_year))
        print(int(date), month, int(year))
        assert (int(current_day), current_month, int(current_year)) != \
               (int(date), month, int(year))

    def change_gender(self):
        cur_gender = self.get_current_gender()
        if cur_gender == self.element_is_visible(self.locators.USER_GENDER_M).text:
            self.element_is_visible(self.locators.USER_GENDER_W).click()
        else:
            self.element_is_visible(self.locators.USER_GENDER_M).click()
        print(self.get_current_gender())
        self.get_save_button().click()
        self.get_save_text()
        return cur_gender

    def change_password(self):
        self.element_is_visible(self.locators.CHANGE_PASSWORD).click()
        new = self.element_is_visible(self.locators.NEW_PASSWORD).send_keys('123456789')
        repeat = self.element_is_visible(self.locators.REPEAT_PASSWORD).send_keys('123456789')
        self.elements_is_clickable(self.locators.BUTTON_SAVE_PASSWORD).click()
        message = self.element_is_visible(self.locators.MESSAGE).text
        return message

    def enter_short_password(self):
        self.element_is_visible(self.locators.CHANGE_PASSWORD).click()
        new = self.element_is_visible(self.locators.NEW_PASSWORD).send_keys('1234567')
        repeat = self.element_is_visible(self.locators.REPEAT_PASSWORD).send_keys('1234567')
        time.sleep(5)
        self.elements_is_clickable(self.locators.BUTTON_SAVE_PASSWORD).click()
        message = self.element_is_visible(self.locators.MESSAGE).text
        print(message)
        return message


    def enter_without_email(self):
        self.element_is_visible(self.locators.USER_ENTER).click()
        self.element_is_visible(self.locators.EMAIL_TAB).click()
        self.element_is_visible(self.locators.INPUT_EMAIL).clear()
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(login.LoginData.password)
        self.element_is_visible(self.locators.ENTER_BUTTON).click()
        alert = self.element_is_visible(self.locators.ALERT_MESSAGE).text
        print(alert)
        return alert

    def enter_without_password(self):
        self.element_is_visible(self.locators.USER_ENTER).click()
        self.element_is_visible(self.locators.EMAIL_TAB).click()
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(login.LoginData.email)
        self.element_is_visible(self.locators.INPUT_PASSWORD).clear()
        self.element_is_visible(self.locators.ENTER_BUTTON).click()
        alert = self.element_is_visible(self.locators.ALERT_MESSAGE).text
        print(alert)
        return alert

