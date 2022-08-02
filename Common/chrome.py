# -*- coding: utf-8 -*-

# chrome library
# example
# import chrome
# driver = chrome.Driver().init_driver()


from selenium import webdriver
import chromedriver_autoinstaller
import subprocess

import unittest


class Driver:
    def get_driver(self, options=None):
        try:
            driver = webdriver.Chrome("chromedriver.exe", options=options)
            driver.implicitly_wait(3)
        except Exception as e:
            raise ('Error load ChromeDriver {}'.format(e))
        except:
            raise "Error load ChromeDriver Unhandled Exception"
        else:
            return driver

    def init_driver(self):
        try:
            chromedriver_autoinstaller.install(cwd=True)

            try:
                subprocess.Popen(
                    r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                    r'--user-data-dir="C:\chrometemp"')  # 디버거 크롬 구동
            except FileNotFoundError:
                subprocess.Popen(
                    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                    r'--user-data-dir="C:\chrometemp"')  # 디버거 크롬 구동
            options = webdriver.ChromeOptions()
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
            options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            driver = self.get_driver(options)  # 크롬 드라이버 로드
            driver.implicitly_wait(10)  # seconds

        except Exception as e:
            raise ('Error [%s]' % (str(e)))
        except:
            raise "Unhandled Exception"
        else:
            return driver


class Tests(unittest.TestCase):
    def test_load_driver(self):
        driver = Driver().init_driver()

        if driver is None:
            raise Exception("driver load Failed")
        else:
            print("Driver Load Success")

    def test_control_driver(self):
        driver = Driver().init_driver()

        if driver is None:
            raise Exception("driver load Failed")
        else:
            print("Driver Load Success")

        driver.get("https://www.naver.com/")

        if driver.title != "NAVER":
            raise Exception("Error get page")
        else:
            print("Driver control Success")
