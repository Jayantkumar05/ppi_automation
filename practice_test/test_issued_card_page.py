# import time
# from Pages.Issued_card_page import Issued_Card_class
# from Pages.Login_Page import LoginPage


# class Test_Issued_Card_():
    
    
#     def test_login_for_issue_page(self,driver):
        
#         login_page = LoginPage(driver)
        
#         login_page.do_login('askjdhf@mailinator.com', 'Test@123')
#         time.sleep(2)
        
#     def test_Issued_Page_form_testing(self,driver):
        
#         orj_issued_card = Issued_Card_class(driver)
        
#         orj_issued_card.Issued_card_to_orj('Name', 'SBI', 9867543666, 'GC card program', 240001127264, 1000, 11092002, 'House Number', 'Area', 'Landmark', 879678, 'City', 'State')
#         time.sleep(2)
        
#         # Check GC insta card creation is progress toast message 
#         Expected_toast_Message = "Card creation is in progress"
#         Current_toast_message = orj_issued_card.Card_Creation_Progress_Toast_Message()
#         print("Print Toast Message: ",Current_toast_message)
#         assert Expected_toast_Message == Current_toast_message, f"Toast message mismatch: expected {Expected_toast_Message}, got {Current_toast_message}"
#         time.sleep(2)
        
        
        