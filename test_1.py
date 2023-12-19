from testpage import OperationsHelper
import logging 
import yaml, time
from BaseApi import ApiHelper

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    assert testpage.get_text_blog() == "Blog"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.click_button_create()
    testpage.enter_title_post("super new title")
    testpage.enter_content_post("text new text")
    testpage.click_post_button()
    time.sleep(3)
    assert testpage.get_post() == "super new title"

def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.click_contact()
    testpage.enter_your_name("Sveta")
    testpage.enter_your_email("sun@mail.com")
    testpage.enter_your_content("hello")
    testpage.click_contact_us_btn()
    time.sleep(3)
    assert testpage.get_alert_text() == "Form successfully submitted"

def test_step5():
    logging.info("test_rest_api Starting")
    user1 = ApiHelper()
    user1.autorization()
    assert 93153 in user1.check_post_id()


