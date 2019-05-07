from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MySelenium:

    def __init__(self, path_driver, wait_time=10):
        self.driver = webdriver.Chrome(path_driver)
        self.wait = WebDriverWait(self.driver, wait_time)

    def visit(self, page):
        try:
            self.driver.get(page)
        except Exception as e:
            print("Exception in visit(", page, "): ", e)

    def input_by_xpath(self, xpath, text, wait_seconds=0.0):
        try:
            elem = self.wait.until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            elem.click()
            elem.clear()
            elem.send_keys(text)
            time.sleep(wait_seconds)
        except Exception as e:
            print("Exception in input_by_xpath(", xpath, "): ", e)

    def input_by_class(self, class_input, text, wait_seconds=0.0):
        try:
            elem = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, class_input)))
            elem.click()
            elem.clear()
            elem.send_keys(text)
            time.sleep(wait_seconds)
        except Exception as e:
            print("Exception in input_by_class(", class_input, "): ", e)

    def input_by_name(self, name_tag, text, wait_seconds=0.0):
        try:
            elem = self.wait.until(
                EC.presence_of_element_located((By.NAME, name_tag)))
            elem.click()
            elem.clear()
            elem.send_keys(text)
            time.sleep(wait_seconds)
        except Exception as e:
            print("Exception in input_by_name(", name_tag, "): ", e)

    def upload_by_name(self, name_tag, text, wait_seconds=0.0):
        try:
            elem = self.wait.until(
                EC.presence_of_element_located((By.NAME, name_tag)))
            elem.send_keys(text)
            time.sleep(wait_seconds)
        except Exception as e:
            print("Exception in input_by_name(", name_tag, "): ", e)

    def input_unknow_xpath(self, xpath, text, wait_seconds=0.0):
        try:
            elem = self.wait.until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            elem.click()
            elem = self.driver.switch_to.active_element
            elem.clear()
            elem.send_keys(text)
            time.sleep(wait_seconds)
        except Exception as e:
            print("Exception in input_unknow_xpath(", xpath, "): ", e)

    def click_all_by_class(self, item_class, wait_seconds=0.0):
        try:
            items_list = self.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, item_class)))
            for item in items_list:
                item.click()
                time.sleep(wait_seconds)
        except Exception as e:
            print("Exception in click_all_by_class(", item_class, "): ", e)

    def click_by_xpath(self, xpath):
        try:
            elem = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, xpath)))
            elem.click()
        except Exception as e:
            print("Exception in click_by_xpath(", xpath, "): ", e)

    def click_by_class(self, class_name):
        try:
            elem = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name)))
            elem.click()
        except Exception as e:
            print("Exception in click_by_class(", class_name, "): ", e)


############################################################################
#
# http://selenium-python.readthedocs.io/index.html
# https://seleniumhq.github.io/selenium/docs/api/py/api.html
#
###########################################################################