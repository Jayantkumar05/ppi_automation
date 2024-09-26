from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

  
# Login Page Locators

class LoginPage:
    user_email_id = 'userEmail'
    user_password_id = 'passwordBoxForLogin'
    login_button_xpath = "//*[@id='loginBtn']"
    warning_message_xpath_for_email = "//span[@class='error-text-format first-letter-cap visible']"
    popup_message_xpath_for_invalid_email_valid_password = "/html/body/div[2]/div"
    warning_message_class_for_write_new_password = "error-text-format visible"
    admin_button_xpath_for_signout = "//div[@class='logo-contents logo-border']"
    signout_xpath = "(//a[@role='menuitem'])[2]"
    # click_admin_button = "(//button[@aria-haspopup='menu'])[1]"
    Otp_login_Xpath = "(//div[@class='password-otp-wrapper']//div[@class='otpInputWrapper mr-1']//input)"
    
    Otp_Toast_Message_Xpath = "//p[@class='v-toast__text']"  
    
    def __init__(self, driver):
        
        self.driver = driver  
        
    

    def enter_email_ID(self, emailid):
        
        email_element = self.driver.find_element(By.ID, self.user_email_id)
        
        email_element.send_keys(emailid)
    
    def Enter_Mobile_Number(self, mobile):
        
        email_element = self.driver.find_element(By.ID, self.user_email_id)
        
        email_element.send_keys(mobile)
        
    def email_clear_method(self):
        
        email_element = self.driver.find_element(By.ID, self.user_email_id)
        email_element.clear()
        
    
    def enter_password(self, password):
        
        password_element = self.driver.find_element(By.ID, self.user_password_id)
        
        password_element.send_keys(password)
        
    def password_clear_method(self):
        
        password_element = self.driver.find_element(By.ID, self.user_password_id)
        
        password_element.clear()
        
    def enter_otp(self, otp): 
        for i in range(1,7):
            OTP_xpath = f"(//div[@class='password-otp-wrapper']//div[@class='otpInputWrapper mr-1']//input)[{i}]"
            OTP_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, OTP_xpath)))
            OTP_element.send_keys(otp)
        
     

    def otp_toast_message(self):
        
        otp_toast_message_element = self.driver.find_element(By.XPATH, self.Otp_Toast_Message_Xpath)
        
        return otp_toast_message_element.text
    
    def click_login_button(self):
        
        login_button_element = self.driver.find_element(By.XPATH, self.login_button_xpath)
        
        login_button_element.click()
        

    def do_login(self, email, password):
        #enter email id
        self.enter_email_ID(email)
        #enter password
        self.enter_password(password)
        #click login
        self.click_login_button()
    

        
        # pop_up_msg=self.retrieve_popup_message_to_user()
        
        # # print("Toast Msg ",pop_up_msg)
        # return pop_up_msg
        
    def click_admin_page(self):
        
        signout_field = self.driver.find_element(By.XPATH, self.admin_button_xpath_for_signout)
        
        signout_field.click()
    
    def click_signout_button(self):
        
        signout_button_element = self.driver.find_element(By.XPATH, self.signout_xpath)
        
        signout_button_element.click()
        
    def For_logout_Page(self):
        
        self.click_admin_page()
        time.sleep(2)
        self.click_signout_button()
        time.sleep(2)
             
        

    def retrieve_warning_message_for_email(self):
 
        #this is basically used for Waits up to 10 seconds for the warning message element to be visible.
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.warning_message_xpath_for_email)))
        
        warning_message_element_for_email = self.driver.find_element(By.XPATH, self.warning_message_xpath_for_email)
        
        return warning_message_element_for_email.text

    def retrieve_popup_message(self):
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.popup_message_xpath_for_invalid_email_valid_password)))
        
        popup_message_element = self.driver.find_element(By.XPATH, self.popup_message_xpath_for_invalid_email_valid_password)
        
        return popup_message_element.text

    def clear_password_field_and_write_new_password(self):
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.user_password_id)))
        
        password_field = self.driver.find_element(By.ID, self.user_password_id)

        password_field.clear()  
        
        password_field.send_keys("Test@123")  
        
        return self.click_login_button()
    
    
    
    def get_current_page_url(self):
        
        current_page_url=self.driver.current_url
        print("Current URL",current_page_url)
        
        return current_page_url
    
        
        
    
        
    
        




