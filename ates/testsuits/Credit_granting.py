import time
import unittest
from engine.browser_engine import BrowserEngine
from testsuits.Signin_ates import SigninAtes
from pageobjectss.login import login_go
from pageobjectss.pagechoose import Choose

class Credit_grant(unittest.TestCase):
    # 加入装饰器，这样只需要打开和关闭一次浏览器，执行所有测试用例
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_credit_grant(self):
        login_go(self.driver).login("sshdlr","iss!@#222qwe")#调用login方法
        chosehome = Choose(self.driver)
        self.driver.find_element_by_xpath('//*[@id="a1"]/div/ul/div/div[1]/div[1]/a/li').click()
        time.sleep(3)