import time
from Pages.Login_Page import LoginPage
from Practice_files.practice_jk import Gc_Bulk_Uploade

class TestGcbulkmoney:
    
    def test_gc_bulk_uploade(self, driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.do_login('askjdhf@mailinator.com', 'Test@123')
        
        time.sleep(2)
        
        # Create object of Gc_Bulk_Uploade Page
        gc_bulk_uploade = Gc_Bulk_Uploade(driver)
        
        # Create CSV file for Gift Card Upload
        total_card = 1001
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
        time.sleep(5)
        
        # Check if the total cards match the expected amount
        gc_bulk_uploade.verify_latest_csv_upload(uploaded_file_name = filename)  # Use filename from CSV creation
        time.sleep(5)
        
        