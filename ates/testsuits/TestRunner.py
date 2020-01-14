from tools import HTMLTestRunner
import os
import unittest
import time
from testsuits.Signin_ates import SigninAtes
from testsuits.Credit_granting import Credit_grant

report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")


#suite = unittest.TestLoader().discover("testsuits")
suite = unittest.TestSuite()
suite.addTest(SigninAtes('test_signinates_1'))
suite.addTest(Credit_grant('test_credit_grant'))
if __name__ == '__main__':

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例测试情况")

    runner.run(suite)

