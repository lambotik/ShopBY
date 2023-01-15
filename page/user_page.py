import login
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



