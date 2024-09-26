from faker import Faker
import csv
import datetime
import os
import logging
import random
import string
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GPR_Bulk_Uploade:
    
    # Locators
    card_button_id = "sideLi1"
    click_GPR_bulk_uploade_xpath = "//li[@class='nav-item mr-4 text-center font-weight-bold fs-14']//a[contains(text(),'GPR Bulk Upload')]"
    upload_csv_file_xpath = "//input[@id='uploadCards']"
    gpr_toast_message_xapth = "//p[@class='v-toast__text']"

   # ===============================================================================================
    
    # table locators
    total_row_xpath = "//tbody[@class='vuetable-body'][1]//tr" 
         
    # ============================================================================================
     
    # Contructor, Taking web driver. 
    def __init__(self,driver):
        
        self.driver = driver
        
    # Open Card section
    def card_button(self):
        card_button_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.card_button_id)))
        time.sleep(2)
        card_button_element.click()
        
    def click_gpr_bulk_uploade(self):
        click_gpr_bulk_uploade_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.click_GPR_bulk_uploade_xpath)))
        time.sleep(10) 
        click_gpr_bulk_uploade_element.click()
        
    # def click_gpr_bulk_uploade_GPR(self):
    #     click_gpr_bulk_uploade_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.click_GPR_bulk_uploade_xpath)))
    #     time.sleep(3) # === If you test another bussines then you change the time according to the business
    #     click_gpr_bulk_uploade_element.click()
        
    def upload_csv_file(self, file_path):
        upload_csv_element = self.driver.find_element(By.XPATH,self.upload_csv_file_xpath)
        logging.info("upload_csv_element")
        upload_csv_element.send_keys(file_path)

    def gpr_toast_message(self):
        gpr_toast_message_element = self.driver.find_element(By.XPATH, self.gpr_toast_message_xapth)
        return gpr_toast_message_element.text

    def Total_row(self):
        Table_Row_element = self.driver.find_element(By.XPATH, self.total_row_xpath)
        return Table_Row_element.text
  
    def load_gpr_bulk_uploade(self, file_path):
        # Click card button
        self.card_button()
        logging.info("click the card button")
        time.sleep(2)
        # Click the gift card load mapping link
        self.click_gpr_bulk_uploade()
        logging.info("click gift card link")
        time.sleep(2)
        # Upload Csv file 
        self.upload_csv_file(file_path)
        logging.info("Uploading the csv file")
        logging.info("file Path Uploaded")        
        time.sleep(2)
          
    def load_gpr_bulk_uploade_(self, file_path):
        # Click card button
        self.card_button()
        logging.info("click the card button")
        time.sleep(2)
        # Click the gift card load mapping link
        self.click_gpr_bulk_uploade()
        logging.info("click gift card link")
        time.sleep(2)
        # Upload Csv file 
        self.upload_csv_file(file_path)
        logging.info("Uploading the csv file")
        logging.info("file Path Uploaded")        
        time.sleep(2)
        
    def load_gpr_bulk_uploade__(self, file_path):
        # Click card button
        # self.card_button()
        # logging.info("click the card button")
        # time.sleep(2)
        # Click the gift card load mapping link
        # self.click_gpr_bulk_uploade()
        # logging.info("click gift card link")
        time.sleep(2)
        # Upload Csv file 
        self.upload_csv_file(file_path)
        logging.info("Uploading the csv file")
        logging.info("file Path Uploaded")        
        time.sleep(2)
        
        
