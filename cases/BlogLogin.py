import time
from common.Utils import BlogDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class BlogLogin:
    url = ''
    driver = ''
    def __init__(self):
        """初始化登录页面并打开指定URL"""
        self.url = "http://8.137.19.140:9090/blog_login.html"
        self.driver = BlogDriver.driver
        self.driver.get(self.url)

    def loginSucTest1(self):
        """测试用户 'zhangsan' 的登录成功"""
        self._login('zhangsan', '123456')
        self._verify_login_success()
        self.driver.back()

    def loginSucTest2(self):
        """测试用户 'lisi' 的登录成功"""
        self._login('lisi', '123456')
        self._verify_login_success()
        self.driver.back()

    def _login(self, username, password):
        """封装的登录方法，接收用户名和密码"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
        self.driver.find_element(By.CSS_SELECTOR, '#username').clear()
        self.driver.find_element(By.CSS_SELECTOR, "#password").clear()
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#submit').click()

    def _verify_login_success(self):
        """验证用户是否成功登录"""
        BlogDriver.getScreenShot()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.container > div.left > div > h3')))
        except:
            pass
        assert self.driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.left > div > h3') is not None

    def test_login_empty_username_empty_password(self):
        """测试用户名和密码为空时的登录行为"""
        self._login('', '')
        self._verify_alert('账号或密码不能为空')
        self.driver.back()

    def test_login_empty_username_valid_password(self):
        """测试用户名为空，密码有效时的登录行为"""
        self._login('', '123456')
        self._verify_alert('账号或密码不能为空')
        self.driver.back()

    def test_login_empty_username_invalid_password(self):
        """测试用户名为空，密码无效时的登录行为"""
        self._login('', '123')
        self._verify_alert('账号或密码不能为空')
        self.driver.back()

    def test_login_invalid_username_empty_password(self):
        """测试用户名无效，密码为空时的登录行为"""
        self._login('123', '')
        self._verify_alert('账号或密码不能为空')
        self.driver.back()

    def test_login_valid_username_empty_password(self):
        """测试用户名有效，密码为空时的登录行为"""
        self._login('123', '')
        self._verify_alert('账号或密码不能为空')
        self.driver.back()

    def test_login_valid_username_invalid_password(self):
        """测试用户名有效，密码无效时的登录行为"""
        self._login('lisi', '123')
        self._verify_alert('密码错误')
        self.driver.back()

    def test_login_invalid_username_valid_password(self):
        """测试用户名无效，密码有效时的登录行为"""
        self._login('123', '123456')
        self._verify_alert('用户不存在')
        self.driver.back()

    def test_login_invalid_username_invalid_password(self):
        """测试用户名无效，密码无效时的登录行为"""
        self._login('123', '123')
        self._verify_alert('用户不存在')
        self.driver.back()

    def _verify_alert(self, expected_alert_text):
        """验证弹出警告框的文本内容"""
        BlogDriver.getScreenShot()
        alert = WebDriverWait(self.driver,5).until(EC.alert_is_present())
        assert alert.text == expected_alert_text
        alert.accept()

    def test_logout_via_profile(self):
        """测试通过个人资料页面登出"""
        self._login('zhangsan', '123456')
        self.driver.find_element(By.CSS_SELECTOR, '#submit').click()
        self.driver.get('http://8.137.19.140:9090/blog_list.html')
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.nav > a:nth-child(6)')))
        self.driver.find_element(By.CSS_SELECTOR,'body > div.nav > a:nth-child(6)').click()
        BlogDriver.getScreenShot()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.container-login > div > h3')))
        self.driver.back()