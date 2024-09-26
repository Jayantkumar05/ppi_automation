import logging
import time
from Pages.Login_Page import LoginPage
from Pages.Insta_kit_Inventory import InstakitInventory
from Pages.Issued_Card import Issued_Card_class

class Test_InstaKit_Inventory:

    def test_Insta_kit(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        logging.info("Logged in successfully.")
        time.sleep(2)
        
        # Create object for Insta Kit Page
        insta_kit_obj = InstakitInventory(driver)
        
        # Check Loading the Insta Kit Form Uploaded
        
        insta_kit_obj.Loading_the_instakitform(
            'Jayant primary Org - Jayant primary Org', 
            'asdfasdf', 'Andhra Pradesh', 43
        )
        logging.info("Insta Kit form loaded successfully.")
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Instakit request in progress"
        current_toast_message = insta_kit_obj.After_Submit_toast_message()
        logging.info(f"Toast Message: {current_toast_message}")
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Verifying The Insta Kit Table
        kit_number, kit_status = insta_kit_obj.verify_the_InstaKit_table()
        if not kit_number or not kit_status:
            logging.error("Failed to retrieve kit number or status.")
            assert False, "Kit number or status is None"
        logging.info(f"Retrieved kit number: {kit_number}, kit status: {kit_status}")
        time.sleep(2)
        
         
        # Create Object for Issued Page
        issued_page_obj = Issued_Card_class(driver)
        
        # Click The Card page and then open the issue form button

        issued_page_obj.Issued_Insta_card_to_GC(
            'Name', 'SBI', 'GC card program', kit_number, 1000, 
            11092002, 'House Number', 'Area', 
            'Landmark', 879678, 'City', 'State'
        )
        logging.info("Issued card form submitted successfully.")
        
        # Check Kit Status
        insta_kit_obj.Check_Insta_kit_status(kit_number, kit_status)
        
        # Print ALl Test Casses is Sucessful Pass.
        logging.info("ALL TEST CASES ARE SUCCESSFULLY PASSED")
        
        # Logout the page
        login_page.For_logout_Page()
        logging.info("Logged out successfully.")
        time.sleep(5)
        
        
        