"""
A simple selenium test written in  python
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import sys

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    URL = ""
    #TITLE = "Google"

    

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Open Test Page"""
        try:
            
            self.driver.get(self.URL)
            #assert self.TITLE in self.driver.title
            
            
            
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    


if __name__ == '__main__':

    if len(sys.argv) > 1:
                TestTemplate.URL = sys.argv.pop()
                #TestTemplate.TITLE = sys.argv.pop()
                #TestTemplate.URL = sys.argv[0]

    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=3).run(suite)
