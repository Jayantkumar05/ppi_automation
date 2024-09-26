from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Business:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://ppi-business-portal.sb.card91.in/user/login"
        self.user_phone_num_id = 'userEmail'
        self.successful_otp_login_popup_message_xpath = "//span[contains(@class, 'v-toast__item--success')]"
        self.warning_message_for_wrong_phone_number_xpath = "//span[contains(@class, 'error-text-format')]"
        self.otp_boxes_xpath = '//input[contains(@id, "__BVID__") and contains(@type, "text")]'
        # self.otp_boxes_xpath = [
        #     '//*[@id="__BVID__26"]/div/div/div[1]/div[1]/input',
        #     '//*[@id="__BVID__27"]/div/div/div[1]/div[2]/input',
        #     '//*[@id="__BVID__28"]/div/div/div[1]/div[3]/input',
        #     '//*[@id="__BVID__29"]/div/div/div[1]/div[4]/input',
        #     '//*[@id="__BVID__30"]/div/div/div[1]/div[5]/input',
        #     '//*[@id="__BVID__31"]/div/div/div[1]/div[6]/input'
        # ]

    def check_phone_number(self, userphone):
        phone_element = self.driver.find_element(By.ID, self.user_phone_num_id)
        phone_element.send_keys(userphone)
        
    def otp_input_box(self,otp):
        otp_element = self.driver.find_element(By.XPATH, self.otp_boxes_xpath)
        otp_element.send_keys(otp)
        
    def give_input_for_checking_phone_number(self, userphone):
        self.driver.get(self.url)
        self.check_phone_number(userphone)

    def fill_otp_in_boxes(self,otp):
        self.driver.get(self.url)
        self.otp_input_box(otp)
        

    def retrieve_warning_message_for_phone(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.warning_message_for_wrong_phone_number_xpath)))
        warning_message_element_for_phone = self.driver.find_element(By.XPATH, self.warning_message_for_wrong_phone_number_xpath)
        return warning_message_element_for_phone.text

    def retrieve_success_popup_message_for_user(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.successful_otp_login_popup_message_xpath)))
        successful_login_popup_message_element_for_phone = self.driver.find_element(By.XPATH, self.successful_otp_login_popup_message_xpath)
        return successful_login_popup_message_element_for_phone.text
