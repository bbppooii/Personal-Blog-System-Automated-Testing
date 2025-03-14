import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from common.Utils import BlogDriver
from selenium.webdriver.common.by import By

class BlogDetail:
    url = ''
    driver = ''
    def __init__(self):
        """初始化 WebDriver 并打开博客详情页"""
        self.url = 'http://8.137.19.140:9090/blog_detail.html?blogId=24713'
        self.driver = BlogDriver.driver
        self.driver.get(self.url)

    def test_current_user_can_edit(self):
        """测试当前用户是否能编辑博客"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.container > div.right > div > div.operating > button:nth-child(1)')))
        self.driver.find_element(By.CSS_SELECTOR,'body > div.container > div.right > div > div.operating > button:nth-child(1)').click()
        BlogDriver.getScreenShot()
        # 确保页面跳转到博客编辑页
        assert self.driver.title == '博客编辑页', f"编辑页面标题错误：{self.driver.title}"

    def test_current_user_can_delete(self):
        """测试当前用户是否能删除博客"""
        # 等待删除按钮可点击
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.container > div.right > div > div.operating > button:nth-child(2)')))
        self.driver.find_element(By.CSS_SELECTOR,'body > div.container > div.right > div > div.operating > button:nth-child(2)').click()
        # 等待弹出确认框
        alert = WebDriverWait(self.driver,5).until(EC.alert_is_present())
        assert alert.text == '确定删除?', f"弹窗提示不匹配：{alert.text}"
        alert.accept()
        BlogDriver.getScreenShot()
        # 等待页面跳转至博客列表页
        WebDriverWait(self.driver, 10).until(EC.title_is('博客列表页'))
        assert self.driver.title == '博客列表页', f"页面标题错误：{self.driver.title}"

    def test_other_users_cannot_edit_delete(self):
        """测试其他用户无法编辑或删除博客"""
        edit_buttons = self.driver.find_elements(By.CSS_SELECTOR,'body > div.container > div.right > div > div.operating > button:nth-child(1)')
        delete_buttons = self.driver.find_elements(By.CSS_SELECTOR,'body > div.container > div.right > div > div.operating > button:nth-child(2)')
        BlogDriver.getScreenShot()
        # 确保没有编辑和删除按钮
        assert not edit_buttons, "其他用户能看到编辑按钮"
        assert not delete_buttons, "其他用户能看到删除按钮"