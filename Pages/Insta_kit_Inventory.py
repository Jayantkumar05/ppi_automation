import logging
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstakitInventory:
    # Locators To Locate the web element.
    Insta_kit_ID = "sideLi2"
    Insta_Kit_Inventory_Button_xpath = "//button[@class='btn-add']"
    Select_Business_name_xpath = "//div[@class='multiselect multi-select-wrapper flex-grow-1 w-85 org-type-wrapper']"
    GC_Card_Program_Xpath = '(//*[@id="group-id"]/div/label)[2]'
    GPR_Card_Program_Xpath = '(//*[@id="group-id"]/div/label)[1]'
    Select_User_By_name_or_phone_number_xpath = "//input[@id='user-input']"
    Search_User_xpath = "//span[@class='search-icon']"
    Click_Left_arrow_xpath = "(//button[@aria-label='previous'])[2]"
    Click_Add_New_Address_Xpath = "//li//div[@class='add-address dashedBdr']"
    Input_HouseNo_Building_Or_Flat_No_xpath = "(//input[@class='input-box form-control is-valid'])[1]"
    Input_Area_Colony_Street_Sector_Village_Locality_xpath = "(//input[@class='input-box form-control is-valid'])[2]"
    Input_Landmark_xpath = "//input[@name = 'landmark']"
    Input_Pincode_xpath = "(//input[@class='input-box form-control is-valid'])[3]"
    Input_City_Xpath = "(//input[@class='input-box form-control is-valid'])[4]"
    Search_State_Xpath = "//div[@class='multiselect multi-select-wrapper flex-grow-1 org-type-wrapper']"
    Click_Add_Button_Xpath = "//button[@type='submit']"
    After_Submit_toast_message_xpath = "//p[@class='v-toast__text']"
    Input_Kits_Quantity_Xpath = "//input[@id='kit-input']"
    Insta_kit_Form_Submit_button_xpath = "//div[@class='d-flex justify-content-center w-100 mt-3']//button[@type='button']"
    
    # Table locator
    Table_Row_Xpath = "//tbody[@class='vuetable-body']" 
    Details_Table_Row_Xpath = "//tbody[@class='body-container']//tr"
    
    def __init__(self, driver):
        self.driver = driver    
            
    def Click_InstaKit_Button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.Insta_kit_ID))).click()

    def Insta_Kit_Inventory_Button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Insta_Kit_Inventory_Button_xpath))).click()
        
    def Select_Business_name(self, businessname):
        business_name_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Select_Business_name_xpath)))
        business_name_element.send_keys(businessname)
        
    def GC_Card_Program(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.GC_Card_Program_Xpath))).click()    
    
    def GPR_Card_Program(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.GPR_Card_Program_Xpath))).click()
        
    def Search_User(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Search_User_xpath))).click()
        
    def Select_User(self, username):
        user_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Select_User_By_name_or_phone_number_xpath)))
        user_element.send_keys(username)
    
    def Click_Left_arrow(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Click_Left_arrow_xpath))).click()
    
    def Click_Add_New_Address(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Click_Add_New_Address_Xpath))).click()
    
    def Input_HouseNo_Building_Or_Flat_No(self, housenumber):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Input_HouseNo_Building_Or_Flat_No_xpath))).send_keys(housenumber)
        
    def Input_Area(self, area):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Input_Area_Colony_Street_Sector_Village_Locality_xpath))).send_keys(area)
        
    def Input_Landmark(self, landmark):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Input_Landmark_xpath))).send_keys(landmark)
        
    def Input_Pincode(self, pincode):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Input_Pincode_xpath))).send_keys(pincode)
        
    def Input_City(self, city):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Input_City_Xpath))).send_keys(city)
        
    def Search_State(self, state):
        state_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Search_State_Xpath)))
        state_element.send_keys(state + Keys.ENTER)
    
    def Click_Add_Button(self):
        Click_Add_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Click_Add_Button_Xpath)))
        Click_Add_Button_ele.click()
        
    def Input_Kits_Quantity(self, kitsquantity):
        Input_Kits_Quantity_ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Input_Kits_Quantity_Xpath)))
        Input_Kits_Quantity_ele.send_keys(kitsquantity)
        
    def Insta_kit_Form_Submit_button(self):
        Insta_kit_Form_Submit_button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Insta_kit_Form_Submit_button_xpath)))
        Insta_kit_Form_Submit_button_ele.click()
        
    def After_Submit_toast_message(self):
        After_Submit_toast_message_ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.After_Submit_toast_message_xpath)))
        return After_Submit_toast_message_ele.text
        
    def Table_row(self):
        Table_row_ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Table_Row_Xpath)))
        return Table_row_ele.text
    
    def Details_Table_Row(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.Details_Table_Row_Xpath)))
    
    def scroll_and_click(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()


    def Loading_the_instakitform(self, businessname, username, state, kitsquantity):
        self.Click_InstaKit_Button()
        time.sleep(2)
        self.Insta_Kit_Inventory_Button()
        time.sleep(2)
        self.Select_Business_name(businessname)
        time.sleep(2)
        self.GC_Card_Program()
        time.sleep(2)
        self.Select_User(username)
        time.sleep(2)
        self.Search_User()
        time.sleep(2)
        self.Click_Left_arrow()
        time.sleep(2)
        self.Click_Left_arrow()
        time.sleep(2)
        self.Click_Left_arrow()
        time.sleep(2)
        self.Click_Add_New_Address()
        time.sleep(2)
        self.Input_HouseNo_Building_Or_Flat_No('hosenumber')
        time.sleep(2)
        self.Input_Area('area')
        time.sleep(2)
        self.Input_Landmark('landmark')
        time.sleep(2)
        self.Input_Pincode('875906')
        time.sleep(2)
        self.Input_City('city')
        time.sleep(2)
        self.Search_State(state)
        time.sleep(2)
        self.scroll_and_click(self.Click_Add_Button_Xpath)
        time.sleep(2)
        self.Input_Kits_Quantity(kitsquantity)
        time.sleep(2)
        self.Insta_kit_Form_Submit_button()
        time.sleep(2)
        
    def Insta_Kit_Creation_For_GPR_Card(self, businessname, username, state, kitsquantity):
        
        self.Click_InstaKit_Button()
        time.sleep(2)
        self.Insta_Kit_Inventory_Button()
        time.sleep(2)
        self.Select_Business_name(businessname + Keys.ENTER)
        time.sleep(2)
        self.GPR_Card_Program()
        time.sleep(2)
        self.Select_User(username)
        time.sleep(2)
        self.Search_User()
        time.sleep(2)
        self.Click_Left_arrow()
        time.sleep(2)
        self.Click_Left_arrow()
        time.sleep(2)
        # self.Click_Left_arrow()
        time.sleep(2)
        self.Click_Add_New_Address()
        time.sleep(2)
        self.Input_HouseNo_Building_Or_Flat_No('hosenumber')
        # time.sleep(2)
        self.Input_Area('area')
        # time.sleep(2)
        self.Input_Landmark('landmark')
        # time.sleep(2)
        self.Input_Pincode('875906')
        # time.sleep(2)
        self.Input_City('city')
        # time.sleep(2)
        self.Search_State(state)
        time.sleep(2)
        self.scroll_and_click(self.Click_Add_Button_Xpath)
        time.sleep(2)
        self.Input_Kits_Quantity(kitsquantity)
        time.sleep(2)
        self.Insta_kit_Form_Submit_button()
        time.sleep(2) 
     
    def Check_Insta_kit_GPR_Card_Creation(self):

        total_row_count = 0

        # Process only the first row
        row = 1

        # Count the Total Number Kits Element.
        total_number_of_kits_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[5]").text.strip()
        total_number_of_kits = int(total_number_of_kits_element)

        logging.info(f"Card status in row {row}: {total_number_of_kits}")

        # Click The Show kits Details
        show_kit_details_element = self.driver.find_element(By.XPATH, f"//tbody//tr[{row}]//div[@class='circular-chevron-wrapper rotate-minus-90']")
        show_kit_details_element.click()
        time.sleep(2)

        # Find all rows in the expanded view
        rows = self.Details_Table_Row()
        number_of_rows = len(rows)
        total_row_count += number_of_rows

        logging.info(f'Number of rows found on this page: {number_of_rows}')

        # Retrieve and print the Kit Number from the second column of the first row
        before_kit_number = None
        if number_of_rows > 0:
            kit_number_element = rows[0].find_element(By.XPATH, 'td[2]').text.strip()
            logging.info(f"Kit number in row 1: {kit_number_element}")
            before_kit_number = kit_number_element
            
        # Click Close Button to close the form
        click_close_form_button_element = self.driver.find_element(By.XPATH, "//button[@aria-label='Close']")
        click_close_form_button_element.click()

        # Allow time for the form to close
        time.sleep(2)

        # Retrieve and check the number of successfully loaded kits
        if total_number_of_kits == total_row_count:
            logging.info('Both counts match.')
        else:
            logging.error("Count mismatch: Expected %d, Found %d", total_number_of_kits, total_row_count)

        return before_kit_number
                
        
    def verify_the_InstaKit_table(self):

        total_row_count = 0
        
        # Get the first row only
        table_row = self.Table_row()

        # Process only the first row
        row = 1

        # Count the Total Number Kits Element.
        total_number_of_kits_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[5]").text.strip()
        total_number_of_kits = int(total_number_of_kits_element)

        logging.info(f"Card status in row {row}: {total_number_of_kits}")

        # Click The Show kits Details
        show_kit_details_element = self.driver.find_element(By.XPATH, f"//tbody//tr[{row}]//div[@class='circular-chevron-wrapper rotate-minus-90']")
        show_kit_details_element.click()
        time.sleep(2)

        # Find all rows in the expanded view
        rows = self.Details_Table_Row()
        number_of_rows = len(rows)
        total_row_count += number_of_rows

        logging.info(f'Number of rows found on this page: {number_of_rows}')

        # Retrieve and print the Kit Number from the second column of the first row
        before_kit_number = None
        before_kit_status = None
        if number_of_rows > 0:
            kit_number_element = rows[0].find_element(By.XPATH, 'td[2]').text.strip()
            logging.info(f"Kit number in row 1: {kit_number_element}")
            before_kit_number = kit_number_element
            before_kit_status_element = rows[0].find_element(By.XPATH, 'td[3]').text.strip()
            logging.info(f"Kit status in row 1: {before_kit_status_element}")
            before_kit_status = before_kit_status_element
            
        # Click Close Button to close the form
        click_close_form_button_element = self.driver.find_element(By.XPATH, "//button[@aria-label='Close']")
        click_close_form_button_element.click()

        # Allow time for the form to close
        time.sleep(2)

        # Retrieve and check the number of successfully loaded kits
        if total_number_of_kits == total_row_count:
            logging.info('Both counts match.')
        else:
            logging.error("Count mismatch: Expected %d, Found %d", total_number_of_kits, total_row_count)

        return before_kit_number, before_kit_status
        
    def Check_Insta_kit_status(self, previous_kit_number, before_kit_status):
        
        self.Click_InstaKit_Button()
        logging.info("Click Insta Kit Button ")
        time.sleep(2)
        
        row = 1 
        # Click The Show kits Details
        show_kit_details_element = self.driver.find_element(By.XPATH, f"//tbody//tr[{row}]//div[@class='circular-chevron-wrapper rotate-minus-90']")
        show_kit_details_element.click()
        time.sleep(2)
        
        while True:
            # Get the details table rows
            detail_table = self.Details_Table_Row()
                
            found = False
            
            for row in range(1, len(detail_table) + 1):
                
                # Search Kit Number
                kit_number_element = self.driver.find_element(By.XPATH, f"//tbody[@class='body-container']//tr[{row}]/td[2]")
                current_kit_number = kit_number_element.text.strip()
                
                logging.info(f"Checking row {row} for kit_number: {current_kit_number}")
                
                if current_kit_number == previous_kit_number:
                    logging.info(f"Kit number matched in row {row}: {current_kit_number}")
                    found = True
                    
                    # Retrieve and log the kit status
                   
                    after_kit_status_element = self.driver.find_element(By.XPATH, f"//tbody[@class='body-container']//tr[{row}]/td[3]")
                    after_kit_status = after_kit_status_element.text.strip()
                    
                    logging.info(f"Kit status in row {row}: {after_kit_status}")
                    
                    # Check if the status has changed from CREATED to ISSUED
                    if after_kit_status != before_kit_status:
                        logging.info(f"Status changed from {before_kit_status} to {after_kit_status}.")
                        
                        # Check Status is Issued or not.
                        if after_kit_status == "ISSUED":
                            logging.info("Kit has been successfully issued.")
                            
                            # Click Close Button to close the form
                            click_close_form_button_element = self.driver.find_element(By.XPATH, "//button[@aria-label='Close']")
                            click_close_form_button_element.click()
                            # Allow time for the form to close
                            time.sleep(2)
                            return True
                        
                        else:
                            logging.warning(f"Kit status changed but is not ISSUED. Current status: {after_kit_status}")
                            return False
                    else:
                        logging.warning(f"Kit status has not changed. Current status: {after_kit_status}")
                        return False
                    
            if not found:
                logging.info("Kit number not found in the current detail table. Retrying...")
                time.sleep(5)  





