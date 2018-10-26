#-*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep
import datetime

class eolinkerDemo(unittest.TestCase):

    @classmethod
    def setUpClass(self):

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


        self.driver.get('https://www.eolinker.com/#/login')
        self.driver.implicitly_wait(10)


    def elem_loc(self,loc):
        return self.driver.find_element_by_xpath(loc)

    def screenshot(self,testcase_name,result):
        now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        png_path = r"C:\Users\王亚峰\Desktop\eolinkerDemoPng\\"+testcase_name+"_"+result+"_"+now_time+".png"
        self.driver.save_screenshot(png_path)
        print(".........screenshot success.",end='')


    def test_1_login_eolinker(self):

        driver = self.driver
        elem_loc = self.elem_loc
        
        testcase_name = "login"

        user = 'arthur00@qq.com'
        pswd = '~zaq1234'

        username_loc = '/html/body/div[1]/login/div/div/div[2]/article/form/ul/li[1]/input'
        password_loc = '/html/body/div[1]/login/div/div/div[2]/article/form/ul/li[2]/input'
        loginbtn_loc = '/html/body/div[1]/login/div/div/div[2]/article/form/ul/li[3]/button'
        logo_loc = '/html/body/div[1]/home/div/eo-navbar5/div/div/header/ul[1]/li[1]'

 
        elem_loc(username_loc).send_keys(user)
        elem_loc(password_loc).send_keys(pswd)
        elem_loc(loginbtn_loc).click()

        driver.implicitly_wait(10)

        try:
            elem_loc(logo_loc)
            print("[检查能否成功登陆] : PASS", end = ' ')
            result = "pass"
            self.screenshot(testcase_name,result)
            
        except Exception as e:
            print("[检查能否成功登陆] : FAILED", end = ' ')
            result = "failed"
            self.screenshot(testcase_name,result)

        '''
        js = "alert('This a selenium demo, Thanks for your watch!')"
        driver.execute_script(js)
        sleep(10)
        '''

    def test_2_header_page(self):
        
        driver = self.driver
        elem_loc = self.elem_loc

        switchbtn_loc = '/html/body/div[1]/home/div/eo-navbar5/div/div/header/ul[1]/li[2]/a/div/div'
        switchwin_loc = '/html/body/div[1]/div/div/div[1]/div'
        
        
        # sub-testcase1
        print()
        testcase_name = 'switch_button'
        try:
            elem_loc(switchbtn_loc)
            print("[检查是否存在切换按钮] : PASS", end = ' ')
            result = "pass"
            self.screenshot(testcase_name,result)
            
        except Exception as e:
            print("[检查是否存在切换按钮] : FAILED", end = ' ')
            result = "failed"
            self.screenshot(testcase_name,result)


        # sub-testcase2
        print()
        testcase_name = 'switchSpace_window'

        elem_loc(switchbtn_loc).click()

        try:
            elem_loc(switchwin_loc)
            print("[检查点切换按钮是否弹出切换窗口] : PASS", end = ' ')
            result = "pass"
            self.screenshot(testcase_name,result)
            
        except Exception as e:
            print("[检查点切换按钮是否弹出切换窗口] : FAILED", end = ' ')
            result = "failed"
            self.screenshot(testcase_name,result)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

        

if __name__ == "__main__":
    unittest.main()
    

        
