from page.user_page import UserFormPage


class TestUserFormPage:
    class TestLoginPage:
        def test_enter_without_email(self, driver):
            login_page = UserFormPage(driver, 'https://shop.by/')
            login_page.open()
            alert = login_page.enter_without_email()
            assert alert == 'Такого аккаунта не существует либо используется другой способ авторизации', \
                'Should be alert message about email'

        def test_enter_without_password(self, driver):
            login_page = UserFormPage(driver, 'https://shop.by/')
            login_page.open()
            alert = login_page.enter_without_password()
            assert alert == 'Неверный e-mail или пароль.', 'Should be alert message about password'

    class TestUserForm:

        def test_change_user_data(self, driver):
            user_page = UserFormPage(driver, 'https://shop.by/')
            user_page.open()
            user_page.enter_user_page()
            user_page.change_user_data()

        def test_user_can_change_gender(self, driver):
            user_page = UserFormPage(driver, 'https://shop.by/')
            user_page.open()
            user_page.enter_user_page()
            cur_gender = user_page.change_gender()
            new_gender = user_page.change_gender()
            assert cur_gender != new_gender, 'User can not change gender'



        def test_enter_short_password(self, driver):
            user_page = UserFormPage(driver, 'https://shop.by/')
            user_page.open()
            user_page.enter_user_page()
            message = user_page.enter_short_password()
            assert message == 'Не менее 8-ми символов', 'Password must be at least 8 characters'

        def test_change_password(self, driver):
            user_page = UserFormPage(driver, 'https://shop.by/')
            user_page.open()
            user_page.enter_user_page()
            message = user_page.change_password()
            assert message == 'Пароль изменен'
