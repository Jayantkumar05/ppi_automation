import time
from selenium.webdriver.common.keys import Keys
from time import gmtime, strftime
# from Integration.Admin_Portal.pages.OrgLoadMoneyPage import OrgLoadMoney
# from Integration.Admin_Portal.pages.CardCreationPage import CardCreation
# from Utilities.randomData import RandomData
# from Utilities import CSVUtils

from Pages.Login_Page import LoginPage
from Pages.CardCreationPage import CardCreation
from Utility import CSVUtils

import pandas as pd



# @pytest.mark.sanity_final
# @pytest.mark.usefixtures("setup", "before_and_after_testcases")
class Test_CardCreation:

    # @pytest.mark.skip
    # @pytest.mark.card_creation_regression
    def test_NsdlIssuer_CardCreation(self,driver):
        # Create object of login class
        login_page = LoginPage(driver)
        
        # Do Login
        login_page.Enter_Mobile_Number(9478226573)
        time.sleep(2)  
        login_page.enter_otp(1)
        time.sleep(3)
        # login_page.do_login('askjdhf@mailinator.com', 'Test@1234')
        
        time.sleep(2)
        
        #Create object for card creation class
        CardCreationPage = CardCreation(driver)
        # initaializing driver

        csv_path = "test_data/Card_Creation_Test_Data.csv"
        
        data_frame=pd.read_csv(csv_path)
        data_frame=data_frame.fillna('')
        
        print("Data Frame",data_frame)
        
        rows = len(data_frame)
        
        print("Total  rows in data frame ", rows)

        # data, rows = CSVUtils.getRowCount(csv_path)
        # # Navigate to CardCreationPage
        # print("Number of Rows:", rows)
        # print("CSV Data:", data)
        # CSVUtils.readData(csv_path, 0, 2)
        business_name = CSVUtils.readData(data_frame, 0, 2)
        print("business name ", business_name)
        # CardCreationPage.navigate_to_Card_Creation_Page(
        #     business_name)
        CardCreationPage.click_Cards_section()
        time.sleep(10)
        for r in range(0, rows):
            try:
                # Click Issue Card Button
                CardCreationPage.click_IssueCardBtn()

                # Enter Full Name
                full_name = CSVUtils.readData(data_frame, r, 3)
                CardCreationPage.enter_FullName(full_name)

                # Enter Name on Card
                name_on_card = CSVUtils.readData(data_frame, r, 4)
                CardCreationPage.enter_NameOnCard(name_on_card)

                # Enter Mobile Number
                mobile_number = CSVUtils.readData(data_frame, r, 5)
                if mobile_number:
                    mobile_number = str(mobile_number).replace('.0', '')
                CardCreationPage.enter_MobileNumber((mobile_number))

                # Enter Email
                email = CSVUtils.readData(data_frame, r, 6)
                CardCreationPage.enter_EmailID(email)

                # Select Card Type
                card_type = CSVUtils.readData(data_frame, r, 7)
                CardCreationPage.select_card_type(card_type)

                # Wallet Starting Balance
                staring_balance = CSVUtils.readData(data_frame, r, 8)
                CardCreationPage.enter_Starting_WalletBalance(
                    str(staring_balance))

                document_type = CSVUtils.readData(data_frame, r, 9)
                document_value = CSVUtils.readData(data_frame, r, 10)

                if document_type == "Pan Number":
                    CardCreationPage.select_DocumentType_And_Provide_DocumentValue(
                        "Pan Number", document_value)
                elif document_type == "Aadhaar Number":
                    CardCreationPage.select_DocumentType_And_Provide_DocumentValue(
                        "Aadhaar Number", document_value)

                # Select DOB
                DOB = CSVUtils.readData(data_frame, r, 11)
                CardCreationPage.enter_DOB_Calender(DOB)

                # Select Gender
                issuer_name = CSVUtils.readData(data_frame, r, 1)
                if issuer_name == "FINO":
                    gender = CSVUtils.readData(data_frame, r, 12)
                    CardCreationPage.SelectGender(gender)
                else:
                    pass

                # Provide Address "Address1"
                address1 = CSVUtils.readData(data_frame, r, 13)
                CardCreationPage.enter_HouseNo(address1)

                # Provide Address "Address2"
                address2 = CSVUtils.readData(data_frame, r, 14)
                CardCreationPage.enter_Area(address2)

                # Provide Address "Landmark"
                landmark = CSVUtils.readData(data_frame, r, 15)
                CardCreationPage.enter_LandMark(landmark)

                # Provide Address "PIN"
                pin_code = CSVUtils.readData(data_frame, r, 16)
                if pin_code:
                    pin_code = str(pin_code).replace('.0', '')
                CardCreationPage.enter_PinCode((pin_code))

                # Provide Address "City"
                city = CSVUtils.readData(data_frame, r, 17)
                CardCreationPage.enter_City(city)

                # Provide Address "State"
                state = CSVUtils.readData(data_frame, r, 18)
                CardCreationPage.enter_State(state)

                validation_type = CSVUtils.readData(data_frame, r, 19)
                print("Check Validation Type", validation_type)

                feature = CSVUtils.readData(data_frame, r, 20)
                print("Check Feature", feature)

                field_name = CSVUtils.readData(data_frame, r, 21)
                print("Check Field Name", field_name)

                expected_result = CSVUtils.readData(data_frame, r, 22)
                print("Check Expected Result Is: ", expected_result)

                # Click Issue Card Button
                CardCreationPage.click_IssueCard_Submit_Btn()
                time.sleep(4)

                if validation_type == "client":
                    all_client_validation_msg = CardCreationPage.get_field_validation_msg_client(field_name)
                    
                    if all_client_validation_msg == expected_result:
                        CSVUtils.writeData(data_frame, r, 23, all_client_validation_msg)
                        print("Check Actual Result Is: ", all_client_validation_msg)
                        CSVUtils.writeData(data_frame, r, 24, "PASS") 
                        print("Check Actual and Expected Result is Match --> [PASS]")
                    else:
                        CSVUtils.writeData(data_frame, r, 23, all_client_validation_msg)
                        print("Check Actual Result Is: ", all_client_validation_msg)
                        CSVUtils.writeData(data_frame, r, 24, "FAIL")
                        print("Check Actual and Expected Result is Not Match --> [FAIL]")
                else:
                    pass

                # Click Close Button
                CardCreationPage.click_close_button()

            except Exception as e:
                data_frame.to_csv(csv_path, index=False)
                print("Error:", e)
                CSVUtils.writeData(data_frame, r, 25, "Something went wrong")
                pass
            
        data_frame.to_csv(csv_path, index=False)    
        