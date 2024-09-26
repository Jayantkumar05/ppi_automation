import logging
import time
import pytest
from Pages.Accounts_Page import AccountsPage
from Pages.GPR_Bulk_Uploade import GPR_Bulk_Uploade
from Pages.Insta_kit_Inventory import InstakitInventory
from Pages.Login_Page import LoginPage
from Pages.YES_Bank_Allocate_Money import YesBankAllocateMoney
from Pages.Org_Load_Amount import OrgLoadAmount
from Pages.Issued_Card import Issued_Card_class 

class Test_Business_Portal_Sanity_GPR_Personalized_Card:
    
    # ===============================================Login Logout Test Cases..================================================
    # Negative Login test casses==============================================================================================
    @pytest.mark.skip     
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
        logging.info("Sucdessfully Login")
        time.sleep(2) 
    

    @pytest.mark.skip
    def test_invalid_email_or_valid_password(self,driver):
        
        login_page_obj = LoginPage(driver)
        time.sleep(2) 
        login_page_obj.email_clear_method()
        time.sleep(2)
        login_page_obj.do_login('aerjjtr@jok.com', 'Test@123')
        expected_popup_message = "Invalid Email or Password"        
        popup_message = login_page_obj.retrieve_popup_message()
        time.sleep(2)
        assert expected_popup_message == popup_message  
        time.sleep(2)
        
    @pytest.mark.skip
    def test_Valid_email_or_Invalid_password(self,driver):
        
        login_page_obj = LoginPage(driver)
        time.sleep(2) 
        login_page_obj.password_clear_method()
        login_page_obj.email_clear_method()  
        time.sleep(2)
        login_page_obj.do_login('lkjahsdf@mailinator.com', 'fjrn@12rirj3')
        expected_popup_message = "Invalid Email or Password"        
        popup_message = login_page_obj.retrieve_popup_message()
        time.sleep(2)
        assert expected_popup_message == popup_message  
        time.sleep(2)
        
    # Positive Login test casses==============================================================================================
    
    @pytest.mark.skip
    def test_success_login_and_success_logout(self,driver):    
        login_page_obj = LoginPage(driver)
        time.sleep(2) 
        login_page_obj.password_clear_method()
        login_page_obj.email_clear_method()  
        time.sleep(2)       
        login_page_obj.do_login('lkjahsdf@mailinator.com', 'Test@123')
        time.sleep(2)  
        login_page_obj.For_logout_Page()
        time.sleep(2)
        
    @pytest.mark.skip
    def test_sucess_otp_login_With_logout(self, driver):
        
        login_page_obj = LoginPage(driver)
        
        login_page_obj.Enter_Mobile_Number(9874356759)
        time.sleep(2)
        expected_toast_message = "OTP has been sent to your mobile number"
        actual_toast_message = login_page_obj.otp_toast_message() 
        print(f"Before Toast Message: {expected_toast_message} \nActual toast message {actual_toast_message}")
        assert expected_toast_message==actual_toast_message
        print("Both Are Match ") 
        login_page_obj.enter_otp(1)
        time.sleep(3)
        login_page_obj.For_logout_Page()
        time.sleep(2)
      
    
    @pytest.mark.skip
    def test_success_Login_Logout_With_Verify_Url(self,driver):    
        login_page_obj = LoginPage(driver)        
        login_page_obj.do_login('lkjahsdf@mailinator.com', 'Test@123')
        time.sleep(2)
        # expected_url = "https://ppi-business-portal.qual.card91.in/user/login"
        expected_url = "https://ppi-business-portal.qual.card91.in/app/organization/overview"
        current_url=login_page_obj.get_current_page_url()
        print("Current Page URL",current_url)
        assert current_url ==expected_url
        time.sleep(2)
        login_page_obj.For_logout_Page()
        time.sleep(2)
    
      
    # @pytest.mark.skip     
    def test_Success_Login_Only(self, driver):
        
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('lkjahsdf@mailinator.com', 'Test@123')
        logging.info("Logged in successfully.")
        time.sleep(2) 
           
    # ==========================================================================================================================
    # =============================================== Business Page Test Cases..================================================
     
    @pytest.mark.skip 
    def test_Load_Money_to_Primary_org(self, driver):
        
        # Create object for Org Load Page
        org_load_page = OrgLoadAmount(driver)
        
        # check before load money in primary org...    
        before_load_amount_primary_org_balanced = org_load_page.get_primary_org_balanced()
        
        # added a bussiness name, UTR and amount...
        random_utr_number = org_load_page.load_money_to_primary_org_for_Bussiness_portal(1000)
        logging.info(f"Print Random Utr Number: {random_utr_number}")

        # Check the toast mesgae is correct or not..
        # expected_toast_message = "Approval Queue created with the id: 240916074010940ID1APQ4975835" 
        current_toast_message = org_load_page.toast_succesfull_message()
        logging.info(f"Toast Message is: {current_toast_message}")
        # assert expected_toast_message == current_toast_message
        time.sleep(2)
        
        after_allocation_primary_org_blanced = org_load_page.get_primary_org_balanced()
        before_balance_after_removal_of_symbol_for_primary_org = before_load_amount_primary_org_balanced.replace('₹', '').replace(',', '')
        after_allocation_primary_org_blanced = float(before_balance_after_removal_of_symbol_for_primary_org) + float(1000)  
        time.sleep(2)
        
        assert before_load_amount_primary_org_balanced != after_allocation_primary_org_blanced
        
        logging.info(f"Before Primary org amount balanced: {before_load_amount_primary_org_balanced}")
        logging.info(f"Before Primary org amount balanced: {after_allocation_primary_org_blanced}") 
        
            
    @pytest.mark.skip 
    def test_Allocate_Money_To_Sub_Org(self, driver):
        
        # Create object for Yes Bank 
        org_yes_bank_allocate_money = YesBankAllocateMoney(driver) 
        
        #check before load money in sub org...
        before_load_amount_sub_org_balanced = org_yes_bank_allocate_money.get_Yes_Bank_sub_org_balanced('SubOrg1')
        
        # Add Alocation Money Code here ...
        # org_yes_bank_allocate_money.Allocate_Balance_To_Business('SubOrg1 - SubOrg1', 1000) # Use If show bussiness name in allocation button
        org_yes_bank_allocate_money.Allocate_Balance_To_Business(1000)
        
        # Check the toast mesgae is correct or not.
        expected_toast_message = "Allocated Successfully" 
        logging.info(f"Expected toast Message: {expected_toast_message} ")
        current_toast_message = org_yes_bank_allocate_money.toast_succesfull_message()
        logging.info(f"Current Toast Message: {current_toast_message} \nBoth Match")
        assert expected_toast_message == current_toast_message
        time.sleep(2)
        
        # Check The After Alocation Balanced.
        after_allocation_sub_org_blanced  = org_yes_bank_allocate_money.get_Yes_Bank_sub_org_balanced('SubOrg1')
        before_balance_after_removal_of_symbol_for_sub_org = before_load_amount_sub_org_balanced.replace('₹', '').replace(',', '')
        after_allocation_sub_org_blanced = float(before_balance_after_removal_of_symbol_for_sub_org) + float(1000)
        
        assert before_load_amount_sub_org_balanced != after_allocation_sub_org_blanced
        logging.info(f"Befor Sub org 1 amount balance: {before_load_amount_sub_org_balanced}")  
        logging.info(f"After sub org 1 amount balance: {after_allocation_sub_org_blanced}")
        time.sleep(5)
        
    # ==========================================================================================================================
    # =============================================== Card Page Test Cases..====================================================
    
    random_mobile = None   
    random_name = None
    
    @pytest.mark.skip
    def test_Successfully_Issued_Personalized_GPR_Card(self, driver):
        
        global random_mobile_no 
        global random_name
        
        # Create object for Issue Card  
        orj_issued_card = Issued_Card_class(driver)

        # Issue the card and get the random mobile number used
        self.random_mobile, random_name = orj_issued_card.Issued_Personalized_card_to_GPR_for_Yes_Bank(
            'Name On Card', 'Jayant YES Business - Jayant YES Business', 'GPR Card Program', 1000, 1000
        )

        # Check Toast Message After Issued Card 
        Issue_card_expected_toast_message = "Card creation is in progress"
        logging.info(f"Expected Personalized Card creation toast message: {Issue_card_expected_toast_message}")
        Issue_card_Actual_toast_message = orj_issued_card.Issued_card_toast_message()
        assert Issue_card_expected_toast_message == Issue_card_Actual_toast_message
        logging.info(f"Actual Personalized Card creation toast message: {Issue_card_Actual_toast_message} \nBoth Are Matched")

        time.sleep(2)
        random_mobile_no = "91" + self.random_mobile  
    
    @pytest.mark.skip                
    def test_Do_Min_kyc_For_GPR_Card(self, driver):
        
        # Create object for Issue Card  
        orj_issued_card = Issued_Card_class(driver)
        
        orj_issued_card.Check_Verification_Issued_Personalized_card_to_GPR_for_Yes_Bank(random_mobile_no , random_name)
        
        time.sleep(2) 
    
    @pytest.mark.skip
    def test_Issued_Personalized_GPR_Card_Load_Fund_Limit_exceeded_Check(self, driver):
        
        # Create object for Issue Card  
        orj_issued_card = Issued_Card_class(driver)
        
        orj_issued_card.test_Issued_Personalized_GPR_Card_Load_Fund_Check_Toast_Method( random_mobile_no, 10001 )
        time.sleep(2)
        
        Limit_exceeded_Expected_Toast_Message = "Max holding amount exceeded"
        Limit_exceeded_Actual_Toast_Message = orj_issued_card.Issued_card_toast_message()
        assert Limit_exceeded_Expected_Toast_Message == Limit_exceeded_Actual_Toast_Message
        logging.info(f"Limit_exceeded_Toast_Message toast message: {Limit_exceeded_Actual_Toast_Message}")
        
        orj_issued_card.Click_Cross_Buttons()
        time.sleep(2)
        
        
            
    @pytest.mark.skip
    def test_Issued_Personalized_GPR_Card_with_successfully_Load_Fund(self, driver):
  
        # Create object for Issue Card  
        orj_issued_card = Issued_Card_class(driver)
        
        orj_issued_card.Load_Fund_In_Personalized_Issue_Card( random_mobile_no, 1000 )
        time.sleep(2)
        
        
    @pytest.mark.skip
    def test_Issued_Personalized_GPR_Card_Withdraw_Fund_Lower_than_Amt_Check(self, driver):
  
        # Create object for Issue Card  
        orj_issued_card = Issued_Card_class(driver)
        
        orj_issued_card.Issued_Personalized_GPR_Card_Withdraw_Fund_Check_Toast_Method(random_mobile_no, 10001)
        time.sleep(1)
        
        Lower_than_Amt_Expected_Toast_Message = "App Balance is lower than given amount"
        Lower_than_Amt_Actual_Toast_Message = orj_issued_card.Issued_card_toast_message()
        assert Lower_than_Amt_Expected_Toast_Message == Lower_than_Amt_Actual_Toast_Message
        logging.info(f"Check Toast Message: {Lower_than_Amt_Actual_Toast_Message}")
        time.sleep(2) 
        orj_issued_card.Click_Cross_Buttons() 
        time.sleep(2) 
        
        
    @pytest.mark.skip
    def test_Issued_Personalized_GPR_Card_with_successfully_Withdraw_Fund(self, driver):   
        
        # Create object for Issue Card  
        orj_issued_card = Issued_Card_class(driver) 
        
        orj_issued_card.Withdraw_Fund_In_Personalized_Issue_Card_For_GPR(random_mobile_no, 100)
        time.sleep(2)
        
        orj_issued_card.Click_Cross_Buttons() 
        time.sleep(2)
       
        
    @pytest.mark.skip 
    def test_Issued_Personalized_GPR_Card_with_Do_Freeze_Card(self, driver):
 
        # Create object for Issue Card  
        orj_issued_card = Issued_Card_class(driver)     
        
        orj_issued_card.Do_freeze_card_For_GPR_Personalized_Card(random_mobile_no) 

    @pytest.mark.skip 
    def test_Issued_Personalized_GPR_Card_with_Do_UnFreeze_Card(self, driver):
  
        # Create object for Issue Card  
        orj_issued_card = Issued_Card_class(driver) 

        orj_issued_card.Do_Unfreeze_card_For_GPR_Personalized_Card(random_mobile_no)
        time.sleep(2) 
        
    @pytest.mark.skip    
    def test_Issued_Personalized_GPR_Card_Doing_Block_Card(self, driver):
  
        # Create object for Issue Card  
        orj_issued_card = Issued_Card_class(driver) 

        orj_issued_card.Do_Block_Card_For_GPR_Personalized_Card(random_mobile_no)
        time.sleep(2)
        

    # ==========================================================================================================================
    # =============================================== Insta Kit Page Test Cases..====================================================
    
    @pytest.mark.skip
    def test_Insta_kit_Creation(self, driver):
        
        # Create object for Insta Kit Page
        insta_kit_obj = InstakitInventory(driver)
        
        # Check Loading the Insta Kit Form Uploaded
        
        insta_kit_obj.Insta_Kit_Creation_For_GPR_Card(
            'Jayant YES Business - Jayant YES Business', 
             'asdfasdf', 'Andhra Pradesh', 23
        )
        logging.info(f"Insta Kit form loaded successfully.")
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Instakit request in progress"
        current_toast_message = insta_kit_obj.After_Submit_toast_message()
        logging.info(f"Toast Message is Passed: {current_toast_message}")
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Verifying The Insta Kit Table
        kit_number = insta_kit_obj.Check_Insta_kit_GPR_Card_Creation()
        logging.info(f"Kit Number is: {kit_number}")
        time.sleep(2)
    
    # ==========================================================================================================================
    # =============================================== GPR Card Bulk Uploade Test Cases..====================================================

    @pytest.mark.skip
    def test_Invaled_Card_program_GPR_bulk_uploade(self, driver):
        
        # Create object of GPR_Bulk_Uploade Page
        gpr_bulk_uploade = GPR_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 10
        csv_file_path, filename = gpr_bulk_uploade.Invaled_Card_program_GPR_bulk_uploade_CSV_Failed_file(total_card)
        
        # Load the gpr card using the dynamic CSV file path
        gpr_bulk_uploade.load_gpr_bulk_uploade_(csv_file_path)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gpr_bulk_uploade.gpr_toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(2)        
    
    
    @pytest.mark.skip
    def test_Only_1000_records_can_be_uploaded_at_a_time_GPR_bulk_uploade(self, driver):
        
        # Create object of GPR_Bulk_Uploade Page
        gpr_bulk_uploade = GPR_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 1003
        csv_file_path, filename = gpr_bulk_uploade.create_csv_file_for_gpr_bulk_upload(total_card)
        
        # Load the gpr card using the dynamic CSV file path
        gpr_bulk_uploade.load_gpr_bulk_uploade__(csv_file_path)
        
        # Check if gift card successfully uploa
        # ded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gpr_bulk_uploade.gpr_toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(2)
    
            
    @pytest.mark.skip
    def test_No_records_found_in_the_uploaded_csv_file_GPR_bulk_uploade(self, driver):

        # Create object of GPR_Bulk_Uploade Page
        gpr_bulk_uploade = GPR_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 0
        csv_file_path, filename = gpr_bulk_uploade.create_csv_file_for_gpr_bulk_upload(total_card)
    
        
        # Load the gpr card using the dynamic CSV file path
        gpr_bulk_uploade.load_gpr_bulk_uploade__(csv_file_path)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gpr_bulk_uploade.gpr_toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(2)
        
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(2)
        
    
    @pytest.mark.skip 
    def test_Successfully_Failed_Status_GPR_bulk_uploade(self, driver):

        # Create object of GPR_Bulk_Uploade Page
        gpr_bulk_uploade = GPR_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 10
        csv_file_path, filename = gpr_bulk_uploade.create_Failed_csv_file_for_gpr_bulk_upload(total_card)
        
        # Load the gpr card using the dynamic CSV file path
        gpr_bulk_uploade.load_gpr_bulk_uploade_(csv_file_path)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gpr_bulk_uploade.gpr_toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(2)
    
    @pytest.mark.skip
    def test_Successful_Complete_GPR_bulk_uploade(self, driver):
        
        # Create object of GPR_Bulk_Uploade Page
        gpr_bulk_uploade = GPR_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 10
        csv_file_path, filename = gpr_bulk_uploade.create_csv_file_for_gpr_bulk_upload(total_card)
        
        # Load the gpr card using the dynamic CSV file path
        gpr_bulk_uploade.load_gpr_bulk_uploade(csv_file_path)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gpr_bulk_uploade.gpr_toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(3)
        
    # ==========================================================================================================================
    # =============================================== Account Page Test Case..====================================================
  
    @pytest.mark.skip
    def test_Check_Closing_Balance(self, driver): 
        
        # Create onject for AccountPage
        org_account_page = AccountsPage(driver)
        
        # Check Closing Amount Balance
        Before_Closing_Balance_amt_ele = org_account_page.Check_Closing_Amount_Balanced()
        Before_Closing_Balance_amt = Before_Closing_Balance_amt_ele.replace('₹', '').replace(',', '')
        logging.info(f"Clossing Balanced is: {Before_Closing_Balance_amt}")
        
        # Create object for Org Load Page
        org_load_page = OrgLoadAmount(driver)
        
        # check before load money in primary org...   
        before_load_amount_primary_org_balanced = org_load_page.get_primary_org_balanced()
        
        # added a bussiness name, UTR and amount...
        random_utr_number = org_load_page.load_money_to_primary_org_for_Bussiness_portal(1000)
        logging.info(f"Print Random Utr Number: {random_utr_number}")

        # Check After Load Balance
        after_allocation_primary_org_blanced = org_load_page.get_primary_org_balanced()
        before_balance_after_removal_of_symbol_for_primary_org = before_load_amount_primary_org_balanced.replace('₹', '').replace(',', '')
        after_allocation_primary_org_blanced = float(before_balance_after_removal_of_symbol_for_primary_org) + float(1000)  
        time.sleep(2)
        
        assert before_load_amount_primary_org_balanced != after_allocation_primary_org_blanced
        
        logging.info(f"Before Primary org amount balanced: {before_load_amount_primary_org_balanced}")
        logging.info(f"Before Primary org amount balanced: {after_allocation_primary_org_blanced}")
        
        # Match The Closing Balance
        After_Closing_Balance_amt, Money_Inflow_amt, Money_Outflow_amt = org_account_page.Match_The_closing_Amount_Balanced()
        
        # Replacing the Comma And Rupee Symbol
        Money_Inflow_amt_ele = Money_Inflow_amt.replace('₹', '').replace(',', '')
        Money_Outflow_amt_ele = Money_Outflow_amt.replace('₹', '').replace(',', '')
        After_Closing_Balance_amt_ele = After_Closing_Balance_amt.replace('₹', '').replace(',', '')
        After_Closing_Balance_amount = float(After_Closing_Balance_amt_ele)
        
        logging.info(f"After Closing Balance: {After_Closing_Balance_amount}, Money Inflow Amount: {Money_Inflow_amt_ele}, Money Outflow Amount: {Money_Outflow_amt_ele}")
        
        # Check Before Closing Balance After Closing Balanced Are Not Match 
        assert Before_Closing_Balance_amt != After_Closing_Balance_amount
        
        
        Money_Inflow_Outflow_Amount = float(Money_Inflow_amt_ele) - float(Money_Outflow_amt_ele)
        
        if  Money_Inflow_Outflow_Amount == After_Closing_Balance_amount:
            logging.info(f"Money Inflow amount: {Money_Inflow_amt_ele} - Money Outflow Amount: {Money_Inflow_amt_ele}")
            logging.info(f"Closing Amount Balanced Is Match: {After_Closing_Balance_amount}")
        else:
            logging.warning("Closing Amount does not match")

            
            
    @pytest.mark.skip
    def test_Check_Money_OutFlow_Balance(self, driver):
        
        # Create onject for AccountPage
        org_account_page = AccountsPage(driver)
        
        # Check Closing Amount Balance
        Before_Mnoey_OutFlow_amt_ele = org_account_page.Check_Money_Outflow_Balanced()
        Before_Mnoey_OutFlow_amt = Before_Mnoey_OutFlow_amt_ele.replace('₹', '').replace(',', '')
        logging.info(f"Before Mnoey OutFlow amt is: {Before_Mnoey_OutFlow_amt}")
        
        # Create object for Yes Bank 
        org_yes_bank_allocate_money = YesBankAllocateMoney(driver) 
        
        #check before load money in sub org...
        before_load_amount_sub_org_balanced = org_yes_bank_allocate_money.get_Yes_Bank_sub_org_balanced('SubOrg1')
        
        # Add Alocation Money Code here ...
        org_yes_bank_allocate_money.Allocate_Balance_To_Business(1000)
        
        # Check the toast mesgae is correct or not.
        expected_toast_message = "Allocated Successfully" 
        logging.info(f"Expected toast Message: {expected_toast_message} ")
        current_toast_message = org_yes_bank_allocate_money.toast_succesfull_message()
        logging.info(f"Current Toast Message: {current_toast_message} \nBoth Match")
        assert expected_toast_message == current_toast_message
        time.sleep(2)
        
        # Check The After Alocation Balanced.
        after_allocation_sub_org_blanced  = org_yes_bank_allocate_money.get_Yes_Bank_sub_org_balanced('SubOrg1')
        before_balance_after_removal_of_symbol_for_sub_org = before_load_amount_sub_org_balanced.replace('₹', '').replace(',', '')
        after_allocation_sub_org_blanced = float(before_balance_after_removal_of_symbol_for_sub_org) + float(1000)
        
        assert before_load_amount_sub_org_balanced != after_allocation_sub_org_blanced
        logging.info(f"Befor Sub org 1 amount balance: {before_load_amount_sub_org_balanced}")  
        logging.info(f"After sub org 1 amount balance: {after_allocation_sub_org_blanced}")
        time.sleep(5)
        
        # Match The Closing Balance
        After_Closing_Balance_amt, Money_Inflow_amt, Money_Outflow_amt = org_account_page.Match_The_closing_Amount_Balanced()
        
        # Replacing the Comma And Rupee Symbol
        Money_Inflow_amt_ele = Money_Inflow_amt.replace('₹', '').replace(',', '')
        Closing_Balance_ele = After_Closing_Balance_amt.replace('₹', '').replace(',', '')
        After_Mnoey_OutFlow_amt_ele = Money_Outflow_amt.replace('₹', '').replace(',', '')
        After_Mnoey_OutFlow_amount = float(After_Mnoey_OutFlow_amt_ele)
        
        logging.info(f"After Money OutFlow Balance: {After_Mnoey_OutFlow_amount}, Money Inflow Amount: {Money_Inflow_amt_ele}, Closing Amount Balanced: {Closing_Balance_ele}")
        
        
        # Check Before Closing Balance After Closing Balanced Are Not Match 
        assert Before_Mnoey_OutFlow_amt != After_Mnoey_OutFlow_amount
        
        Money_Inflow_Outflow_Amount = float(Money_Inflow_amt_ele) - float(After_Mnoey_OutFlow_amount)
        
        print(Money_Inflow_amt_ele)
        print(After_Mnoey_OutFlow_amount)
        print(f"After Subtraction {Money_Inflow_Outflow_Amount}")

        Closing_Balance_float = float(Closing_Balance_ele)
        
        if  Money_Inflow_Outflow_Amount == Closing_Balance_float:
            logging.info(f"Money Inflow amount: {Money_Inflow_amt_ele} - Money Outflow Amount: {After_Mnoey_OutFlow_amount}")
            logging.info(f"Closing Amount Balanced Is Match: {Closing_Balance_ele}")
        else:
            logging.warning("Closing Amount does not match") 
      
      
    # ==========================================================================================================================
    # =============================================== Logout Method Test Case..====================================================
    
    # @pytest.mark.skip
    def test_Logout_The_Page(self, driver):
       
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Logout the page
        login_page.For_logout_Page()
        logging.info("Logged out successfully.")
        time.sleep(2)
        
