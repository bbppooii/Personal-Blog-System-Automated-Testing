import datetime
import os
import sys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service

class Driver:
    driver = None

    def __init__(self):
        """初始化WebDriver并启动浏览器"""
        options = webdriver.EdgeOptions()
        options.page_load_strategy = 'eager'
        # options.add_argument('-headless')  # 启动无界面模式
        edge_driver_path = EdgeChromiumDriverManager().install()
        self.driver = webdriver.Edge(service=Service(edge_driver_path), options=options)

    def getScreenShot(self):
        """保存当前页面的截图到指定目录"""
        dirname = datetime.datetime.now().strftime('%Y-%m-%d')
        screenshot_dir = os.path.join(os.path.dirname(os.getcwd()), 'images', dirname)

        # 如果截图目录不存在，则创建
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # 根据方法名和时间戳生成唯一的文件名
        filename = sys._getframe().f_back.f_code.co_name + "-" + datetime.datetime.now().strftime(
            '%Y-%m-%d-%H%M%S') + ".png"

        # 保存截图
        screenshot_path = os.path.join(screenshot_dir, filename)
        self.driver.save_screenshot(screenshot_path)


# 创建BlogDriver实例
BlogDriver = Driver()

