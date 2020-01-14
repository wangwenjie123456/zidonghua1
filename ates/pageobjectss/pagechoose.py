from engine.basepage import BasePage

class Choose(BasePage):

    # sports_link = "xpath=>//*[@id='channel-all']/div/ul/li[7]/a"

    news_link = "xpath=>//*[@id='a1']/div/ul/div/div[1]/div[1]/a/li"
    def click_news(self):
       self.click(self.news_link)
       self.sleep(2)
