from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Utils import BlogDriver

class BlogList:
    """博客列表页测试类"""
    url = ''
    driver = ''
    def __init__(self):
        """初始化 WebDriver 并打开博客列表页"""
        self.url = 'http://8.137.19.140:9090/blog_list.html'  # 博客列表页 URL
        self.driver = BlogDriver.driver  # 获取 WebDriver 实例
        self.driver.get(self.url)  # 打开博客列表页

    def test_account_name_display(self):
        """测试用户名称是否正确显示"""
        BlogDriver.getScreenShot()  # 截图用于调试
        user_name = self.driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.left > div > h3').text
        assert user_name in ['zhangsan', 'lisi'], f"用户名不匹配，当前显示：{user_name}"

    def test_article_count_display(self):
        """测试文章统计信息是否正确显示"""
        BlogDriver.getScreenShot()
        article_text = self.driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.left > div > div:nth-child(4) > span:nth-child(1)').text
        assert article_text == '文章', f"页面上未找到'文章'文本，当前文本：{article_text}"

    def test_category_display(self):
        """测试分类信息是否正确显示"""
        BlogDriver.getScreenShot()
        category_text = self.driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.left > div > div:nth-child(4) > span:nth-child(2)').text
        assert category_text == '分类', f"页面上未找到'分类'文本，当前文本：{category_text}"

    def test_blog_title_exists(self):
        """测试博客标题是否存在"""
        BlogDriver.getScreenShot()
        assert self.is_element_present(By.CSS_SELECTOR, 'body > div.container > div.right > div:nth-child(1) > div.title'), "博客标题未找到"

    def test_blog_date_exists(self):
        """测试博客发布日期是否存在"""
        BlogDriver.getScreenShot()
        assert self.is_element_present(By.CSS_SELECTOR, 'body > div.container > div.right > div:nth-child(1) > div.date'), "博客发布日期未找到"

    def test_blog_content_exists(self):
        """测试博客内容简介是否存在"""
        BlogDriver.getScreenShot()
        assert self.is_element_present(By.CSS_SELECTOR, 'body > div.container > div.right > div:nth-child(1) > div.desc'), "博客内容简介未找到"

    def test_blog_button_exists(self):
        """测试博客详情按钮是否存在"""
        BlogDriver.getScreenShot()
        assert self.is_element_present(By.CSS_SELECTOR, 'body > div.container > div.right > div:nth-child(1) > a'), "博客详情按钮未找到"

    def test_navigation_to_blog_list(self):
        """测试导航栏跳转到博客列表页"""
        self.driver.find_element(By.CSS_SELECTOR, 'body > div.nav > a:nth-child(4)').click()
        WebDriverWait(self.driver, 5).until(EC.title_is('博客列表页'))
        assert self.driver.title == '博客列表页', f"页面跳转失败，当前页面标题：{self.driver.title}"

    def test_navigation_to_blog_editor(self):
        """测试导航栏跳转到博客编辑页"""
        self.driver.find_element(By.CSS_SELECTOR, 'body > div.nav > a:nth-child(5)').click()
        try:
            WebDriverWait(self.driver, 5).until(EC.title_is('博客编辑页'))
        except:
            pass
        assert self.driver.title == '博客编辑页', f"页面跳转失败，当前页面标题：{self.driver.title}"

    def test_logout_redirect_to_login_page(self):
        """测试退出账号是否跳转到登录页"""
        self.driver.find_element(By.CSS_SELECTOR, 'body > div.nav > a:nth-child(6)').click()
        try:
            WebDriverWait(self.driver, 5).until(EC.title_is('博客登录页'))
        except:
            pass
        assert self.driver.title == '博客登陆页', f"退出登录失败，当前页面标题：{self.driver.title}"

    def is_element_present(self, by, selector):
        """检查页面元素是否存在"""
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))
            return True
        except:
            return False

