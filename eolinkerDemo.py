#-*- coding:utf-8 -*-

import unittest
from selenium import webdriver
import time
import datetime

class eolinkerDemo(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

        #chrmdri_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        #self.driver = webdriver.Chrome(executable_path=chrmdri_path)

        
        #self.driver = webdriver.PhantomJS()


        '''
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=option)
        '''

    def elem_loc(self,loc):
        return self.driver.find_element_by_xpath(loc)

    def screenshot(self,result):
        now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        png_path = r"C:\Users\王亚峰\Desktop\eolinkerDemoPng\login_"+result+"_"+now_time+".png"
        self.driver.save_screenshot(png_path)
        print("screenshot success!")


    def test_login_eolinker(self):
        driver = self.driver
        driver.get('https://www.eolinker.com/#/login')

        username_loc = '/html/body/div[1]/login/div/div/div[2]/article/form/ul/li[1]/input'
        password_loc = '/html/body/div[1]/login/div/div/div[2]/article/form/ul/li[2]/input'
        loginbtn_loc = '/html/body/div[1]/login/div/div/div[2]/article/form/ul/li[3]/button'

        logo_loc = '/html/body/div[1]/home/div/eo-navbar5/div/div/header/ul[1]/li[1]'


        user = 'arthur00@qq.com'
        pswd = '~zaq1234'

        elem1 = driver.find_element_by_xpath(username_loc)
        elem2 = driver.find_element_by_xpath(password_loc)
        elem3 = driver.find_element_by_xpath(loginbtn_loc)

        
        elem1.send_keys(user)
        elem2.send_keys(pswd)
        elem3.click()

        time.sleep(10)

        try:
            self.elem_loc(logo_loc)
            print("[test_login_eolinker] : PASS")
            result = "pass"
            self.screenshot(result)
            
        except Exception as e:
            print("[test_login_eolinker] : FAILED")
            result = "failed"
            self.screenshot(result)



    def tearDown(self):
        self.driver.quit()

        

if __name__ == "__main__":
    unittest.main()
        
