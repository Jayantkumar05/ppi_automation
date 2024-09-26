import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountsPage:
    
    # Find Locators
    Click_Business_Page_ID = "sideLi0"
    Click_Accounts_Page_Button_ID = "sideLi3"
    Closing_Balance_Amout_Xpath = "//label[text()='Closing balance']//following-sibling::span"
    Money_Inflow_Amount_Xpath = "//label[text()='Money Inflow']//following-sibling::span"
    Money_Outflow_Amount_Xpath = "//label[text()='Money Outflow']//following-sibling::span"
    
    # Contructor, Taking web driver. 
    def __init__(self,driver):

        self.driver = driver
    
    # Click Business Page
    def Click_Business_Page_Button(self):
        Click_Business_Page_Button_Ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.Click_Business_Page_ID)))
        Click_Business_Page_Button_Ele.click()    
    
    # Click Account Page
    def Click_Accounts_Page_Button(self):
        Click_Accounts_Page_Button_Ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.Click_Accounts_Page_Button_ID)))
        Click_Accounts_Page_Button_Ele.click()
        
    # Get Closing Amount Balance Method
    def Closing_Balance_Amout(self):
        Closing_Balance_Amout_Ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Closing_Balance_Amout_Xpath)))
        return Closing_Balance_Amout_Ele.text
    
    # Get Money Inflow Amount Balance Method
    def Money_Inflow_Amount(self):
        Money_Inflow_Amount_Ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Money_Inflow_Amount_Xpath)))
        return Money_Inflow_Amount_Ele.text    
    
    # Get Closing Amount Balance Method
    def Money_Outflow_Amount(self):
        Money_Outflow_Amount_Ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Money_Outflow_Amount_Xpath)))
        return Money_Outflow_Amount_Ele.text
        
    
    # Methos for Getting Closing Amount Balance
    def Check_Closing_Amount_Balanced(self):
        
        self.Click_Accounts_Page_Button()
        time.sleep(2)
        
        Before_Closing_Balance_amt = self.Closing_Balance_Amout() 
        
        self.Click_Business_Page_Button() 
        time.sleep(2)
        
        return Before_Closing_Balance_amt
        
    # Method  For Match Closing Amount Balance
    def Match_The_closing_Amount_Balanced(self):
        
        self.Click_Accounts_Page_Button()
        time.sleep(2)
        
        After_Closing_Balance_amt = self.Closing_Balance_Amout()

        Money_Inflow_amt = self.Money_Inflow_Amount()
        
        Money_Outflow_amt = self.Money_Outflow_Amount()
        
        return After_Closing_Balance_amt, Money_Inflow_amt, Money_Outflow_amt
        
    # Methos for Getting Money Outflow Amount Balance
    def Check_Money_Outflow_Balanced(self):
        
        # self.Click_Accounts_Page_Button()
        # time.sleep(2)
        
        Money_Outflow_Balance_amt = self.Money_Outflow_Amount() 
        
        self.Click_Business_Page_Button() 
        time.sleep(2)
        
        return Money_Outflow_Balance_amt
        