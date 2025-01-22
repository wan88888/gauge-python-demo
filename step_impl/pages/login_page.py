from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://the-internet.herokuapp.com/login"
        
        # 页面元素定位器
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash_message = (By.ID, "flash")
        
    def navigate_to(self):
        """导航到登录页面"""
        self.driver.get(self.url)
        
    def enter_username(self, username):
        """输入用户名"""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        )
        element.clear()
        element.send_keys(username)
        
    def enter_password(self, password):
        """输入密码"""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_input)
        )
        element.clear()
        element.send_keys(password)
        
    def click_login(self):
        """点击登录按钮"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        element.click()
        
    def get_flash_message(self):
        """获取提示消息"""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.flash_message)
        )
        return element.text
        
    def login(self, username, password):
        """执行完整的登录操作"""
        self.navigate_to()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()