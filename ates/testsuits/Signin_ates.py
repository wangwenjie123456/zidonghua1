import time
import unittest
from engine.browser_engine import BrowserEngine
from pageobjectss.ates_signin import HomePage
from pageobjectss.pagechoose import Choose
from selenium import webdriver

#登录模块
class SigninAtes(unittest.TestCase):
     #加入装饰器，这样只需要打开和关闭一次浏览器，执行所有测试用例
     @classmethod
     def setUpClass(cls):
         browse = BrowserEngine(cls)
         cls.driver = browse.open_browser(cls)

     @classmethod
     def tearDownClass(cls):
         cls.driver.quit()

     def test_signinates_1(self):
         homepage = HomePage(self.driver)
         homepage.type_account('sshdlr')
         homepage.type_password('iss!@#222qwe')
         homepage.send_submit_btn()
         time.sleep(2)
         homepage.get_windows_img()
         time.sleep(2)
         chosehome = Choose(self.driver)
         self.driver.find_element_by_xpath('//*[@id="a1"]/div/ul/div/div[1]/div[1]/a/li').click()
         time.sleep(30)
         try:
             assert '全球金融管理服务平台' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
             print('Test Pass')
         except Exception as e:
             print('Test Fail', format(e))
         time.sleep(3)

if __name__ == '__main__':
    unittest.main()