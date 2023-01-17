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
    ALERT_MESSAGE = (By.XPATH, '//div[@class="errorMessage"]')

    # UserPage
    INPUT_NICK_NAME = (By.XPATH, '//input[@id="username"]')
    INPUT_FIRST_NAME = (By.XPATH, '//input[@id="user-name"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@id="sur-name"]')
    USER_GENDER_M = (By.XPATH, '//div[@data-value="M"]')
    USER_GENDER_W = (By.XPATH, '//div[@data-value="W"]')
    SELECTED_USER_GENDER = (By.XPATH, '//div[@class="gender-fake-radio gender selected"]')
    SELECT_USER_DATE = (By.XPATH, '//select[@id="user-date"]')
    SELECT_USER_MONTH = (By.XPATH, '//select[@id="user-month"]')
    SELECT_USER_YEAR = (By.XPATH, '//select[@id="user-year"]')
    LIST_DATE = (By.XPATH, '//*[@id="user-date"]/option')
    LIST_MONTH = (By.XPATH, '//*[@id="user-month"]/option')
    LIST_YEAR = (By.XPATH, '//*[@id="user-year"]/option')
    DATE = (By.XPATH, '//select[@id="user-date"]')
    MONTH = (By.XPATH, '//select[@id="user-month"]')
    YEAR = (By.XPATH, '//select[@id="user-year"]')
    SAVE_BUTTON = (By.XPATH, '//input[@id="set-data"]')
    SAVE_DONE = (By.XPATH, '//*[@id="profile"]/div[12]/div[2]/div')
    PHONE_NUMBER = (By.XPATH, '//input[@id="phone"]')
    MONTH_INDEX = (By.XPATH, '//*[@id="user-month"]/option')
    WRONG_NICK_NAME = (By.XPATH, '//*[@id="profile"]/div[3]/div[2]/span')

    # Change password
    CHANGE_PASSWORD = (By.XPATH, '//span[@class="hidden-xs"]')
    NEW_PASSWORD = (By.XPATH, '//input[@id="user-password"]')
    REPEAT_PASSWORD = (By.XPATH, '//input[@id="user-password-repeat"]')
    BUTTON_SAVE_PASSWORD = (By.XPATH, '//input[@id="save-password"]')
    MESSAGE = (By.XPATH, '//*[@id="password"]/div[4]/div[2]/div')
    CLEAR_BUTTON = (By.XPATH, '//input[@id="clean-passwords"]')