#=====================================================================
    
    # functions for making random csv table    

    # Generating random data
    def generate_random_name(self):
        length = random.randint(2, 25)
        name = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        return name.capitalize()

    # Generatiing a random mobile numbers...
    def generate_random_mobile(self):
        return f"{random.randint(6000000000, 9999999999)}"

    # Generating the random date of birth...
    def generate_random_dob(self):
        faker = Faker()
        return faker.date_of_birth(minimum_age=19, maximum_age=60).strftime('%Y-%m-%d')   
    
    # Generating the random email...
    def generate_random_email(self):
        return f"{self.generate_random_name().lower()}@example.com"

    # Downloading the csv file in the test_data folder    
    def create_csv_file_for_gpr_bulk_upload(self, number_of_rows):
        
        # Using Time Stamp for New name in every run time...
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # Create CSV file using timestamp...
        file_path = f'test_data/GPR_bulk_uploade_{timestamp}.csv'
        
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['FULL_NAME', 'NAME_ON_CARD',  'MOBILE','EMAIL', 'DOB', 
                          'GENDER', 'DELIVERY_ADDRESS_1', 'DELIVERY_ADDRESS_2', 
                          'DELIVERY_ADDRESS_LANDMARK', 'DELIVERY_ADDRESS_CITY', 
                          'DELIVERY_ADDRESS_PINCODE', 'DELIVERY_ADDRESS_STATE', 
                          'DELIVERY_ADDRESS_COUNTRY', 'ORG_ID', 'CARD_PROGRAM_ID', 
                          'WALLET_ID_1', 'WALLET_1_LIMIT', 'WALLET_ID_2', 
                          'WALLET_2_LIMIT', 'NARRATION', 'CARD_MODE', 
                          'SEND_PERSONALISED_CARD_WITHOUT_KYC','KYC_DOC_TYPE', 
                          'KYC_DOC_VALUE', 'KYC_DOC_DOB', 'KYC_DOC_GENDER', 
                          'KIT_NUMBER', 'EMBOSS_LINE_4', 'PIN_MAILER']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for _ in range(number_of_rows):
                writer.writerow({
                    'FULL_NAME': self.generate_random_name(),
                    'NAME_ON_CARD' : self.generate_random_name(),
                    'MOBILE': self.generate_random_mobile(),
                    'EMAIL': self.generate_random_email(),
                    'DOB': self.generate_random_dob(),
                    'GENDER': 'M',
                    'DELIVERY_ADDRESS_1' : self.generate_random_name(),
                    'DELIVERY_ADDRESS_2' : self.generate_random_name(),
                    'DELIVERY_ADDRESS_LANDMARK' : self.generate_random_name(),
                    'DELIVERY_ADDRESS_CITY': 'Bangalore',
                    'DELIVERY_ADDRESS_PINCODE' : 560102,
                    'DELIVERY_ADDRESS_STATE' : 'Karnataka',
                    'DELIVERY_ADDRESS_COUNTRY' : 'India',
                    'ORG_ID' : '240916061218011ID1OID5593315', # ==== changed for test_ppi_business_portal_file
                    'CARD_PROGRAM_ID' : '240916062029869ID1CP3501224',  # ==== changed for test_ppi_business_portal_file
                    'WALLET_ID_1' : '83d2a45c-113a-4709-ba15-af4cd5fd13a9', # ==== changed for test_ppi_business_portal_file
                    'WALLET_1_LIMIT' : 1000,
                    'WALLET_ID_2' : '',
                    'WALLET_2_LIMIT' : '',
                    'NARRATION' : '', 
                    'CARD_MODE' : 'DIGITAL_ONLY_CARD', 
                    'SEND_PERSONALISED_CARD_WITHOUT_KYC' : '',
                    'KYC_DOC_TYPE' : '', 
                    'KYC_DOC_VALUE' : '', 
                    'KYC_DOC_DOB' : '',
                    'KYC_DOC_GENDER' : '', 
                    'KIT_NUMBER' : '',
                    'EMBOSS_LINE_4' : '',
                    'PIN_MAILER' : 'False',
                })
                
                
            return  os.path.abspath(file_path), f"GPR_bulk_uploade_{timestamp}.csv"

    # Downloading the Failed csv file in the test_data folder    
    def create_Failed_csv_file_for_gpr_bulk_upload(self, number_of_rows):
        
        # Using Time Stamp for New name in every run time...
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # Create CSV file using timestamp...
        file_path = f'test_data/GPR_bulk_uploade_{timestamp}.csv'
        
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['FULL_NAME', 'NAME_ON_CARD',  'MOBILE','EMAIL', 'DOB', 
                          'GENDER', 'DELIVERY_ADDRESS_1', 'DELIVERY_ADDRESS_2', 
                          'DELIVERY_ADDRESS_LANDMARK', 'DELIVERY_ADDRESS_CITY', 
                          'DELIVERY_ADDRESS_PINCODE', 'DELIVERY_ADDRESS_STATE', 
                          'DELIVERY_ADDRESS_COUNTRY', 'ORG_ID', 'CARD_PROGRAM_ID', 
                          'WALLET_ID_1', 'WALLET_1_LIMIT', 'WALLET_ID_2', 
                          'WALLET_2_LIMIT', 'NARRATION', 'CARD_MODE', 
                          'SEND_PERSONALISED_CARD_WITHOUT_KYC','KYC_DOC_TYPE', 
                          'KYC_DOC_VALUE', 'KYC_DOC_DOB', 'KYC_DOC_GENDER', 
                          'KIT_NUMBER', 'EMBOSS_LINE_4', 'PIN_MAILER']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for _ in range(number_of_rows):
                writer.writerow({
                    'FULL_NAME': self.generate_random_name(),
                    'NAME_ON_CARD' : self.generate_random_name(),
                    # 'MOBILE': self.generate_random_mobile(),
                    'EMAIL': self.generate_random_email(),
                    'DOB': self.generate_random_dob(),
                    'GENDER': 'M',
                    'DELIVERY_ADDRESS_1' : self.generate_random_name(),
                    'DELIVERY_ADDRESS_2' : self.generate_random_name(),
                    'DELIVERY_ADDRESS_LANDMARK' : self.generate_random_name(),
                    'DELIVERY_ADDRESS_CITY': 'Bangalore',
                    'DELIVERY_ADDRESS_PINCODE' : 560102,
                    'DELIVERY_ADDRESS_STATE' : 'Karnataka',
                    'DELIVERY_ADDRESS_COUNTRY' : 'India',
                    'ORG_ID' : '240916061218011ID1OID5593315', # ========================= changed in every new business
                    'CARD_PROGRAM_ID' : '240916062029869ID1CP3501224', # ========================= changed in every new business
                    'WALLET_ID_1' : '83d2a45c-113a-4709-ba15-af4cd5fd13a9', # ========================= changed in every new business
                    'WALLET_1_LIMIT' : 1000,
                    'WALLET_ID_2' : '',
                    'WALLET_2_LIMIT' : '',
                    'NARRATION' : '', 
                    'CARD_MODE' : 'DIGITAL_ONLY_CARD', 
                    'SEND_PERSONALISED_CARD_WITHOUT_KYC' : '',
                    'KYC_DOC_TYPE' : '', 
                    'KYC_DOC_VALUE' : '', 
                    'KYC_DOC_DOB' : '',
                    'KYC_DOC_GENDER' : '', 
                    'KIT_NUMBER' : '',
                    'EMBOSS_LINE_4' : '',
                    'PIN_MAILER' : 'False',
                })
                
                
            return  os.path.abspath(file_path), f"GPR_bulk_uploade_{timestamp}.csv"
     
    
    # Downloading the csv Invaled card progrm Failed file in the test_data folder    
    def Invaled_Card_program_GPR_bulk_uploade_CSV_Failed_file(self, number_of_rows):
        
        # Using Time Stamp for New name in every run time...
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # Create CSV file using timestamp...
        file_path = f'test_data/GC_bulk_uploade_{timestamp}.csv'
        
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['LOAD_AMOUNT', 'FULL_NAME', 'MOBILE', 'DOB', 'NAME_ON_CARD', 'EMAIL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for _ in range(number_of_rows):
                writer.writerow({
                    'LOAD_AMOUNT': '1000',
                    'FULL_NAME': self.generate_random_name(),
                    # 'MOBILE': self.generate_random_mobile(),
                    'DOB': self.generate_random_dob(),
                    # 'NAME_ON_CARD': self.generate_random_bank_name(),
                    'EMAIL': self.generate_random_email(),
                })
                
                
            return  os.path.abspath(file_path), f"GC_bulk_uploade_{timestamp}.csv"
            
            
#===================================================================================================
  
    def verify_latest_csv_upload(self, uploaded_file_name):
        
        while True:
            
            table_row = self.Total_row()
            
            for row in range(1, len(table_row) + 1):
                # Get the CSV file name from the 4th column of this row
                csv_file_name_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[4]")
                csv_file_name_text = csv_file_name_element.text.strip() 
                
                logging.info(f"Checking row {row} for CSV file: {csv_file_name_text}")
                
                if csv_file_name_text.lower() == uploaded_file_name.lower():
                        logging.info(f"File name matched in row {row}: {csv_file_name_text}")
                        # file_found = True

                        # Check the card status in the 10th column of the same row
                        # card_status_complete_element = self.driver.find_element(By.XPATH, f"//tbody//tr[{row}]//td[10]//span[@class='first-letter-cap active-status']")
                        # card_status_complete = card_status_complete_element.text.strip()
                        
                        # card_status_processing_element = self.driver.find_element(By.XPATH, f"//tbody//tr[{row}]//td[10]//span[@class='first-letter-cap field-status']")
                        # card_status_processing = card_status_processing_element.text.strip()
                        
                        # card_status_failed_element = self.driver.find_element(By.XPATH, f"//tbody//tr[{row}]//td[10]//span[@class='first-letter-cap failed-status']")
                        # card_status_failed = card_status_failed_element.text.strip()
                        
                        card_status_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[10]")
                        card_status_text = card_status_element.text.strip()
                        
                        logging.info(f"Card status in row {row}: {card_status_text}")
                        
                        if card_status_text == "completed":
                            logging.info(f"Card creation completed for file: {csv_file_name_text}")
                            
                            # Define the XPaths for the table rows and the Next button
                            total_rows_xpath = "(//table//tbody[@class='vuetable-body'])[2]//tr"
                            next_button_xpath = "(//button[@aria-label='Next Page'])[2]"

                            total_row_count = 0

                            # Click to open the card details
                            open_gc_successfully_loaded_cards_form_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]//div[@class='circular-chevron-wrapper rotate-minus-90']")
                            open_gc_successfully_loaded_cards_form_element.click()
                            time.sleep(2)

                            # Click the select row button
                            click_select_row_button_element = self.driver.find_element(By.XPATH, "(//button[@class='btn dropdown-toggle btn-primary btn-xs'])[2]")
                            click_select_row_button_element.click()
                            time.sleep(2)

                            # Select 100 rows
                            click_select_100_row_button_element = self.driver.find_element(By.XPATH, "(//ul[@role='menu'])[4]//li//a[contains(text(),'100')]")
                            click_select_100_row_button_element.click()
                            time.sleep(2)

                            while True:
                                # Find all rows in the table
                                rows = self.driver.find_elements(By.XPATH, total_rows_xpath)
                                number_of_rows = len(rows)

                                # Update total row count
                                total_row_count += number_of_rows

                                logging.info(f'Number of rows found on this page: {number_of_rows}')
                                
                                for i in range(number_of_rows):
                                    logging.info(f'Processing row {i+1}/{number_of_rows}')
                                
                                # Try to click the Next Page button if it exists
                                try:
                                    next_button_element = self.driver.find_element(By.XPATH, next_button_xpath)
                                    if 'disabled' in next_button_element.get_attribute('class'):
                                        logging.info('No more pages to navigate to.')
                                        break
                                    next_button_element.click()
                                    time.sleep(2)  
                                except Exception as e:
                                    logging.error(f'Next button not found or unable to click: {e}')
                                    break

                            # Click Close Button to close the form
                            click_close_form_button_element = self.driver.find_element(By.XPATH, "//button[@aria-label='Close']")
                            click_close_form_button_element.click()
                            time.sleep(2)

                            # Retrieve and check the number of successfully loaded cards
                            
                            # Extract values from the table cells
                            total_card_request_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[6]").text.strip()
                            cards_created_successfully_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[7]").text.strip()
                            cards_not_created_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[8]").text.strip()
                            
                            total_card_request = int(total_card_request_element)
                            cards_loaded_successfully_count = int(cards_created_successfully_element)
                            cards_not_created = int(cards_not_created_element)
                            
                            logging.info(f'Total number of rows across all pages: {total_row_count}')
                            logging.info(f'Total number of Loaded Successful Cards: {cards_loaded_successfully_count}')
                            
                            # Check if the number of rows matches the number of loaded successful cards
                            if total_row_count == cards_loaded_successfully_count:
                                logging.info('Both counts match.')
                                
                                # Check if the calculation is correct
                                calculation = total_card_request - cards_loaded_successfully_count
                                logging.info(f'Total Card Request: {total_card_request}')
                                logging.info(f'Total Card Successfully Loaded: {cards_loaded_successfully_count}')
                                logging.info(f'Card Not Loaded: {calculation}')
                                logging.info(f'Total Card Successfully Loaded: {cards_loaded_successfully_count} + Card Not Loaded: {calculation} = Total Card Request: {total_card_request}')
                                logging.info("All are Matched.")
                                
                                if calculation == cards_not_created:
                                    logging.info(f'Calculation Match , PASS.')
                                else:
                                    logging.error(f"Calculation mismatch: {calculation} != {cards_not_created}")
                                    return False
                                
                                return True
                            else:
                                logging.error('Total rows and loaded successful cards do not match.')
                                return False
                        
                        elif card_status_text == "processing":
                            logging.info(f"Card creation still processing for file: {csv_file_name_text}")
                            time.sleep(5)
                            break  
                        
                        elif card_status_text == "failed":
                            
                            total_card_request_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[6]").text.strip()
                            cards_not_created_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[8]").text.strip()
                            
                            total_card_request = int(total_card_request_element)
                            cards_not_created = int(cards_not_created_element)
                            
                            logging.info(f'total_card_request: {total_card_request}')
                            logging.info(f'cards_not_created : {cards_not_created}')
                            calculate_result = total_card_request - cards_not_created
                            logging.info(f'{total_card_request} - {cards_not_created} = {calculate_result}')
                            
                            if total_card_request == cards_not_created:
                                logging.error(f"Card creation failed for file: {csv_file_name_text}, Because The result is Zero.")                            
                            else:
                                logging.error(f"Card count mismatch in failed status. Total Requests: {total_card_request}, Not Created: {cards_not_created}.")
                            
                            return False
                        
                        else:
                            return False
    




