import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class AdoteNaoCompre_Testes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_01_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-1']/ul/ui/a/span").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("usuario7")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("senha123")
        driver.find_element_by_css_selector("button[name=\"btnLogin\"]").click()

    def test_02_edit_extra_info(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-1']/ul/ui/a/span").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("usuario7")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("senha123")
        driver.find_element_by_css_selector("button[name=\"btnLogin\"]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_link_text("Perfil").click()
        driver.find_element_by_id("link_edit_extra").click()
        driver.find_element_by_id("btn_save").click()

    def test_03_search_dog(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("key").clear()
        driver.find_element_by_name("key").send_keys("En")
        driver.find_element_by_id("btnsearch").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'Informações')])[3]").click()
        driver.find_element_by_link_text(u"Adote, não compre!").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

# Create your tests here.
