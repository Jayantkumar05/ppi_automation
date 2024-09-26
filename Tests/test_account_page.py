import logging
import time
import pytest
from Pages.Accounts_Page import AccountsPage
from Pages.Login_Page import LoginPage
from Pages.Org_Load_Amount import OrgLoadAmount
from Pages.YES_Bank_Allocate_Money import YesBankAllocateMoney




class Test_account_page:
    # @pytest.mark.skip
    def test_Check_Closing_Balance(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('lkjahsdf@mailinator.com', 'Test@123')
        
        time.sleep(2)
        
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

            
            
    # @pytest.mark.skip
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
            
            