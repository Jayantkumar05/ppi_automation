# test_business_module.py file code 
import time
import pytest
from Practice_files.Bussiness_Page import Business

class TestBussinessLoginModule: 

    # def test_invalid_phone_number_for_login(self):
    #     invaled_phone_number_obj = Business()
    #     invaled_phone_number_obj.give_input_for_checking_phone_number('7780421935765')
    #     expected_warning_message = "please enter a valid email or 10 digit phone number"
    #     warning_message = invaled_phone_number_obj.retrieve_warning_message_for_phone()
    #     assert expected_warning_message in warning_message
    #     time.sleep(10)
        
    def test_valid_phone_number_or_otp(self):
        valid_phone_number_obj = Business()
        valid_phone_number_obj.give_input_for_checking_phone_number('9250384716') 
        time.sleep(6)  
        valid_phone_number_obj.fill_otp_in_boxes('111111')
        time.sleep(5) 

        after_login_expected_popup_message = "OTP has been sent to your mobile number"
        success_popup_message = valid_phone_number_obj.retrieve_success_popup_message_for_user()
        assert after_login_expected_popup_message in success_popup_message
 
        # expected_url = "https://ppi-business-portal.sb.card91.in/app/organization/overview"
        # assert valid_phone_number_obj.driver.current_url == expected_url
        # time.sleep(10)
    
    # def test_valid_phone_number_or_otp(self):
    #     valid_phone_number_obj = Business()
    #     valid_phone_number_obj.give_input_for_checking_phone_number('9250384716')
    #     valid_phone_number_obj.fill_otp_in_boxes()
    #     after_login_expected_popup_message = "OTP has been sent to your mobile number"
    #     success_popup_message = valid_phone_number_obj.retrieve_success_popup_message_for_user()
    #     assert after_login_expected_popup_message in success_popup_message
    #     time.sleep(10)
    
    # def test_valid_phone_number_or_otp(business):
    #     valid_phone_number_obj = Bussiness()
    #     valid_phone_number_obj.give_input_for_checking_phone_number('9250384716')
    
    #     time.sleep(6)   

    #     otp_code = "111111"  # Example OTP code
    #     business.fill_otp_in_boxes(otp_code)   
    #     time.sleep(5)  

    #     # Verify the success popup message
    #     after_login_expected_popup_message = "OTP has been sent to your mobile number"
    #     success_popup_message = business.retrieve_success_popup_message_for_user()
    #     assert after_login_expected_popup_message in success_popup_message

    #     # Optionally, verify the page URL after login
    #     expected_url = "https://ppi-business-portal.sb.card91.in/app/organization/overview"
    #     assert business.driver.current_url == expected_url

