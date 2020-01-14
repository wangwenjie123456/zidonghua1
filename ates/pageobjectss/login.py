from selenium import webdriver
import time
import time
from engine.browser_engine import BrowserEngine

class login_go():
    u'''登录类封装'''
    def __init__(self,driver):
        u'''初始化driver参数'''
        self.driver = driver

    def login(self,username,password):
        u'''输入用户名和密码,点击登录'''
        self.driver.find_element_by_xpath('//*[@id="username"]').clear()
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="spa"]').clear()
        self.driver.find_element_by_xpath('//*[@id="spa"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
