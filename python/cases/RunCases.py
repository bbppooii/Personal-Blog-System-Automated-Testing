import time
from common.Utils import BlogDriver
from cases import BlogLogin, BlogList, BlogEdit, BlogDetail, BlogCancellation

def run_blog_login_tests():
    """运行登录模块的所有测试"""
    print("Running BlogLogin tests...")
    BlogLogin.BlogLogin().loginSucTest1()  # 测试用户名 zhangsan 的登录
    BlogLogin.BlogLogin().loginSucTest2()  # 测试用户名 lisi 的登录
    BlogLogin.BlogLogin().test_login_empty_username_empty_password()  # 测试用户名和密码都为空
    BlogLogin.BlogLogin().test_login_empty_username_valid_password()  # 测试用户名为空，密码有效
    BlogLogin.BlogLogin().test_login_invalid_username_invalid_password()  # 测试用户名和密码无效

def run_blog_list_tests():
    """运行博客列表页的所有测试"""
    print("Running BlogList tests...")
    BlogList.BlogList().test_account_name_display()  # 测试用户名是否正确显示
    BlogList.BlogList().test_article_count_display()  # 测试文章数是否正确显示
    BlogList.BlogList().test_category_display()  # 测试分类信息是否正确显示
    BlogList.BlogList().test_blog_title_exists()  # 测试博客标题是否存在
    BlogList.BlogList().test_blog_date_exists()  # 测试博客发布日期是否存在
    BlogList.BlogList().test_blog_content_exists()  # 测试博客内容简介是否存在
    BlogList.BlogList().test_blog_button_exists()  # 测试博客详情按钮是否存在
    BlogList.BlogList().test_navigation_to_blog_list()  # 测试博客列表跳转
    BlogList.BlogList().test_navigation_to_blog_editor()  # 测试博客编辑页跳转
    BlogList.BlogList().test_logout_redirect_to_login_page()  # 测试登出后是否跳转到登录页

def run_blog_edit_tests():
    """运行博客编辑页的所有测试"""
    print("Running BlogEdit tests...")
    BlogEdit.BlogEdit().test_publish_redirect_list()  # 测试发布后是否跳转到博客列表页

def run_blog_detail_tests():
    """运行博客详情页的所有测试"""
    print("Running BlogDetail tests...")
    BlogDetail.BlogDetail().test_current_user_can_edit()  # 测试当前用户是否能编辑博客
    BlogDetail.BlogDetail().test_current_user_can_delete()  # 测试当前用户是否能删除博客
    BlogDetail.BlogDetail().test_other_users_cannot_edit_delete()  # 测试其他用户是否能编辑或删除博客

def run_blog_cancellation_tests():
    """运行博客注销的所有测试"""
    print("Running BlogCancellation tests...")
    BlogCancellation.BlogCancellation().test_logout_success()  # 测试注销是否成功并限制访问

def run_all_tests():
    """运行所有测试"""
    run_blog_login_tests()  # 运行登录相关测试
    run_blog_list_tests()   # 运行博客列表相关测试
    BlogLogin.BlogLogin().loginSucTest1()  # 重新登录
    run_blog_edit_tests()  # 运行博客编辑相关测试
    run_blog_detail_tests()  # 运行博客详情页相关测试
    run_blog_cancellation_tests()  # 运行博客注销相关测试
    print("所有测试已成功通过！")

if __name__ == "__main__":
    try:
        run_all_tests()
    except Exception as e:
        print(f"错误发生: {e}")
    finally:
        BlogDriver.driver.quit()  # 结束所有测试后关闭浏览器
