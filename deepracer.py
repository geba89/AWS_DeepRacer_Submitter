from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Aws_DeepRacer_Submitter():
    def __init__(self, path):
        self.driver = webdriver.Chrome(path)

    def open_aws(self):
        self.driver.get("https://aws.amazon.com/console/")

    def go_to_log_in_screen(self):
        search = self.driver.find_element(By.CLASS_NAME, "lb-btn-p-primary")
        search.click()
        time.sleep(5)

    def click_existing_account(self):
        search_list = self.driver.find_elements(By.CLASS_NAME, "StretchButton_stetchButton_1v42P")
        search_list[1].click()

    def aws_log_in_iams(self, iamuser, accountid, password):
        search = self.driver.find_element(By.ID, "iam_user_radio_button")
        search.click()

        search = self.driver.find_element(By.CLASS_NAME, "aws-signin-textfield")
        search.send_keys(iamuser)

        search = self.driver.find_element(By.ID, "next_button")
        search.click()

        search = self.driver.find_element(By.ID, "account")
        search.send_keys(accountid)
        search = self.driver.find_element(By.ID, "username")
        search.send_keys(iamuser)
        search = self.driver.find_element(By.ID, "password")
        search.send_keys(password)
        search = self.driver.find_element(By.ID, "signin_button")
        search.click()  
        time.sleep(3)
    
    def aws_select_root(self, user):
        time.sleep(3)
        search = self.driver.find_element(By.ID, "root_user_radio_button")
        search.click()
        search = self.driver.find_element(By.CLASS_NAME, "aws-signin-textfield")
        search.send_keys(user)
        search = self.driver.find_element(By.ID, "next_button")
        search.click()

    def aws_root_password(self, password):
        time.sleep(1)
        search = self.driver.find_element(By.ID, "password")
        search.send_keys(password)
        search = self.driver.find_element(By.ID, "signin_button")
        search.click()

    
    def close_reward(self):
        time.sleep(5)      
        if len(self.driver.find_elements(By.XPATH, "//*[contains(@class, 'awsui_dismiss-control')]")) > 1:
            search = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'awsui_dismiss-control')]")[1]
            search.click()     

    def select_and_submit_model(self, model_id, button_id):
        time.sleep(1)      
        search = self.driver.find_elements(By.XPATH, "//*[contains(@id,'formField')]")[2]
        search.click()
        search = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'awsui_label-content')]")[model_id]
        search.click()
        search = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'awsui_button')]")[button_id]
        search.click()

    def check_if_can_submit(self):
        search = self.driver.find_element(By.ID, 'PLCHLDR_latest_model_time')
        print(search.text)   

    def open_page(self, page):
        self.driver.get(page) 
