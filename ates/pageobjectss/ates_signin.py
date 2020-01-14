from engine.basepage import BasePage
class HomePage(BasePage):
    input_account = "id=>username"
    input_password = "id=>spa"
    search_submit_btn = "xpath=>//*[@id='btnLogin']"
    new_links = "xpath=>//*[@id='a1']/div/ul/div/div[1]/div[1]/a/li"



    def type_account(self, text):
        self.type(self.input_account, text)

    def type_password(self,text):
        self.type(self.input_password, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_new(self):
        self.click(self.new_links)
        self.sleep(2)
