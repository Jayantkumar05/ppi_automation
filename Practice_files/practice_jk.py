

from faker import Faker
import logging
import os
import csv
import time
import string
import random
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Gc_Bulk_Uploade:
    
    card_button_id = "sideLi1"
    click_gift_card_load_mapping_xpath = "//li[@class='nav-item mr-4 text-center font-weight-bold fs-14']//a[contains(text(),'Gift Card Load and Mapping')]"
    click_load_gift_card_button_xpath = "//button[@class='btn ml-1 add-btn btn-primary']"
    select_the_card_program_xpath = "(//div[@role='combobox'])[2]"
    upload_csv_file_xpath = '//input[@id="uploadCards"]'
    upload_gift_card_data_xpath = "//button[@type='submit']"
    toast_message_xpath = "//p[@class='v-toast__text']"
    check_uploade_status_is_processing_xpath ="//span[@class='first-letter-cap field-status']"
    check_uploade_status_is_complete_xpath = "(//span[@class='first-letter-cap active-status'])[1]"
    total_card_request_xpath = "(//td[@class='text-muted center aligned'])[1]"
    total_card_collect_xpath = "(//td[@class='text-muted center aligned '])[1]"
    
    # ===============================================================================================
    
    # table locators
    total_row_xpath = "//tbody[@class='vuetable-body'][1]//tr" 
    card_module_XPATH =  "//*[@id='cardIcon']"
    gift_card_load_and_mapping_xpath = "/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]"
        
    # ============================================================================================
    
    # Contructor, Taking web driver. 
    def __init__(self,driver):
        
        self.driver = driver
        
    # Open Card section
    def card_button(self):
        card_button_element = self.driver.find_element(By.ID, self.card_button_id)
        card_button_element.click()
        
    def click_gift_card_load_mapping(self):
        click_gift_card_load_mapping_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.click_gift_card_load_mapping_xpath)))
        time.sleep(10)
        click_gift_card_load_mapping_element.click()
        
    def click_load_gift_card_button(self):
        click_load_gift_card_button_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.click_load_gift_card_button_xpath)))
        click_load_gift_card_button_element.click()
    
    def select_the_card_program(self, cardprogram):
        select_the_card_program_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.select_the_card_program_xpath)))
        select_the_card_program_element.send_keys(cardprogram)    

    def upload_csv_file(self, file__path):
        upload_csv_element = self.driver.find_element(By.XPATH,self.upload_csv_file_xpath)
        logging.info("upload_csv_element")
        upload_csv_element.send_keys(file__path)
        
    def uplode_gift_card(self):
        uplode_gift_card_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.upload_gift_card_data_xpath)))
        uplode_gift_card_element.click()
        
    def toast_message(self):
        toast_message_element = self.driver.find_element(By.XPATH, self.toast_message_xpath)
        return toast_message_element.text
    
    #=====================================================================
    # Table locators method 
    
    def Total_row(self):
        Table_Row_element = self.driver.find_element(By.XPATH, self.total_row_xpath)
        return Table_Row_element.text 

    def Card_module(self):
        Card_module_element = self.driver.find_element(By.XPATH, self.card_module_XPATH)
        Card_module_element.click()

    def gift_card_load_anad_mapping(self):
        gift_card_load_anad_mapping_element = self.driver.find_element(By.XPATH, self.gift_card_load_and_mapping_xpath)
        gift_card_load_anad_mapping_element.click()
    
    #===========================================================================================================

    # Load the gift card functionalities...
    def load_gift_card(self,cardprogram, file__path):
        
        # Click card button
        self.card_button()
        logging.info("click the card button")
        time.sleep(2)
        # Click the gift card load mapping link
        self.click_gift_card_load_mapping()
        logging.info("click gift card link")
        time.sleep(2)
        # Click the load gift card button
        self.click_load_gift_card_button()
        logging.info("click the gift card button")
        time.sleep(2)
        # Select the Card program name
        self.select_the_card_program(cardprogram + Keys.ENTER)
        logging.info("enter the card program")
        time.sleep(2)
        # Upload Csv file 
        self.upload_csv_file(file__path)
        logging.info("Uploading the csv file")
        logging.info("file Path Uploaded")
        time.sleep(2)
        #Upload the gift card load..
        self.uplode_gift_card()
        logging.info("click uloading the form button")
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
        # For Correct date --  min_age-19,max_age-60.
        # For Uncorrect date --  min_age-15,max_age-28.
        return faker.date_of_birth(minimum_age=19, maximum_age=60).strftime('%Y-%m-%d')   
    
    # Generating the random email...
    def generate_random_email(self):
        return f"{self.generate_random_name().lower()}@example.com"

    # Taking the random banks...
    def generate_random_bank_name(self):
        banks = ['Deutsche Bank', 'KOTAK MAHINDRA BANK', 'HDFC', 'YESBANK', 'UNION BANK', 'PUNJAB & SIND BANK', 'PUNJAB NATIONAL BANK']
        return random.choice(banks)
    
    # Downloading the csv file in the test_data folder    
    def create_csv_file_for_gc_upload(self, number_of_rows):
        
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
                    'MOBILE': self.generate_random_mobile(),
                    'DOB': self.generate_random_dob(),
                    'NAME_ON_CARD': self.generate_random_bank_name(),
                    'EMAIL': self.generate_random_email(),
                })
                
                
            return  os.path.abspath(file_path), f"GC_bulk_uploade_{timestamp}.csv"
            
        
    #===================================================================================================
  
    def verify_latest_csv_upload(self, uploaded_file_name, check_interval=10, max_retries=100):
        retries = 0

        while retries < max_retries:
            file_found = False

            # Try to refresh the page or section where the table is located
            try:
                refresh_element = self.driver.find_element(By.XPATH, "//div[@class='ml-3']/div")
                refresh_element.click()
                logging.info('Refreshed the page.')
                time.sleep(2)  # Allow time for the page to refresh and update
            except Exception as e:
                logging.warning(f"Refresh button not found or unable to click: {e}")
            
            # Get all rows in the table
            table_row = self.Total_row()
            
            for row in range(1, len(table_row) + 1):
                try:
                    # Get the CSV file name from the 4th column of this row
                    csv_file_name_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[4]")
                    csv_file_name_text = csv_file_name_element.text.strip()   
                    
                    logging.info(f"Checking row {row} for CSV file: {csv_file_name_text}")

                    if csv_file_name_text.lower() == uploaded_file_name.lower():
                        logging.info(f"File name matched in row {row}: {csv_file_name_text}")
                        file_found = True

                        # Check the card status in the 10th column of the same row
                        card_status_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[10]")
                        card_status_text = card_status_element.text.strip().lower()
                        
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
                            try:
                                total_card_request_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[5]").text.strip()
                                cards_loaded_successfully_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[6]").text.strip()
                                cards_not_created_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[7]").text.strip()
                                
                                total_card_request = int(total_card_request_element)
                                cards_loaded_successfully_count = int(cards_loaded_successfully_element)
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
                            except ValueError as e:
                                logging.error(f"Failed to parse card counts: {e}")
                                return False
                            
                        elif card_status_text == "processing":
                            logging.info(f"Card creation still processing for file: {csv_file_name_text}")
                            break  # Exit the row check to retry after waiting
                        
                        elif card_status_text == "failed":
                            logging.error(f"Card creation failed for file: {csv_file_name_text}")

                            try:
                                # Extract values from the table cells
                                total_card_request_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[5]").text.strip()
                                cards_loaded_successfully_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[6]").text.strip()
                                cards_not_created_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[7]").text.strip()
                                total_card_request = int(total_card_request_element)
                                cards_loaded_successfully_count = int(cards_loaded_successfully_element)
                                cards_not_created = int(cards_not_created_element)
                                
                                # Retrieve the expected result from column 10 
                                actual_result_element = self.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[10]//span[@class='reason-wrapper']")
                                actual_result = actual_result_element.text.strip()
                                
                                # Check if the number of rows matches the number of loaded successful cards
                                if total_card_request == 0 and cards_loaded_successfully_count == 0 and cards_not_created == 0:
                                    # Log actual result
                                    logging.info(f"Failed status detected. Actual result: {actual_result}")
                                    return actual_result
                                
                                else:
                                    # Log the mismatch if total values do not match
                                    logging.error(f"Card count mismatch in failed status. Total Requests: {total_card_request}, Loaded Successfully: {cards_loaded_successfully_count}, Not Created: {cards_not_created}.")
                                    return False

                            except Exception as e:
                                logging.error(f"Error processing failed status for row {row}: {e}")
                                return False

                        else:
                            logging.info(f"Card status is {card_status_text}. Retrying...")
                
                except Exception as e:
                    logging.error(f"Error processing row {row}: {e}")
            
            if not file_found:
                logging.info(f"No match found for {uploaded_file_name}. Retrying...")
            
            retries += 1
            logging.info(f"Retry {retries}/{max_retries}. Waiting {check_interval} seconds before retrying.")
            time.sleep(check_interval)
        
        logging.error(f"File {uploaded_file_name} did not reach 'Completed' status after {max_retries} retries.")
        return False










