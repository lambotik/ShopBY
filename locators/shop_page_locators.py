from selenium.webdriver.common.by import By


class UserPageLocators:
    # MainPage
    USER_ENTER = (By.XPATH, '//div[@id="Header__Authentication"]')
    USER_ICON = (By.XPATH, '//div[@id="header-photo"]')
    SETTINGS = (By.CSS_SELECTOR, '[href="/management/settings/update/"]')
    EMAIL_TAB = (By.XPATH, '//a[@id="email-tab"]')
    INPUT_EMAIL = (By.XPATH, '//input[@id="LLoginForm_email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="LLoginForm_password"]')
    ENTER_BUTTON = (By.XPATH, '//input[@name="yt2"]')

    # UserPage
    INPUT_NICK_NAME = (By.XPATH, '//input[@id="username"]')
    INPUT_FIRST_NAME = (By.XPATH, '//input[@id="user-name"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@id="sur-name"]')
    USER_GENDER_M = (By.XPATH, '//div[@data-value="M"]')
    USER_GENDER_W = (By.XPATH, '//div[@data-value="W"]')
    SELECTED_USER_GENDER = (By.XPATH, '//div[@class="gender-fake-radio gender selected"]')


