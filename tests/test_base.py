# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import unittest
import sys
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType


class TestBase(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1024x768')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)

        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

        self.driver.maximize_window()
        self.driver.get('https://developers.line.me/en/')

    def tearDown(self):
        if sys.exc_info():
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

        self.driver.quit()