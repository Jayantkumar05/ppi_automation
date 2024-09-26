import time
from Pages.Login_Page import LoginPage
from Pages.Org_Load_Amount import OrgLoadAmount


class Testorgloadmoney:
    
    def test_org_load(self, driver):
        
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(3)
        
        # Create object of Org Load Page
        org_load_page = OrgLoadAmount(driver)
    
        #Performs the primary org realted actions... 
        
        # check before load money in primary org...    
        before_load_amount_primary_org_balanced = org_load_page.get_primary_org_balanced()
        print("Before Primary org amount balanced: ", before_load_amount_primary_org_balanced)
        
        # added a bussiness name, UTR and amount...
        org_load_page.load_money_to_primary_org('utr12342677', 1000) 
        
        # Check the toast mesgae is correct or not..
        expected_toast_message = "Load Money success" 
        current_toast_message = org_load_page.toast_succesfull_message()
        assert expected_toast_message == current_toast_message
        time.sleep(2)        
        
        after_allocation_primary_org_blanced = org_load_page.get_primary_org_balanced()
        before_balance_after_removal_of_symbol_for_primary_org = before_load_amount_primary_org_balanced.replace('₹', '').replace(',', '')
        after_allocation_primary_org_blanced = float(before_balance_after_removal_of_symbol_for_primary_org) + float(1000) 
        print("After Primary org amount balance: ",after_allocation_primary_org_blanced)
        time.sleep(2)

        # =====================================================================================
        
        #  Perform the sub-org 1 related actions...
        
        #check before load money in sub org...
        before_load_amount_sub_org_balanced = org_load_page.get_sub_org_balanced('Jayant Sub Org 1')
        print("Befor Sub org 1 amount balance: ",before_load_amount_sub_org_balanced) 
        
        # added a bussiness bussinessname, UTR and amount... 
        org_load_page.load_money_to_sub_org('Jayant Sub Org 1 - Jayant Sub Org 1', 'utr12342677', 1000)
        
        # Check the toast mesgae is correct or not..
        expected_toast_message = "Load Money success" 
        current_toast_message = org_load_page.toast_succesfull_message()
        assert expected_toast_message == current_toast_message
        time.sleep(2)        
        
        after_allocation_sub_org_blanced  = org_load_page.get_sub_org_balanced('Jayant Sub Org 1')
        before_balance_after_removal_of_symbol_for_sub_org = before_load_amount_sub_org_balanced.replace('₹', '').replace(',', '')
        after_allocation_sub_org_blanced = float(before_balance_after_removal_of_symbol_for_sub_org) + float(1000) 
        print("After sub org 1 amount balance: ",after_allocation_sub_org_blanced)
        time.sleep(2)
        
        
        #  Perform the sub-org 2 related actions...
        
        #check before load money in sub org...
        before_load_amount_sub_org_balanced = org_load_page.get_sub_org_balanced('Jayant Sub Org 2')
        print("Befor Sub org 2 amount balance: ",before_load_amount_sub_org_balanced) 
        
        # added a bussiness bussinessname, UTR and amount... 
        org_load_page.load_money_to_sub_org('Jayant Sub Org 2 - Jayant Sub Org 2', 'utr12342677', 1000)
        
        # Check the toast mesgae is correct or not..
        expected_toast_message = "Load Money success" 
        current_toast_message = org_load_page.toast_succesfull_message()
        assert expected_toast_message == current_toast_message
        time.sleep(2)        
        
        after_allocation_sub_org_blanced  = org_load_page.get_sub_org_balanced('Jayant Sub Org 2')
        before_balance_after_removal_of_symbol_for_sub_org = before_load_amount_sub_org_balanced.replace('₹', '').replace(',', '')
        after_allocation_sub_org_blanced = float(before_balance_after_removal_of_symbol_for_sub_org) + float(1000) 
        print("After sub org 2 amount balance: ",after_allocation_sub_org_blanced)
        time.sleep(2)
        
        #  Perform the sub-org 3 related actions...
        
        #check before load money in sub org...
        before_load_amount_sub_org_balanced = org_load_page.get_sub_org_balanced('Jayant Sub Org3')
        print("Befor Sub org 3 amount balance: ",before_load_amount_sub_org_balanced) 
        
        # added a bussiness bussinessname, UTR and amount... 
        org_load_page.load_money_to_sub_org('Jayant Sub Org3 - Jayant Sub Org 3', 'utr12342677', 1000)
        
        # Check the toast mesgae is correct or not..
        expected_toast_message = "Load Money success" 
        current_toast_message = org_load_page.toast_succesfull_message()
        assert expected_toast_message == current_toast_message
        time.sleep(2)        
        
        after_allocation_sub_org_blanced  = org_load_page.get_sub_org_balanced('Jayant Sub Org3')
        before_balance_after_removal_of_symbol_for_sub_org = before_load_amount_sub_org_balanced.replace('₹', '').replace(',', '')
        after_allocation_sub_org_blanced = float(before_balance_after_removal_of_symbol_for_sub_org) + float(1000) 
        print("After sub org 3 amount balance: ",after_allocation_sub_org_blanced)
        time.sleep(5)

        # Logout the page
        login_page.For_logout_Page()
        print("Logged out successfully.")
        time.sleep(5)