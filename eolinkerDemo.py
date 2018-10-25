#-*- coding:utf-8 -*-

import unittest
from selenium import webdriver
import time
import datetime

class eolinkerDemo(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        
        #self.driver = webdriver.Chrome(executable_path=chrome_path))

        #self.driver = webdriver.PhantomJS()
        #self.driver = webdriver.PhantomJS(executable_path="./phantomjs"))

        '''
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=option)
        '''

    def elem_loc(self,loc):
        return self.driver.find_element_by_xpath(loc)

    def screenshot(self,testcase_name,result):
        now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        png_path = r"C:\Users\王亚峰\Desktop\eolinkerDemoPng\\"+testcase_name+"_"+result+"_"+now_time+".png"
        self.driver.save_screenshot(png_path)
        print(".........screenshot success.")


    def test_login_eolinker(self):

        testcase_name = "login"
        driver = self.driver
        driver.get('https://www.eolinker.com/#/login')
        driver.implicitly_wait(10)

        username_loc = '/html/body/div[1]/login/div/div/div[2]/article/form/ul/li[1]/input'
        password_loc = '/html/body/div[1]/login/div/div/div[2]/article/form/ul/li[2]/input'
        loginbtn_loc = '/html/body/div[1]/login/div/div/div[2]/article/form/ul/li[3]/button'

        logo_loc = '/html/body/div[1]/home/div/eo-navbar5/div/div/header/ul[1]/li[1]'

        user = 'arthur00@qq.com'
        pswd = '~zaq1234'


        elem_loc = self.elem_loc
        elem1 = elem_loc(username_loc)
        elem2 = elem_loc(password_loc)
        elem3 = elem_loc(loginbtn_loc)

        
        elem1.send_keys(user)
        elem2.send_keys(pswd)
        elem3.click()

        driver.implicitly_wait(10)

        try:
            elem_loc(logo_loc)
            print("[test_login_eolinker] : PASS", end = ' ')
            result = "pass"
            self.screenshot(testcase_name,result)
            
        except Exception as e:
            print("[test_login_eolinker] : FAILED", end = ' ')
            result = "failed"
            self.screenshot(testcase_name,result)

        '''
        js = "alert('This a selenium demo, Thanks for your watch!')"
        driver.execute_script(js)
        time.sleep(10)
        '''

    def tearDown(self):
        self.driver.quit()

        

if __name__ == "__main__":
    unittest.main()

        
