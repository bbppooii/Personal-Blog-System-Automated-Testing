from common.Utils import BlogDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BlogEdit:
    url = ''
    driver = ''
    def __init__(self):
        """初始化WebDriver并打开博客编辑页面"""
        self.url = 'http://8.137.19.140:9090/blog_edit.html'
        self.driver = BlogDriver.driver
        self.driver.get(self.url)

    def test_publish_redirect_list(self):
        """测试发布博客后是否跳转到博客列表页"""
        # 输入博客标题
        self.driver.find_element(By.CSS_SELECTOR, '#title').send_keys('789')
        # 提交博客
        self.driver.find_element(By.CSS_SELECTOR, '#submit').click()
        BlogDriver.getScreenShot()
        # 等待页面跳转到博客列表页，并验证跳转是否成功
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is('博客列表页'))
        except:
            pass
        # 确保页面标题为'博客列表页'
        assert self.driver.title == '博客列表页', f"页面标题错误，实际为：{self.driver.title}"
