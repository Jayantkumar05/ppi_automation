import time
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class YesBankAllocateMoney:
    
    # Check Money To Sub Org Locators
    search_sub_org_xpath = "//input[@placeholder='Display / legal name']"
    click_on_search_sub_org_xapth = "//span[@class='search-icon cursor-pointer fade-in']"
    go_to_the_sub_org_detailed_xpath = "//div[@class='circular-chevron-wrapper rotate-minus-90']"
    get_balanced_of_sub_org_xpath = "//*[@id='subBusinessDetailView___BV_modal_body_']/div/div[1]/div/div[4]/div[1]/h3"
    cancel_sub_org_form_before_allocation_xpath = "//button[@aria-label='Close']"
    toaxt_test_className = "v-toast__text"
    
    # Allocate Money Locators
    Allocate_Form_Button_ClASS_NAME = "button-slot"
    Input_Bussiness_Name_Xpath = "//input[@aria-label='Amount Input']"
    # Input_Bussiness_Name_Xpath = "(//div[@role='combobox'])[2]"  # if the Bussiness name is shown in the allotcate money box then use it 
    Input_Amount_Number_Xpath = "//input[@name='amount']"
    Submit_Allocate_Money_Button_Xpath = "//button[@type='submit']"
    
    # ====================================================================================
    
    def __init__(self,driver):
        
        self.driver = driver 
        
    # Open Aloocation Form 
    def Allocate_Form_Button(self):
        Allocate_Form_Button_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.Allocate_Form_Button_ClASS_NAME)))
        Allocate_Form_Button_element.click()
        
    # Input Business name for sub org
    def Input_Bussiness_Name(self,businessname):
        Input_Bussiness_Name_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Input_Bussiness_Name_Xpath)))
        Input_Bussiness_Name_element.send_keys(businessname)
        
    # Input Aamount number for sub org
    def Input_Amount_Number(self, amount):
        Input_Amount_Number_element =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Input_Amount_Number_Xpath)))
        Input_Amount_Number_element.send_keys(amount)
        
    # Submit Allocate Button method
    def Submit_Allocate_Money_Button(self):
        Submit_Allocate_Money_Button_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Submit_Allocate_Money_Button_Xpath)))
        Submit_Allocate_Money_Button_element.click()
    
    # this is for searching sub org and get balance =============================================================
    
    def search_sub_org(self,legalname):
        #give legal name 
        search_sub_org_element = self.driver.find_element(By.XPATH, self.search_sub_org_xpath)
        search_sub_org_element.send_keys(legalname)

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

    def clear_sub_org(self):
        #give legal name 
        search_sub_org_element = self.driver.find_element(By.XPATH, self.search_sub_org_xpath)
        search_sub_org_element.clear()
    
    def toast_succesfull_message(self):    
        money_added_element = self.driver.find_element(By.CLASS_NAME, self.toaxt_test_className)
        return money_added_element.text
    
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
    
    # # Allocate Balance To Business.  # If the show bussiness name in allocate button then apply it 
    # def Allocate_Balance_To_Business(self, businessname, amount):
    #     #open Form Button
    #     self.Allocate_Form_Button() 
    #     time.sleep(2)
    #     self.Input_Bussiness_Name(businessname + Keys.ENTER)  
    #     time.sleep(2)
    #     self.Input_Amount_Number(amount) 
    #     time.sleep(2)
    #     self.Submit_Allocate_Money_Button()
    #     time.sleep(2)
        
    # Allocate Balance To Business.
    def Allocate_Balance_To_Business(self, amount):
        #open Form Button
        self.Allocate_Form_Button()   
        time.sleep(2)
        self.Input_Amount_Number(amount) 
        time.sleep(2)
        self.Submit_Allocate_Money_Button()
        time.sleep(2)