import time
from Pages.Login_Page import LoginPage
import pytest
    
    
class TestLoginModule: 
    
    # Positive test casses===================================================================
    
    # Test Sucessfull Otp Login 
    #@pytest.mark.skip
    def test_sucess_otp_login(self, driver):
        login_page_obj = LoginPage(driver)
        login_page_obj.Enter_Mobile_Number(9874356759)
        time.sleep(2)
        expected_toast_message = "OTP has been sent to your mobile number"
        actual_toast_message = login_page_obj.otp_toast_message() 
        print(f"Before Toast Message: {expected_toast_message} \nActual toast message {actual_toast_message}")
        assert expected_toast_message==actual_toast_message
        print("Both Are Match ") 
        login_page_obj.enter_otp(1)
        time.sleep(2)
    
    
    # Succesfull Login only
    #@pytest.mark.skip
    def test_success_login(self,driver):    
        login_page_obj = LoginPage(driver)        
        login_page_obj.do_login('askjdhf@mailinator.com', 'Test@1234')
        time.sleep(2)
  
        
    # Test Success login then successfull logout
    #@pytest.mark.skip
    def test_success_login_and_success_logout(self,driver):    
        login_page_obj = LoginPage(driver)        
        login_page_obj.do_login('askjdhf@mailinator.com', 'Test@1234')
        time.sleep(2)  
        login_page_obj.For_logout_Page()
        time.sleep(2)

    # Test login Url 
    #@pytest.mark.skip
    def test_success_login_Url(self,driver):    
        login_page_obj = LoginPage(driver)        
        login_page_obj.do_login('askjdhf@mailinator.com', 'Test@1234')
        time.sleep(2)
        expected_url = "https://ppi-business-portal.qa.card91.in/app/organization/overview"
        current_url=login_page_obj.get_current_page_url()
        print("Current Page URL",current_url)
        assert current_url ==expected_url
        time.sleep(2)
        login_page_obj.For_logout_Page()
        time.sleep(2)
           
    # Negative test casses================================================================


    # Only Invaled Email
    #@pytest.mark.skip     
    def test_Invaled_email_only(self, driver):
        
        login_page_obj = LoginPage(driver)
        
        # Enter email ID
        wrong_email_format= 'jsdnjrgmail.com'
        login_page_obj.enter_email_ID(wrong_email_format)
        time.sleep(2)
        # Get Validation Message
        email_waring_msg=login_page_obj.retrieve_warning_message_for_email()
        # Assert validation message with expected 
        expected_warning_message = "please enter a valid email or 10 digit phone number"
        assert email_waring_msg==expected_warning_message
        time.sleep(2) 
        
    # If the Admin is block Then check
    @pytest.mark.skip     
    def test_admin_block(self,driver):
        
        login_page_obj = LoginPage(driver)
        time.sleep(2) 
        login_page_obj.email_clear_method()  
        time.sleep(2)
        login_page_obj.do_login('askjdhf@mailinator.com', 'fjrn@12rirj3')
        expected_popup_message = "Admin is locked, please do reset password to unlock it"        
        popup_message = login_page_obj.retrieve_popup_message()
        time.sleep(2)
        assert expected_popup_message == popup_message  
        time.sleep(2)
                
    # Valed Email or Invalid Password
    #@pytest.mark.skip
    def test_Valid_email_or_Invalid_password(self,driver):
        
        login_page_obj = LoginPage(driver)
        time.sleep(2) 
        login_page_obj.email_clear_method()  
        time.sleep(2)
        login_page_obj.do_login('askjdhf@mailinator.com', 'fjrn@12rirj3')
        expected_popup_message = "Invalid Email or Password"        
        popup_message = login_page_obj.retrieve_popup_message()
        time.sleep(2)
        assert expected_popup_message == popup_message  
        time.sleep(2)
        
        
           
    # Invaled Email or Valid Password
    #@pytest.mark.skip
    def test_invalid_email_or_valid_password(self,driver):
        
        login_page_obj = LoginPage(driver)
        time.sleep(2)
        login_page_obj.email_clear_method()
        time.sleep(2)
        login_page_obj.do_login('aerjjtr@jok.com', 'Test@1234')
        expected_popup_message = "Invalid Email or Password"        
        popup_message = login_page_obj.retrieve_popup_message()
        time.sleep(2)
        assert expected_popup_message == popup_message  
        time.sleep(2)
        
        

        
    
    
    
    

        
        
        
        
        

        
    

        