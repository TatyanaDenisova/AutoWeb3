from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging, requests
import yaml



class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])    



class OperationsHelper(BasePage):

    #ENTER TEXT
    def enter_text_info_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Elemen {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True
    

    def enter_login(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="logging form")

    def enter_pass(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_title_post(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_POST_TITLE"], word, description="title")

    def enter_content_post(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT"], word, description="content")
   
    def enter_your_name(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_NAME"], word, description="contact name")

    def enter_your_email(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_EMAIL"], word, description="contact email")

    def enter_your_content(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT"], word, description="contact content")   
    
    #CLICK BTN
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False 
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True                        
                                      
    def click_contact_us_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="send")

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_button_create(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_CREATE"], description="creat post")

    def click_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_POST_BTN"], description="publicate")

    def click_contact(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT"], description="contact")


    #GET TEXT
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")  
        return text

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error lable")
    
    def get_text_blog(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RESULT_LOGIN"], description="result login")

    def get_post(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST_RESULT"], description="result post")
    
    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text
    