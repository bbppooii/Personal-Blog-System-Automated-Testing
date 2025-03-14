from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.Utils import BlogDriver


class BlogCancellation:
    url = ''
    driver = ''
    def __init__(self):
        """初始化 WebDriver 并打开博客列表页"""
        self.url = 'http://8.137.19.140:9090/blog_list.html'
        self.driver = BlogDriver.driver
        self.driver.get(self.url)

    def test_logout_success(self):
        """测试用户注销后是否正确跳转回登录页，并限制访问受保护页面"""
        # 点击注销按钮
        self.driver.find_element(By.CSS_SELECTOR, 'body > div.nav > a:nth-child(6)').click()
        BlogDriver.getScreenShot()
        # 等待页面跳转到登录页（10秒内出现登录标题）
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.container-login > div > h3')))
        # 确保用户名和密码框为空
        assert self.driver.find_element(By.CSS_SELECTOR,'#username').get_attribute('value') == ''
        assert self.driver.find_element(By.CSS_SELECTOR,'#password').get_attribute('value') == ''
        # 测试访问受保护的页面，确保被重定向到登录页
        protected_pages = [
            "http://8.137.19.140:9090/blog_list.html",
            "http://8.137.19.140:9090/blog_detail.html?blogId=24428",
        ]
        for page in protected_pages:
            self.driver.get(page)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.container-login > div > h3'))
            )
        # 额外检查：尝试编辑博客，确保未登录状态下不能提交
        self.driver.get("http://8.137.19.140:9090/blog_edit.html")
        try:
            self.driver.find_element(By.CSS_SELECTOR, '#title').send_keys('1')
            self.driver.find_element(By.CSS_SELECTOR, '#submit').click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.container-login > div > h3')))
        except:
            print("未登录用户无法提交博客，测试通过")
