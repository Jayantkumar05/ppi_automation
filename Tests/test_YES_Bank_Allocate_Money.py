import logging
import time
from Pages.Login_Page import LoginPage
from Pages.YES_Bank_Allocate_Money import YesBankAllocateMoney
from Pages.Org_Load_Amount import OrgLoadAmount
from Pages.Issued_Card import Issued_Card_class
from Utility.min_kyc_yes import Yes_Min_KYC 

class TestYesBankAllocateMoney:
    
    def test_YesBankAllocateMoney(self, driver):
        
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('lkjahsdf@mailinator.com', 'Test@123')
        logging.info("Logged in successfully.")
        time.sleep(2) 

        # Create object for Org Load Page
        org_load_page = OrgLoadAmount(driver)

        
        # # check before load money in primary org...    
        # before_load_amount_primary_org_balanced = org_load_page.get_primary_org_balanced()
        # print("Before Primary org amount balanced: ", before_load_amount_primary_org_balanced)
        
        
        # # added a bussiness name, UTR and amount...
        # org_load_page.load_money_to_primary_org('utr12342677', 1000)

        # # Check the toast mesgae is correct or not..
        # # expected_toast_message = "Approval Queue created with the id: 240916074010940ID1APQ4975835" 
        # current_toast_message = org_load_page.toast_succesfull_message()
        # print(f"Toast Message is: {current_toast_message}")
        # # assert expected_toast_message == current_toast_message
        # time.sleep(2)
        
        # after_allocation_primary_org_blanced = org_load_page.get_primary_org_balanced()
        # before_balance_after_removal_of_symbol_for_primary_org = before_load_amount_primary_org_balanced.replace('₹', '').replace(',', '')
        # after_allocation_primary_org_blanced = float(before_balance_after_removal_of_symbol_for_primary_org) + float(1000) 
        # print("After Primary org amount balance: ",after_allocation_primary_org_blanced)
        # time.sleep(2)
        
        # ================================================================================================================================
        
        #  Perform the sub-org 1 related actions...
        
        #check before load money in sub org...
        before_load_amount_sub_org_balanced = org_load_page.get_Yes_Bank_sub_org_balanced('SubOrg1')
        print("Befor Sub org 1 amount balance: ",before_load_amount_sub_org_balanced) 
        
        # Create object for Yes Bank 
        org_yes_bank_allocate_money = YesBankAllocateMoney(driver)
        
        # Add Alocation Money Code here ...
        org_yes_bank_allocate_money.Allocate_Balance_To_Business(1000)
        
        # Check the toast mesgae is correct or not.
        expected_toast_message = "Allocated Successfully" 
        print(f"Expected toast Message: {expected_toast_message} ")
        current_toast_message = org_load_page.toast_succesfull_message()
        print(f"Current Toast Message: {current_toast_message} \nBoth Match")
        assert expected_toast_message == current_toast_message
        time.sleep(2)
        
        # Check The After Alocation Balanced.
        after_allocation_sub_org_blanced  = org_load_page.get_Yes_Bank_sub_org_balanced('SubOrg1')
        before_balance_after_removal_of_symbol_for_sub_org = before_load_amount_sub_org_balanced.replace('₹', '').replace(',', '')
        after_allocation_sub_org_blanced = float(before_balance_after_removal_of_symbol_for_sub_org) + float(1000) 
        print("After sub org 1 amount balance: ",after_allocation_sub_org_blanced)
        time.sleep(2)
        
        #==========================================================================================================================
        
    
        # Create object for Issue Card  
        orj_issued_card = Issued_Card_class(driver)

        # Issue the card and get the random mobile number used
        random_mobile, random_name  = orj_issued_card.Issued_Personalized_card_to_GPR_for_Yes_Bank(
            'Demo Name Card', 'Jayant YES Business - Jayant YES Business','GPR Card Program', 1000, 1000
        ) 
        print(random_name)
        Issue_card_expected_toast_message = "Card creation is in progress"
        print(f"Expected Personalized Card creation toast message: {Issue_card_expected_toast_message}")
        Issue_card_Actual_toast_message = orj_issued_card.Issued_card_toast_message()
        assert Issue_card_expected_toast_message == Issue_card_Actual_toast_message
        print(f"Actual Personalized Card creation toast message: {Issue_card_Actual_toast_message} \nBoth Are Matched")

        time.sleep(3) 

        # str_random_mobile = str(f"91{random_mobile}")
        random_mobile_no ="91"+ random_mobile
        orj_issued_card.Check_Verification_Issued_Personalized_card_to_GPR_for_Yes_Bank(random_mobile_no,random_name)
        
        time.sleep(2)


        # time.sleep(20)
            
            