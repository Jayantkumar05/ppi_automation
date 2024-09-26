import re
import time  
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.Random_Method import Random_Methods


class OrgLoadAmount:
    
    load_money_button_xpath = "//button[@class='btn ml-3 custom-allocate-money-btn semi-transparent-btn float-right btn-primary']"
    display_bussiness_name_input_xpath = "//div[@class='multiselect multi-select-wrapper flex-grow-1 allocate-money-wrapper']"
    utr_number_input_id = "(//input[@name='amount'])[1]"
    todays_date_xpath = "//span[@class='cell day today']"
    # todays_date_xpath = "//span[@class='cell day today weekend sat']"
    # todays_date_xpath = "//span[@class='cell day today weekend sun']"
    click_calender_dropdown_xpath = "//input[@class='form-control is-valid cursor-pointer']"
    issue_bank_xpath = "//div[@class='multiselect multi-select-wrapper flex-grow-1 org-type-wrapper multiselect--above']"
    enter_amount_input_xpath = "(//input[@class='form-control is-valid'])[2]"
    final_add_money_buton_xpath = "//button[@class='btn custom-allocate-money-btn mt-3 btn-primary']"
    toaxt_test_className = "v-toast__text"
    # ==============================================================================================================================
    check_primary_before_allocation_acount_bal_xpath = "//div[@class='d-flex flex-row justify-content-between']//span[contains(text(),'Account Balance')]//following::h3[1]"
    search_sub_org_xpath = "//input[@placeholder='Display / legal name']"
    click_on_search_sub_org_xapth = "//span[@class='search-icon cursor-pointer fade-in']"
    go_to_the_sub_org_detailed_xpath = "//div[@class='circular-chevron-wrapper rotate-minus-90']"
    get_balanced_of_sub_org_xpath = "//*[@id='subBusinessDetailView___BV_modal_body_']/div/div[1]/div/div[4]/div[1]/h3"
    cancel_sub_org_form_before_allocation_xpath = "//button[@aria-label='Close']"
    
    # ====================================================================================
    
    def __init__(self,driver):
        
        self.driver=driver 
        self.random_methods = Random_Methods() 
    
    # open primary org form
    def click_load_money_button(self):
        load_money_button_element = self.driver.find_element(By.XPATH, self.load_money_button_xpath)
        load_money_button_element.click()
        
    def utr_number_box(self, utr):
        utr_element = self.driver.find_element(By.XPATH, self.utr_number_input_id)
        utr_element.send_keys(utr)
        
    def random_utr_number_box(self):
        random_utr_number = self.random_methods.generate_10_digit_mobile_numbers()
        utr_element = self.driver.find_element(By.XPATH, self.utr_number_input_id)
        utr_element.send_keys(random_utr_number)
        
    def select_today_date(self):
        calender_today_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.todays_date_xpath)))
        calender_today_element.click()
        
    def calender_dropdown(self):
        calender_dropdown_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.click_calender_dropdown_xpath)))
        calender_dropdown_element.click()
        self.select_today_date()     
        
    def amount_box(self, amount):
        amount_element = self.driver.find_element(By.XPATH, self.enter_amount_input_xpath)
        amount_element.send_keys(amount)            
        
    def final_click(self):      
        finally_click = self.driver.find_element(By.XPATH,self.final_add_money_buton_xpath)
        finally_click.click()
    
    def toast_succesfull_message(self):    
        money_added_element = self.driver.find_element(By.CLASS_NAME, self.toaxt_test_className)
        return money_added_element.text
    
    # Checking before allocation primary org ballanced and after primary org ballanced...
    def get_primary_org_balanced(self):
        check_primary_acount_bal_element = self.driver.find_element(By.XPATH, self.check_primary_before_allocation_acount_bal_xpath)            
        return check_primary_acount_bal_element.text
        
    
    def load_money_to_primary_org(self, utr, amount):
        # Click the load amount button
        self.click_load_money_button()
        # Enter UTR
        self.utr_number_box(utr)
        # Enter Date 
        self.calender_dropdown()
        time.sleep(2)
        # Enter Amount
        self.amount_box(amount)
        time.sleep(2)
        # Final submit the form 
        self.final_click()
        time.sleep(2)
    
    def load_money_to_primary_org_for_Bussiness_portal(self, amount):
        # Click the load amount button
        self.click_load_money_button()
        # Enter UTR
        # random_ut_number = self.random_methods.generate_10_digit_mobile_numbers()
        # self.utr_number_box(utr)
        random_utr_number = self.random_utr_number_box()
        # Enter Date 
        self.calender_dropdown()
        time.sleep(2)
        # Enter Amount
        self.amount_box(amount)
        time.sleep(2)
        # Final submit the form 
        self.final_click()
        time.sleep(2)
        
        return random_utr_number
        
        
    # Get money to primary Org
    # Load Money to primary Org
    # Get money to sub Org
    # Load money to sub Org 
        

    
    
    # this is for searching sub org and get balance =============================================================
    
    def search_sub_org(self,legalname):
        #give legal name 
        search_sub_org_element = self.driver.find_element(By.XPATH, self.search_sub_org_xpath)
        search_sub_org_element.send_keys(legalname)
    
    def clear_sub_org(self):
        #give legal name 
        search_sub_org_element = self.driver.find_element(By.XPATH, self.search_sub_org_xpath)
        search_sub_org_element.clear()
    
    def click_on_search_sub_org(self):
        click_on_serch_result_element = self.driver.find_element(By.XPATH, self.click_on_search_sub_org_xapth)    
        click_on_serch_result_element.click()
    
    def go_to_the_sub_org_detailed(self):
        go_to_the_sub_org_detailed_element = self.driver.find_element(By.XPATH, self.go_to_the_sub_org_detailed_xpath)
        go_to_the_sub_org_detailed_element.click()
    
    
    def get_balanced_of_sub_org(self):
        get_balanced_of_sub_org_element = self.driver.find_element(By.XPATH, self.get_balanced_of_sub_org_xpath)
        return get_balanced_of_sub_org_element.text
    
    def close_sub_org_detailed_form(self):
        close_sub_org_detailed_form_element = self.driver.find_element(By.XPATH, self.cancel_sub_org_form_before_allocation_xpath)
        close_sub_org_detailed_form_element.click()
        
    def bussiness_name_box(self,bussinessname):
        search_box_element = self.driver.find_element(By.XPATH, self.display_bussiness_name_input_xpath)
        search_box_element.send_keys(bussinessname) 
    
    def get_sub_org_balanced(self,legalname):
        #search sub org legal name
        self.search_sub_org(legalname) 
        time.sleep(2)
        #click the search option
        self.click_on_search_sub_org() 
        time.sleep(2)
        #Go to the sub org detailed
        self.go_to_the_sub_org_detailed() 
        time.sleep(2)
        #Check the befor load balanced in sub org
        before_Load_balance = self.get_balanced_of_sub_org() 
        time.sleep(2)
        self.close_sub_org_detailed_form()
        time.sleep(2)
        self.clear_sub_org()
        time.sleep(2)
        return before_Load_balance
    
    # YES Bank Sub org Check
    def get_Yes_Bank_sub_org_balanced(self,legalname):
        #search sub org legal name
        self.search_sub_org(legalname) 
        time.sleep(2)
        #click the search option
        self.click_on_search_sub_org() 
        time.sleep(2)
        #Go to the sub org detailed
        self.go_to_the_sub_org_detailed() 
        time.sleep(2)
        #Check the befor load balanced in sub org
        before_Load_balance = self.get_balanced_of_sub_org() 
        time.sleep(2)
        self.close_sub_org_detailed_form()
        time.sleep(2)
        self.clear_sub_org()
        time.sleep(2)
        return before_Load_balance
    
    def load_money_to_sub_org(self, bussinessname, utr, amount):
        # Click the load amount button
        self.click_load_money_button()
        time.sleep(2)
        # Enter Sub org name 
        self.bussiness_name_box(bussinessname + Keys.ENTER)
        time.sleep(2)
        # Enter UTR
        self.utr_number_box(utr)
        # Enter Date 
        self.calender_dropdown()
        time.sleep(2)
        # Enter Amount
        self.amount_box(amount)
        time.sleep(2)
        # Final submit the form 
        self.final_click()
        time.sleep(2)
        
    # ===========================================================
    
    
    
    







