from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

class TwitterBot:
    
    def__init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.pygame.sprite.get_bottom_layer()
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send.keys(self.username)
        password.send.keys(self.password)
        password.send.keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'$src=typd')
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scroollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            tweets =bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)

ed = TwitterBot('yourEmail', 'yourPassword')
ed.login()
ed.like_tweet()