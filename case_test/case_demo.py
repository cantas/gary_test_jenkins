import unittest
from selenium import webdriver
from ddt import ddt,file_data
from time import sleep
@ddt
class Case(unittest.TestCase):

    @file_data('../data/url.yaml')
    def test_01(self, **kwargs):
        option = webdriver.ChromeOptions()
        option.page_load_strategy = 'none'
        driver = webdriver.Chrome(options=option)

        driver.implicitly_wait(5)
        driver.get(kwargs['url'])
        driver.find_element(**kwargs['input']).send_keys(kwargs['text'])
        driver.find_element(**kwargs['button']).click()
        sleep(3)
        driver.quit()

if __name__ == '__main__':
    unittest.main()
