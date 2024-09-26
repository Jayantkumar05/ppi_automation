import time
from Pages.Issued_Card import Issued_Card_class
from Pages.Login_Page import LoginPage
import pytest

class Test_Issued_Card_():
    
            
    @pytest.mark.skip
    def test_Successfully_Issue_Digital_Card_GC_testing(self,driver):
            
        login_page = LoginPage(driver)
        time.sleep(2)
        
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        time.sleep(3)
        
        orj_issued_card = Issued_Card_class(driver)
        
        orj_issued_card.Issued_Digital_card_to_GC('Name', 'Cardname',6473839589, 
                                            'GC card program', 1000, 
                                            11092002, 'House Number', 
                                            'Area', 'Landmark', 879678, 
                                            'City', 'State')
        time.sleep(2)
        
        login_page.For_logout_Page()
        time.sleep(2)
        
    @pytest.mark.skip
    def test_Successfully_Issue_Personalized_Card_GC_testing(self,driver):
            
        login_page = LoginPage(driver)
        time.sleep(2)
        
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        time.sleep(3)
        
        orj_issued_card = Issued_Card_class(driver)
        
        orj_issued_card.Issued_Personalized_card_to_GC('Name', 'Cardname',6473839589, 
                                            'GC card program', 1000, 
                                            11092002, 'House Number', 
                                            'Area', 'Landmark', 879678, 
                                            'City', 'State')
        time.sleep(2)
        
        login_page.For_logout_Page()
        time.sleep(2)
        
    @pytest.mark.skip
    def test_Successfully_Issue_Insta_Card_GC_testing(self,driver):
        
        login_page = LoginPage(driver)
        time.sleep(2)
        
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        time.sleep(3)
        
        orj_issued_card = Issued_Card_class(driver)
        
        orj_issued_card.Issued_Insta_card_to_GC('Name', 'Cardname', 'GC card program',
                                                 565456435655, 1000, 11092002, 
                                                 'House Number', 'Area', 'Landmark',
                                                 879678, 'City', 'State')
        time.sleep(2)

    
        # orj_issued_card.Form_Close_cross_button()
        # time.sleep(2)
        
        login_page.For_logout_Page()
        time.sleep(2)
            
            
    # ================================For GPR Card======================================================#
            
    # @pytest.mark.skip
    def test_Successfully_Issue_Digital_Card_GPR_testing(self,driver):
            
        login_page = LoginPage(driver)
        time.sleep(2)
        
        login_page.do_login('lkjahsdf@mailinator.com', 'Test@123')
        time.sleep(3)
        
        orj_issued_card = Issued_Card_class(driver)
        
        orj_issued_card.Issued_Digital_card_to_GPR('Name', 'Cardname',6473839589, 
                                            'GPR Card Program', 1000, 'Aadhaar last four digits',
                                            1158, 11092002, 'Male', 'House Number','Area', 'Landmark', 
                                            879678, 'City', 'State')
        time.sleep(2)
        
        orj_issued_card.Form_Close_cross_button()
        time.sleep(2)
    
        login_page.For_logout_Page()
        time.sleep(2)
        
    # @pytest.mark.skip
    def test_Successfully_Issue_Personalized_Card_GPR_testing(self,driver):
            
        login_page = LoginPage(driver)
        time.sleep(2)
        
        login_page.do_login('lkjahsdf@mailinator.com', 'Test@123')
        time.sleep(3)
        
        orj_issued_card = Issued_Card_class(driver)

        orj_issued_card.Issued_Personalized_card_to_GPR('Name', 'Cardname',6473839589, 
                                            'GPR Card Program', 1000, 'Aadhaar last four digits',
                                            1158, 11092002, 'Male', 'House Number','Area', 'Landmark', 
                                            879678, 'City', 'State')        
        
        time.sleep(2) 
        

        # Check GC insta card creation is progress toast message 
        # Expected_toast_Message = "Card creation is in progress"
        # Current_toast_message = orj_issued_card.Card_Creation_Progress_Toast_Message()
        # print("Print Toast Message: ",Current_toast_message)
        # assert Expected_toast_Message == Current_toast_message, f"Toast message mismatch: expected {Expected_toast_Message}, got {Current_toast_message}"
        # time.sleep(2)
    
        orj_issued_card.Form_Close_cross_button()
        time.sleep(2)
        
        login_page.For_logout_Page()
        time.sleep(2)
        
        
    # @pytest.mark.skip
    def test_Successfully_Issue_Insta_Card_GPR_testing(self,driver):
            
        login_page = LoginPage(driver)
        time.sleep(2)
        
        login_page.do_login('lkjahsdf@mailinator.com', 'Test@123')
        time.sleep(3)
        
        orj_issued_card = Issued_Card_class(driver)
        
        
        
        orj_issued_card.Issued_Insta_card_to_GPR('Name', 'Cardname',6473839589, 
                                            'GPR Card Program', 1000, 'Aadhaar last four digits',
                                            1158, 11092002, 'Male', 'House Number','Area', 'Landmark', 
                                            879678, 'City', 'State')
        time.sleep(2) 
    
        orj_issued_card.Form_Close_cross_button()
        time.sleep(2)
        
        login_page.For_logout_Page()
        time.sleep(2)
        


















    # # Load Funds Check 
    # def test_Load_fund_check(self, driver): 
        
    #     login_page = LoginPage(driver)
    #     time.sleep(2)
        
    #     login_page.do_login('lkjahsdf@mailinator.com', 'Test@123')
    #     time.sleep(3)
        
    #     orj_issued_card = Issued_Card_class(driver)
        
        
        
    #     orj_issued_card.Load_Fund_In_Personalized_Issue_Card( 918719559411, 1000 )
    #     time.sleep(2)
        
    #     login_page.For_logout_Page()
    #     time.sleep(2)
