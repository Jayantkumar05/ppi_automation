import logging
import time
from Pages.Login_Page import LoginPage
from Pages.GPR_Bulk_Uploade import GPR_Bulk_Uploade
import pytest

class Test_GPR_Bulk_Uploade:
    # @pytest.mark.skip
    def test_Successful_Complete_GPR_bulk_uploade(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(2)
        
        # Create object of GPR_Bulk_Uploade Page
        gpr_bulk_uploade = GPR_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 10
        csv_file_path, filename = gpr_bulk_uploade.create_csv_file_for_gpr_bulk_upload(total_card)
        
        # print("fileName: ", filename)
        # print("filePath: ", csv_file_path)
        
        # Load the gpr card using the dynamic CSV file path
        gpr_bulk_uploade.load_gpr_bulk_uploade(csv_file_path)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gpr_bulk_uploade.gpr_toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(2)
        
        # Logout the page
        login_page.For_logout_Page()
        logging.info("Logged out successfully.")
        time.sleep(5)
        
        logging.info("Successful_Complete_GPR_bulk_uploade")
        
    @pytest.mark.skip
    def test_No_records_found_in_the_uploaded_csv_file_GPR_bulk_uploade(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(2)
        
        # Create object of GPR_Bulk_Uploade Page
        gpr_bulk_uploade = GPR_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 0
        csv_file_path, filename = gpr_bulk_uploade.create_csv_file_for_gpr_bulk_upload(total_card)
        
        # print("fileName: ", filename)
        # print("filePath: ", csv_file_path)
        
        # Load the gpr card using the dynamic CSV file path
        gpr_bulk_uploade.load_gpr_bulk_uploade(csv_file_path)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gpr_bulk_uploade.gpr_toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(2)
        
        # Logout the page
        login_page.For_logout_Page()
        logging.info("Logged out successfully.")
        time.sleep(5)
        
        logging.info("No_records_found_in_the_uploaded_csv_file_GPR_bulk_uploade")
        
        
    @pytest.mark.skip
    def test_Only_1000_records_can_be_uploaded_at_a_time_GPR_bulk_uploade(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(2)
        
        # Create object of GPR_Bulk_Uploade Page
        gpr_bulk_uploade = GPR_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 1300
        csv_file_path, filename = gpr_bulk_uploade.create_csv_file_for_gpr_bulk_upload(total_card)
        
        # print("fileName: ", filename)
        # print("filePath: ", csv_file_path)
        
        # Load the gpr card using the dynamic CSV file path
        gpr_bulk_uploade.load_gpr_bulk_uploade(csv_file_path)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gpr_bulk_uploade.gpr_toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(2)
        
        # Logout the page
        login_page.For_logout_Page()
        logging.info("Logged out successfully.")
        time.sleep(5)
        
        logging.info("Only_1000_records_can_be_uploaded_at_a_time_GPR_bulk_uploade")
        
    # @pytest.mark.skip 
    def test_Successfully_Failed_Status_GPR_bulk_uploade(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(2)
        
        # Create object of GPR_Bulk_Uploade Page
        gpr_bulk_uploade = GPR_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 33
        csv_file_path, filename = gpr_bulk_uploade.create_Failed_csv_file_for_gpr_bulk_upload(total_card)
        
        # print("fileName: ", filename)
        # print("filePath: ", csv_file_path)
        
        # Load the gpr card using the dynamic CSV file path
        gpr_bulk_uploade.load_gpr_bulk_uploade(csv_file_path)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gpr_bulk_uploade.gpr_toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(2)
        
        # Logout the page
        login_page.For_logout_Page()
        logging.info("Logged out successfully.")
        time.sleep(5)
        
        logging.info("Successfully_Failed_Status_GPR_bulk_uploade")
        
        
    @pytest.mark.skip
    def test_Invaled_Card_program_GPR_bulk_uploade(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(2)
        
        # Create object of GPR_Bulk_Uploade Page
        gpr_bulk_uploade = GPR_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 33
        csv_file_path, filename = gpr_bulk_uploade.Invaled_Card_program_GPR_bulk_uploade_CSV_Failed_file(total_card)
        
        # print("fileName: ", filename)
        # print("filePath: ", csv_file_path)
        
        # Load the gpr card using the dynamic CSV file path
        gpr_bulk_uploade.load_gpr_bulk_uploade(csv_file_path)
        
        # Check if gift card successfully uploaded or not
        expected_toast_message = "Cards creation in progress"
        current_toast_message = gpr_bulk_uploade.gpr_toast_message()
        assert expected_toast_message == current_toast_message, f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        time.sleep(2)
        
        # Check if the total cards match the expected amount
        gpr_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename) 
        time.sleep(2)
        
        # Logout the page
        login_page.For_logout_Page()
        logging.info("Logged out successfully.")
        time.sleep(5)
        
        logging.info("Invaled_Card_program_GPR_bulk_uploade")
            


    