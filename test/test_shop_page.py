import time

from page.user_page import UserFormPage


class TestUserFormPage:
    class TestUserForm:

        def test_change_user_data(self, driver):
            user_page = UserFormPage(driver, 'https://shop.by/')
            user_page.open()
            user_page.enter_user_page()


