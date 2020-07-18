import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlopen

from selenium.webdriver.common.keys import Keys
import time
import os
import argparse


class ChromeOperate():
    def __init__(self, user_agent="", accessURL = "http://www.ua110.com/", headlessFlag = True):
        super().__init__()
        self.startURL = accessURL
        self.headlessFlag = headlessFlag
        self.user_agent = user_agent

    def ChromeOptions(self):
        try:
            ChromeOptions = Options()
            # 设置user-agent。
            print("user-agent='"+self.user_agent + "'")
            # ChromeOptions.add_argument("user-agent='Mozilla/5.0 (Linux; Android 4.0.3; M031 Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'")
            ChromeOptions.add_argument("user-agent='"+self.user_agent + "'")
            # 启用无痕模式。
            ChromeOptions.add_argument('--incognito')
            if self.headlessFlag == True:
                # 设置为无界面模式。
                ChromeOptions.add_argument('--headless')
                # ChromeOptions.add_argument('--disable-gpu')
                browser = webdriver.Chrome(options=ChromeOptions, executable_path="D:\Python37\Scripts\chromedriver.exe")
            else:
                browser = webdriver.Chrome(options=ChromeOptions, executable_path="D:\Python37\Scripts\chromedriver.exe")
            
            browser.get(self.startURL)
            # 休眠10秒。
            time.sleep(5)

            # 清除所有cookie。
            cookies = browser.get_cookies()
            browser.delete_all_cookies()
        finally:
            print("quit")
            browser.quit()


def ChromeAction(StartURL, useragent, headlessFlag):

    # 读取大量数据已经没有问题了，需要的是设置编码格式为ANSI。
    # user_agents_csv = pd.read_csv('lotof_user_agent.csv', encoding='ANSI')
    user_agents_csv = pd.read_csv('ua.csv', header=None, encoding='ANSI',dtype=str)


    # 先随机选择出来一行，类型为dataframe。
    # 然后将dataframe转换为numpyarray类型，也就是通过values转换的。
    # 最后将numpyarray转换为String类型，通过取[0][0]来实现。string作为参数输入。
    single_ua = user_agents_csv.sample(1, replace=True,random_state=None,axis=0).values[0][0]
    co = ChromeOperate(user_agent=single_ua, headlessFlag=headlessFlag)
    co.ChromeOptions()
    print("Complete.")


if __name__ == "__main__":
    ChromeAction('http://ua110.com','',False)
    # try:

    #     parser = argparse.ArgumentParser(description="The parameters of Chrome browser settings.")
    #     parser.add_argument('--StartURL', '-u', help='StartURL 属性，初始访问页面，默认值为http://ua110.com，非必要参数', default='http://ua110.com')
    #     parser.add_argument('--useragent', '-a', help='useragent 属性，设置useragent，有默认值。没有设置的情况下，从文件中随机选择。非必要参数', 
    #         default="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20")
    #     parser.add_argument('--headlessFlag', '-l', help='headlessFlag 属性，设置是否使用隐藏运行模式，非必要参数。默认值为False', required=False)
    #     args = parser.parse_args()

    #     ChromeAction(args.StartURL, args.useragent, args.headlessFlag)
    # except Exception as e:
    #     print(e)

