import logging
import time
from Pages.Login_Page import LoginPage
from Pages.Gc_Bulk_Upload import Gc_Bulk_Uploade
import pytest

class TestGcbulkmoney:
    # @pytest.mark.skip
    def test_Successful_Complete_gc_bulk_uploade(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(2)
        
        # Create object of Gc_Bulk_Uploade Page
        gc_bulk_uploade = Gc_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 10
        csv_file_path, filename = gc_bulk_uploade.create_csv_file_for_gc_upload(total_card)
        
        # print("fileName: ", filename)
        # print("filePath: ", csv_file_path)
        
        # Load the gift card using the dynamic CSV file path
        gc_bulk_uploade.load_gift_card('GC card program', csv_file_path)
        time.sleep(2)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gc_bulk_uploade.toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gc_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename)  # Use filename from CSV creation
        time.sleep(5)
        
        
        # Logout the page
        login_page.For_logout_Page()
        logging.info("Logged out successfully.")
        time.sleep(5)
        
        logging.info("Successfully GC Bulk Uploade")
        
        

    # @pytest.mark.skip        
    def test_No_records_found_in_the_uploaded_csv_file_GC_bulk_uploade_testing(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(2)
        
        # Create object of Gc_Bulk_Uploade Page
        gc_bulk_uploade = Gc_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 0
        csv_file_path, filename = gc_bulk_uploade.create_csv_file_for_gc_upload(total_card)
        
        # print("fileName: ", filename)
        # print("filePath: ", csv_file_path)
        
        # Load the gift card using the dynamic CSV file path
        gc_bulk_uploade.load_gift_card('GC card program', csv_file_path)
        time.sleep(2)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gc_bulk_uploade.toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gc_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename)  # Use filename from CSV creation
        time.sleep(5)
        
        
        # Logout the page
        login_page.For_logout_Page()
        logging.info("Logged out successfully.")
        time.sleep(5)
        
        logging.info("Successfully Check Zero gc bulk uploade testing")
        
    
    # @pytest.mark.skip
    def test_Only_1000_records_can_be_uploaded_at_a_time_GC_bulk_uploade_testing(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(2)
        
        # Create object of Gc_Bulk_Uploade Page
        gc_bulk_uploade = Gc_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 1111
        csv_file_path, filename = gc_bulk_uploade.create_csv_file_for_gc_upload(total_card)
        
        # print("fileName: ", filename)
        # print("filePath: ", csv_file_path)
        
        # Load the gift card using the dynamic CSV file path
        gc_bulk_uploade.load_gift_card('GC card program', csv_file_path)
        time.sleep(2)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gc_bulk_uploade.toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gc_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename)  # Use filename from CSV creation
        time.sleep(5)
        
        
        # Logout the page
        login_page.For_logout_Page()
        print("Logged out successfully.")
        time.sleep(5)
        
        logging.info("Successfully Check Overlimit gc bulk uploade testing")
        
    
    # @pytest.mark.skip
    def test_Failed_Status_GC_Bulk_Uploade(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(2)
        
        # Create object of Gc_Bulk_Uploade Page
        gc_bulk_uploade = Gc_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 20
        csv_file_path, filename = gc_bulk_uploade.CSV_Failed_file(total_card)
        
        # print("fileName: ", filename)
        # print("filePath: ", csv_file_path)
        
        # Load the gift card using the dynamic CSV file path
        gc_bulk_uploade.load_gift_card('GC card program', csv_file_path)
        time.sleep(2)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gc_bulk_uploade.toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gc_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename)  # Use filename from CSV creation
        time.sleep(5)
        
        
        # Logout the page
        login_page.For_logout_Page()
        logging.info("Logged out successfully.")
        time.sleep(5)
        
        logging.info("Successfully Check Failed Status")
        
        