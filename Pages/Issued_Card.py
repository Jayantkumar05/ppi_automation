import logging
import random
import string
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Utility.min_kyc_yes import Yes_Min_KYC 



class Issued_Card_class:
    
    Click_Card_Btn_Id = "sideLi1"
    Click_Issue_Card_Form_Xpath = "//button[@class='btn add-btn btn-primary']"
    Name_Input_Xpath = "(//input[@class='form-control is-valid'])[1]"
    Name_On_Card_xpath = "(//input[@class='form-control is-valid'])[2]"
    Mobile_Number_xpath = "(//input[@class='form-control is-valid'])[3]"
    Select_Card_Program_xpath = "(//div[@role='combobox'])[1]"
    Wallet_Xpath = "//input[@aria-label='smart wallets']"
    Calender_Input_Xpath = "//input[@name='DOB']"
    
    # Digital Card Locators GC========================================================================
    D_Digital_Card_Type_Xpath = "(//div[@class='card-body'])[2]"
    D_Adress_house_Digital_xpath = "(//input[@class='form-control is-valid'])[7]"
    D_Area_Name_Xpath = "(//input[@class='form-control is-valid'])[8]"
    D_Landmark_Xpath = "(//input[@class='form-control is-valid'])[9]"
    D_Pincode_Xpath = "(//input[@class='form-control is-valid'])[10]"
    D_City_Xpath = "(//input[@class='form-control is-valid'])[11]"
    D_State_Xpath = "(//input[@class='form-control is-valid'])[12]"
    
    # Digital Card Locators For GPR ================================================================
    D_Choose_Document_Type_Xpath = "(//div[@role='combobox'])[2]"
    D_Input_Document_Value_classname = "//input[@name='docValue']"
    D_Select_Gender_Xpath = "(//div[@role='combobox'])[3]"
    
    # Personalized Card Locators GC ================================================================
    P_Personalized_Card_Type_xpath = "(//div[@class='card-body'])[3]"
    
    # Insta Card Locators ==========================================================================
    I_Input_Kit_Number_Xpath = "//input[@name='Kit No.']"
    I_Adress_house_number_Xpath = "(//input[@class='form-control is-valid'])[8]"
    I_Area_Name_Xpath = "(//input[@class='form-control is-valid'])[9]"
    I_Landmark_Xpath = "(//input[@class='form-control is-valid'])[10]"
    I_Pincode_Xpath = "(//input[@class='form-control is-valid'])[11]"
    I_City_Xpath = "(//input[@class='form-control is-valid'])[12]"
    I_State_Xpath = "(//input[@class='form-control is-valid'])[13]"
    
    # For YES BANK Locators GPR =====================================================================
    Displayed_Business_Name_Xpath = "(//div[@class='multiselect multi-select-wrapper flex-grow-1 org-type-wrapper'])[1]"
    Select_The_Card_Program_Xpath = "(//div[@class='multiselect multi-select-wrapper flex-grow-1 org-type-wrapper'])[2]"
    Wallet_First_Input_Box_Xpath = "(//input[@name='amount'])[1]"
    Wallet_Second_Input_Box_Xpath = "(//input[@name='amount'])[2]"
    Issued_card_toast_message_Xpath = "//p[@class='v-toast__text']"
    Search_Mobile_In_Yes_Bank_Xpath = "(//input[@type='text'])[1]"
    Click_Search_option_Xpath = "//span[@class='search-icon cursor-pointer fade-in']"
    Croxx_Search_option_Xpath = "//span[@class='close-icon cursor-pointer rotate-in-animation']"
    
    # Table Row Kyc Verification 
    Table_Row_Before_Card_Holder_Name_Xpath = "//table//tbody//tr//td[3]"
    Table_Row_Before_Card_Status_Xpath = "//table//tbody//tr//td[10]"
    
    # For load Or Withdraw Money in GPR Locators 
    Business_Page_ID = "sideLi0"
    Click_Card_Program_Xpath = "(//ul[@role='tablist']//li[@role='presentation'])[2]"
    Click_GPR_Card_Program_Xpath = "//div[@class='scroll-without-scrollbar']//div//button"
    # Take_Wallet_Name_Xpath = '//*[@id="groupDetailModal___BV_modal_body_"]/div/div[5]/div[2]/span/div[1]/div/div[1]/div/button/div/text()'
    Take_Wallet_Name_Xpath = " (//div[contains(text(), 'asdfasdf')])[3]"
    Click_Croxx_Button_Xpath = "//button[@Class='close']"
    Detailed_Table_Xpath = "(//table//tbody)[2]"
    Load_Money_Button_Xpath = "(//div[@class='card-detail-right']//section[@class='card-detail-action mr-4']//button[@type='submit'])[1]"
    Select_User_Name_Match_Xpath = "//form//div[@class='row']//div[text()='asdfasdf']"
    Load_Money_INput_Box_Xpath = "(//input[@id='amount-input-undefined'])[1]"
    Click_Add_Money_Submit_button_Xpath = "//button[contains(text(), 'Add Money')]"
    Toast_Message_Xpath = "//p[@class='v-toast__text']"
    Withdwal_Fund_Button_Xpath = "(//button[contains(text(), 'Withdraw Fund')])[1]"
    Click_withdrwal_Money_Submit_button_Xpath = "(//button[contains(text(), 'Withdraw Fund')])[2]"
    # Locators For Freeze Card 
    Freeze_Card_Button_Xpath = "//button[normalize-space(text())='Freeze Card']"
    UnFreeze_Card_Button_Xpath = "//button[normalize-space(text())='Unfreeze Card']"
    Conform_Freeze_Card_Button_Xpath = "//button[normalize-space(text())='Yes, Freeze Card']"
    Conform_UnFreeze_Card_Button_Xpath = "//button[normalize-space(text())='Yes, Unfreeze Card']"
    Get_Toast_Message_Class_Name = "v-toast__text" 
    # Locatore For Block Card
    Block_Card_Button_Xpath = "//button[normalize-space(text())='Block Card']"
    Conform_Block_Card_Button_Xpath = "//button[normalize-space(text())='Yes, Block Card']"
    Double_Conform_Block_Card_Button_Xpath = "//button[text()='Block']"
    Click_Damage_Input_Buttom_Xpath = "(//input[@type='radio'])[9]"
     
    # ===============================================================================================
    
    Click_Issued_Card_Button_Xpath = "//button[@type='submit']" 
    Toast_Message_Xpath = "//p[contains(text(),'Card creation is in progress')]"
    Form_Close_cross_button_xpath = "//button[@aria-label='Close']"
    
    # Contructor, Taking web driver. 
    def __init__(self,driver):

        self.driver = driver
    
    def Click_Card_Btn(self):
        Click_Card_Btn_element = self.driver.find_element(By.ID, self.Click_Card_Btn_Id)
        Click_Card_Btn_element.click()
        
    def Click_Issue_Card_Form(self):
        Click_Issue_Card_Form_Xpath_element = self.driver.find_element(By.XPATH, self.Click_Issue_Card_Form_Xpath) 
        time.sleep(2)
        Click_Issue_Card_Form_Xpath_element.click()
        
    def Name_Input(self, name):
        Name_Input_element = self.driver.find_element(By.XPATH, self.Name_Input_Xpath)
        Name_Input_element.send_keys(name)
        
    def Name_On_Card(self,cardname):
        Name_On_Card_element = self.driver.find_element(By.XPATH, self.Name_On_Card_xpath)
        Name_On_Card_element.send_keys(cardname)        
    
    #========================Fill Input Random Mobile Number method======================#
    # def Mobile_Number(self, mobile):
    #     Mobile_Number_element = self.driver.find_element(By.XPATH, self.Mobile_Number_xpath)
    #     Mobile_Number_element.send_keys(mobile)

    # def generate_random_mobile(self):
    #     # Generate a random 10-digit mobile number
    #     return f"{random.randint(6000000000, 9999999999)}"

    # def fill_mobile_number(self):
    #     random_mobile = self.generate_random_mobile()
    #     self.Mobile_Number(random_mobile)
    
    def fill_random_mobile_number(self):
        # Generate a random 10-digit mobile number
        random_mobile = f"{random.randint(6000000000, 9999999999)}"

        # Find the mobile number element and fill it with the random mobile number
        mobile_number_element = self.driver.find_element(By.XPATH, self.Mobile_Number_xpath)
        mobile_number_element.send_keys(random_mobile)
        return random_mobile
    #=====================================================================================#   
    
    def Select_Card_Program(self,cardprogram):
        Select_Card_Program_element = self.driver.find_element(By.XPATH, self.Select_Card_Program_xpath)
        Select_Card_Program_element.send_keys(cardprogram)
        
    def Wallet(self,wallet):
        Wallet_element = self.driver.find_element(By.XPATH, self.Wallet_Xpath)
        Wallet_element.send_keys(wallet)
        
    def Calender_Input(self, calender):
        Calender_Input_element = self.driver.find_element(By.XPATH, self.Calender_Input_Xpath)
        Calender_Input_element.send_keys(calender)

    # Digital Card Methods GC =============================================================================

    def Digital_Card_Type(self):
        Digital_Card_Type_element = self.driver.find_element(By.XPATH, self.D_Digital_Card_Type_Xpath)
        Digital_Card_Type_element.click()

    def D_Digital_house_number(self, housenum):
        Adress_house_number_element = self.driver.find_element(By.XPATH, self.D_Adress_house_Digital_xpath)
        Adress_house_number_element.send_keys(housenum)
        
    def D_Area_Name(self, area):
        Area_Name_element = self.driver.find_element(By.XPATH, self.D_Area_Name_Xpath)
        Area_Name_element.send_keys(area)
        
    def D_Landmark(self, landmark):
        Landmark_element = self.driver.find_element(By.XPATH, self.D_Landmark_Xpath)
        Landmark_element.send_keys(landmark)
        
    def D_Pincode(self, pincode):
        Pincode_element = self.driver.find_element(By.XPATH, self.D_Pincode_Xpath)
        Pincode_element.send_keys(pincode)
        
    def D_City(self, city):
        City_element = self.driver.find_element(By.XPATH, self.D_City_Xpath)
        City_element.send_keys(city)
        
    def D_State(self, state):
        State_element = self.driver.find_element(By.XPATH, self.D_State_Xpath)
        State_element.send_keys(state)

    # Digital Card Methods GPR =============================================================================
    def Choose_Document_Type(self, Document):
        Choose_Document_Type_element = self.driver.find_element(By.XPATH, self.D_Choose_Document_Type_Xpath)
        Choose_Document_Type_element.send_keys(Document)
        
    def Input_Document_Value(self, aadhar):
        Input_Document_Value_element = self.driver.find_element(By.XPATH, self.D_Input_Document_Value_classname)
        Input_Document_Value_element.send_keys(aadhar)
        
    def Select_Gender(self, gender):
        State_element = self.driver.find_element(By.XPATH, self.D_Select_Gender_Xpath)
        State_element.send_keys(gender)


    # Personalized Card Methods GC =========================================================================
    
    def Personalized_Card_Type(self):
        Digital_Card_Type_element = self.driver.find_element(By.XPATH, self.P_Personalized_Card_Type_xpath)
        Digital_Card_Type_element.click()
    
    # Insta Card mathods ================================================================================
    
    def I_Input_Kit_Number(self,Inputkitnumber):
        select_card_program_dropdown_element = self.driver.find_element(By.XPATH, self.I_Input_Kit_Number_Xpath)
        select_card_program_dropdown_element.send_keys(Inputkitnumber)
    
    def I_Adress_house_number(self, housenum):
        Adress_house_number_element = self.driver.find_element(By.XPATH, self.I_Adress_house_number_Xpath)
        Adress_house_number_element.send_keys(housenum)
            
    def I_Area_Name(self, area):
        Area_Name_element = self.driver.find_element(By.XPATH, self.I_Area_Name_Xpath)
        Area_Name_element.send_keys(area)
        
    def I_Landmark(self, landmark):
        Landmark_element = self.driver.find_element(By.XPATH, self.I_Landmark_Xpath)
        Landmark_element.send_keys(landmark)
        
    def I_Pincode(self, pincode):
        Pincode_element = self.driver.find_element(By.XPATH, self.I_Pincode_Xpath)
        Pincode_element.send_keys(pincode)
        
    def I_City(self, city):
        City_element = self.driver.find_element(By.XPATH, self.I_City_Xpath)
        City_element.send_keys(city)
        
    def I_State(self, state):
        State_element = self.driver.find_element(By.XPATH, self.I_State_Xpath)
        State_element.send_keys(state)
    
    # =============================================================================================================

    def Click_Issued_Card_Button(self):
        Click_Issued_Card_Button_element = self.driver.find_element(By.XPATH, self.Click_Issued_Card_Button_Xpath)
        Click_Issued_Card_Button_element.click()
    
    def Card_Creation_Progress_Toast_Message(self):
        Toast_Message_element = self.driver.find_element(By.XPATH, self.Toast_Message_Xpath)
        return Toast_Message_element.text
    
    def Form_Close_cross_button(self):
        Form_Close_cross_button_element = self.driver.find_element(By.XPATH, self.Form_Close_cross_button_xpath)
        Form_Close_cross_button_element.click()
    
    # Mathods for Yes Bank ===============================================================================================================        

    # Input Bussiness name for Yes Bank. 
    # def Displayed_Business_Name(self, businessname):
    #     Displayed_Business_Name_element = self.driver.find_element(By.XPATH, self.Displayed_Business_Name_Xpath)
    #     Displayed_Business_Name_element.send_keys(businessname + Keys.ENTER)

    def Displayed_Business_Name(self, businessname):
         
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Displayed_Business_Name_Xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # element.clear()   
        element.send_keys(businessname)
        # element.send_keys(Keys.ENTER)
        time.sleep(1)
    
    # Select the card program for Yes Bank. 
    def Select_The_Card_Program(self, cardprogram):
        Select_The_Card_Program_element = self.driver.find_element(By.XPATH, self.Select_The_Card_Program_Xpath)
        Select_The_Card_Program_element.send_keys(cardprogram + Keys.ENTER)
        
    # Input amount for wallet 1 Inbox for Yes Bank.
    def Wallet_First_Input_Box(self, wallet1):
        Wallet_First_Input_Box_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Wallet_First_Input_Box_Xpath)))
        Wallet_First_Input_Box_element.send_keys(wallet1)
        
    # Input amount for wallet 2 Inbox for Yes Bank. 
    def Wallet_Second_Input_Box(self, wallet2):
        Wallet_Second_Input_Box_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Wallet_Second_Input_Box_Xpath)))
        Wallet_Second_Input_Box_element.send_keys(wallet2)
        
    # Successfully Issued Card Toast Message 
    def Issued_card_toast_message(self):
        Issued_card_toast_message_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Issued_card_toast_message_Xpath)))
        return Issued_card_toast_message_element.text
    
    # Search the mobile number in the table 
    def Search_Mobile_In_Yes_Bank(self, mobile):
        Search_Mobile_In_Yes_Bank_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Search_Mobile_In_Yes_Bank_Xpath)))
        Search_Mobile_In_Yes_Bank_element.send_keys(mobile)
    
    def clear_Mobile_In_Yes_Bank(self):
        Search_Mobile_In_Yes_Bank_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Search_Mobile_In_Yes_Bank_Xpath)))
        Search_Mobile_In_Yes_Bank_element.clear()
    
    # Click the search icon for search the same the mobile number in the table 
    def Click_Search_option(self):
        Click_Search_option_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Click_Search_option_Xpath)))
        Click_Search_option_element.click()
        
    def generate_random_name(self):
        length = random.randint(2, 25)
        name = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        Name_Input_element = self.driver.find_element(By.XPATH, self.Name_Input_Xpath)
        Name_Input_element.send_keys(name)
        return name.capitalize()
    
    def Table_Row_Before_Card_Holder_Name(self):
        Before_Card_holder_Name_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Table_Row_Before_Card_Holder_Name_Xpath)))
        return Before_Card_holder_Name_element.text
    
    def Table_Row_Before_Card_Sattus(self):
        Before_Card_holder_Name_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Table_Row_Before_Card_Status_Xpath)))
        return Before_Card_holder_Name_element.text
    
    # Methods For Load And Withdrawl Money.
    def Click_Business_Page(self):
        Business_Page_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.Business_Page_ID)))
        Business_Page_ele.click()   
    
    def Click_Card_Program(self):
        Click_Card_Program_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Click_Card_Program_Xpath)))
        Click_Card_Program_ele.click()
        
    def Click_GPR_Card_Program(self):
        Click_GPR_Card_Program_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Click_GPR_Card_Program_Xpath)))
        Click_GPR_Card_Program_ele.click()
        

    def Take_Wallet_Name(self):
        Take_Wallet_Name_ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Take_Wallet_Name_Xpath)))
        wallet_name = Take_Wallet_Name_ele.text.strip()   

        if "default" in wallet_name:
            wallet_name = wallet_name.split()[0]  

        return wallet_name
    
    def Click_Croxx_Button(self):
        Click_Croxx_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Click_Croxx_Button_Xpath)))
        Click_Croxx_Button_ele.click()
        
    def Load_Money_INput_Box(self,amt):
        Load_Money_INput_Box_ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Load_Money_INput_Box_Xpath)))
        Load_Money_INput_Box_ele.send_keys(amt)
        
    def Load_Money_Button(self):
        Load_Money_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Load_Money_Button_Xpath)))
        Load_Money_Button_ele.click()
        
    def Detailed_Table(self):
        Detailed_Table_ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Detailed_Table_Xpath)))
        return Detailed_Table_ele.text
    
    def Click_Add_Money_Submit_button(self):
        Click_Add_Money_Submit_button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Click_Add_Money_Submit_button_Xpath)))
        Click_Add_Money_Submit_button_ele.click()
        
    
    def Toast_Message(self):
        Toast_Message_ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Toast_Message_Xpath)))
        return Toast_Message_ele.text
    
    def Withdwal_Fund_Button(self):
        Withdwal_Fund_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Withdwal_Fund_Button_Xpath)))
        Withdwal_Fund_Button_ele.click()
        
    def Click_withdrwal_Money_Submit_button(self):
        Click_withdrwal_Money_Submit_button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Click_withdrwal_Money_Submit_button_Xpath)))
        Click_withdrwal_Money_Submit_button_ele.click()
    
    def Croxx_Search_option(self):
        Croxx_Search_option_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Croxx_Search_option_Xpath)))
        Croxx_Search_option_ele.click()
        
    def Click_Freeze_Card_Button(self):
        Freeze_Card_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Freeze_Card_Button_Xpath)))
        Freeze_Card_Button_ele.click()
        
    def Click_Conform_Freeze_Card_Button(self):
        Conform_Freeze_Card_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Conform_Freeze_Card_Button_Xpath)))
        Conform_Freeze_Card_Button_ele.click()

    def Click_UnFreeze_Card_Button(self):
        UnFreeze_Card_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.UnFreeze_Card_Button_Xpath)))
        UnFreeze_Card_Button_ele.click()
        
    def Click_Conform_UnFreeze_Card_Button(self):
        Conform_UnFreeze_Card_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Conform_UnFreeze_Card_Button_Xpath)))
        Conform_UnFreeze_Card_Button_ele.click()
        
    def Click_Block_Card_Button(self):
        Block_Card_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Block_Card_Button_Xpath)))
        Block_Card_Button_ele.click()
        
    def Click_Conform_Block_Card_Button(self):
        Conform_Block_Card_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Conform_Block_Card_Button_Xpath)))
        Conform_Block_Card_Button_ele.click()
        
    def Click_Double_Conform_Block_Card_Button_Xpath(self):
        Double_Conform_Block_Card_Button_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Double_Conform_Block_Card_Button_Xpath)))
        Double_Conform_Block_Card_Button_ele.click()
          
    def Click_Damage_Input_Buttom(self):
        Click_Damage_Input_Buttom_ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Click_Damage_Input_Buttom_Xpath)))
        Click_Damage_Input_Buttom_ele.click()
        
    def Get_Toast_Message(self):
        Get_Toast_Message_ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Get_Toast_Message_Class_Name)))
        return Get_Toast_Message_ele.text
        
        
    # ==========================================================================================================================================================
        
    # Mwthod to Issue Digitl GC..
    def Issued_Digital_card_to_GC(self, name, cardname, mobile, cardprogram, wallet,
                           calender, housenum, area, landmark, pincode, city, state):
        self.Click_Card_Btn()
        time.sleep(2)
        self.Click_Issue_Card_Form()
        time.sleep(2)
        self.Name_Input(name)
        time.sleep(2)
        self.Name_On_Card(cardname)
        time.sleep(2)
        # self.Mobile_Number(mobile) 
        time.sleep(2)
        self.Select_Card_Program(cardprogram + Keys.ENTER)
        time.sleep(2)
        self.Digital_Card_Type()
        time.sleep(2)
        self.Wallet(wallet)
        time.sleep(2)
        self.Calender_Input(calender)
        time.sleep(2)
        self.D_Digital_house_number(housenum)
        time.sleep(2)
        self.D_Area_Name(area)
        time.sleep(2)
        self.D_Landmark(landmark)
        time.sleep(2)
        self.D_Pincode(pincode)
        time.sleep(2)
        self.D_City(city)
        time.sleep(2)
        self.D_State(state)
        time.sleep(2)
        self.Click_Issued_Card_Button()
        time.sleep(15)
        
    # Mwthod to Issue Personalized GC..
    def Issued_Personalized_card_to_GC(self, name, cardname, mobile, cardprogram, wallet,
                           calender, housenum, area, landmark, pincode, city, state):
        self.Click_Card_Btn()
        time.sleep(2)
        self.Click_Issue_Card_Form()
        time.sleep(2)
        self.Name_Input(name)
        time.sleep(2)
        self.Name_On_Card(cardname)
        time.sleep(2)
        # self.Mobile_Number(mobile) 
        time.sleep(2)
        self.Personalized_Card_Type()
        time.sleep(2)
        self.Select_Card_Program(cardprogram + Keys.ENTER)
        time.sleep(2)
        self.Wallet(wallet)
        time.sleep(2)
        self.Calender_Input(calender)
        time.sleep(2)
        self.D_Digital_house_number(housenum)
        time.sleep(2)
        self.D_Area_Name(area)
        time.sleep(2)
        self.D_Landmark(landmark)
        time.sleep(2)
        self.D_Pincode(pincode)
        time.sleep(2)
        self.D_City(city)
        time.sleep(2)
        self.D_State(state)
        time.sleep(2)
        self.Click_Issued_Card_Button()
        time.sleep(15)

    
    # Mwthod to Issued Insta GC..
    def Issued_Insta_card_to_GC(self, name, cardname, cardprogram, kitnumber, wallet,
                           calender, housenum, area, landmark, pincode, city, state):
        self.Click_Card_Btn()
        time.sleep(2)
        self.Click_Issue_Card_Form()
        time.sleep(2)
        self.Name_Input(name)
        time.sleep(2)
        self.Name_On_Card(cardname)
        time.sleep(2)
        # self.fill_mobile_number() 
        time.sleep(2)
        self.Select_Card_Program(cardprogram + Keys.ENTER)
        time.sleep(2)
        self.I_Input_Kit_Number(kitnumber)
        time.sleep(2)
        self.Wallet(wallet)
        time.sleep(2)
        self.Calender_Input(calender)
        time.sleep(2)
        self.I_Adress_house_number(housenum)
        time.sleep(2)
        self.I_Area_Name(area)
        time.sleep(2)
        self.I_Landmark(landmark)
        time.sleep(2)
        self.I_Pincode(pincode)
        time.sleep(2)
        self.I_City(city)
        time.sleep(2)
        self.I_State(state)
        time.sleep(2)
        self.Click_Issued_Card_Button()
        time.sleep(15)
        
    # Mwthod to Issue Digitl GPR Card..
    def Issued_Digital_card_to_GPR(self, name, cardname, mobile, cardprogram, wallet,
                           Document, aadhar, calender,gender, housenum, area, landmark, pincode, city, state):
        self.Click_Card_Btn()
        time.sleep(2)
        self.Click_Issue_Card_Form()
        time.sleep(2)
        self.Name_Input(name)
        time.sleep(2)
        self.Name_On_Card(cardname)
        time.sleep(2)
        # self.Mobile_Number(mobile) 
        time.sleep(2)
        self.Digital_Card_Type()
        time.sleep(2)
        self.Select_Card_Program(cardprogram + Keys.ENTER)
        time.sleep(2)
        self.Wallet(wallet)
        time.sleep(2)
        self.Choose_Document_Type(Document + Keys.ENTER)
        time.sleep(2)
        self.Input_Document_Value(aadhar)
        time.sleep(2)
        self.Calender_Input(calender)
        time.sleep(2)
        self.Select_Gender(gender + Keys.ENTER)
        time.sleep(2)
        self.I_Adress_house_number(housenum)
        time.sleep(2)
        self.I_Area_Name(area)
        time.sleep(2)
        self.I_Landmark(landmark)
        time.sleep(2)
        self.I_Pincode(pincode)
        time.sleep(2)
        self.I_City(city)
        time.sleep(2)
        self.I_State(state)
        time.sleep(2)
        self.Click_Issued_Card_Button()
        time.sleep(15)    
        
    # Mwthod to Issue Personalized GPR Card..
    def Issued_Personalized_card_to_GPR(self, name, cardname, mobile, cardprogram, wallet,
                           Document, aadhar, calender,gender, housenum, area, landmark, pincode, city, state):
        self.Click_Card_Btn()
        time.sleep(2)
        self.Click_Issue_Card_Form()
        time.sleep(2)
        self.Name_Input(name)
        time.sleep(2)
        self.Name_On_Card(cardname)
        time.sleep(2)
        # self.Mobile_Number(mobile) 
        time.sleep(2)
        self.Select_Card_Program(cardprogram + Keys.ENTER)
        time.sleep(2)
        self.Personalized_Card_Type()
        time.sleep(2) 
        self.Wallet(wallet)
        time.sleep(2)
        self.Choose_Document_Type(Document + Keys.ENTER)
        time.sleep(2)
        self.Input_Document_Value(aadhar)
        time.sleep(2)
        self.Calender_Input(calender)
        time.sleep(2)
        self.Select_Gender(gender + Keys.ENTER)
        time.sleep(2)
        self.I_Adress_house_number(housenum)
        time.sleep(2)
        self.I_Area_Name(area)
        time.sleep(2)
        self.I_Landmark(landmark)
        time.sleep(2)
        self.I_Pincode(pincode)
        time.sleep(2)
        self.I_City(city)
        time.sleep(2)
        self.I_State(state)
        time.sleep(2)
        self.Click_Issued_Card_Button()
        time.sleep(5)
    
    
  # Mwthod to Issue Insta GPR Card..
    def Issued_Insta_card_to_GPR(self, name, cardname, mobile, cardprogram, wallet,
                           Document, aadhar, calender,gender, housenum, area, landmark, pincode, city, state):
        self.Click_Card_Btn()
        time.sleep(2)
        self.Click_Issue_Card_Form()
        time.sleep(2)
        self.Name_Input(name)
        time.sleep(2)
        self.Name_On_Card(cardname)
        time.sleep(2)
        # self.Mobile_Number(mobile) 
        time.sleep(2) 
        self.Select_Card_Program(cardprogram + Keys.ENTER)
        time.sleep(2)
        self.Wallet(wallet)
        time.sleep(2)
        self.Choose_Document_Type(Document + Keys.ENTER)
        time.sleep(2)
        self.Input_Document_Value(aadhar)
        time.sleep(2)
        self.Calender_Input(calender)
        time.sleep(2)
        self.Select_Gender(gender + Keys.ENTER)
        time.sleep(2)
        self.I_Adress_house_number(housenum)
        time.sleep(2)
        self.I_Area_Name(area)
        time.sleep(2)
        self.I_Landmark(landmark)
        time.sleep(2)
        self.I_Pincode(pincode)
        time.sleep(2)
        self.I_City(city)
        time.sleep(2)
        self.I_State(state)
        time.sleep(2)
        self.Click_Issued_Card_Button()
        time.sleep(5)    
  
    
    # Mwthod to Issue Personalized GPR Card For Yes Bank Allocation...
    def Issued_Personalized_card_to_GPR_for_Yes_Bank(self, cardname, businessname, 
                                                     cardprogram, wallet1, wallet2):

        self.Click_Card_Btn()
        time.sleep(2)
        self.Click_Issue_Card_Form()
        time.sleep(2) 
        random_name = self.generate_random_name()
        # time.sleep(2)
        self.Name_On_Card(cardname)
        # time.sleep(2)  
        random_mobile = self.fill_random_mobile_number()
        time.sleep(2)
        self.Personalized_Card_Type()
        time.sleep(2)

        # Ensure proper input and interaction with business name
        self.Displayed_Business_Name(businessname + Keys.ENTER)
        print("Business Name Entered")

        time.sleep(2)

        # Ensure proper input and interaction with card program
        self.Select_The_Card_Program(cardprogram + Keys.ENTER)
        print("Card Program Selected")
        
        time.sleep(2)
        time.sleep(2)
        self.Wallet_First_Input_Box(wallet1)
        # time.sleep(2)
        self.Wallet_Second_Input_Box(wallet2)
        # time.sleep(2)
        self.D_Digital_house_number("housenum")
        # time.sleep(2)
        self.D_Area_Name("area")
        # time.sleep(2)
        self.D_Landmark("landmark")
        # time.sleep(2)
        self.D_Pincode("637827")
        # time.sleep(2)
        self.D_City("Bangalore")
        # time.sleep(2)
        self.D_State("Karnataka")
        time.sleep(2)
        self.Click_Issued_Card_Button()
        time.sleep(2)
        
        return random_mobile, random_name
    
  
    # Checking verification Issued_Personalized_card_Table_to_GPR_Card_for_Yes_Bank.
    
    def Do_YES_Min_KYC_For_Personalized_Issued_Card(self,random_mobile, random_name):
        
        self.Click_Card_Btn()
        time.sleep(2)       
        # Search the latest Issue Personalized card through Phone Number.  
        self.Search_Mobile_In_Yes_Bank(random_mobile)
        time.sleep(2)  
        
        self.Click_Search_option() 
        time.sleep(2) 
        
        kyc_processor = Yes_Min_KYC(mob = random_mobile, name = random_name)
        
        status_code = kyc_processor.submit_Aadhaar_MIN_KYC()
        
        logging.info(f"KYC Submission Status Code: {status_code}")
        
        if status_code == 200:
            logging.info("KYC submission successful.")
        else:
            logging.info("KYC submission failed.")
            
        time.sleep(2)                 
        
        
    def Check_Verification_Issued_Personalized_card_to_GPR_for_Yes_Bank(self, random_mobile, random_name):
        
        # Check After Kyc Card Status
        Before_Card_holder_Name = self.Table_Row_Before_Card_Holder_Name()
        Before_Card_Status = self.Table_Row_Before_Card_Sattus()
        
        self.Do_YES_Min_KYC_For_Personalized_Issued_Card(random_mobile, random_name)
         
        
        After_Card_Status_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//table//tbody//tr//td[10]')))
        After_Card_Status = After_Card_Status_element.text
        
        if Before_Card_Status != After_Card_Status:
             
            self.Click_Business_Page()
            time.sleep(2)
            self.Click_Card_Btn()
            time.sleep(2)
            self.Search_Mobile_In_Yes_Bank(random_mobile)
            time.sleep(2)  
            
            self.Click_Search_option() 
            time.sleep(2)
            
            
            logging.info(f"Status changed from {Before_Card_Status} to {After_Card_Status}.")
                    
        else:
            logging.warning(f"Kit status has not changed. Current status: {After_Card_Status}")
            
            
        Click_Check_GPR_Card_Details_Button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@variant="primary"]')))
        Click_Check_GPR_Card_Details_Button.click()
        logging.info("Successfully Click Card Detail Button")
        
        # For Closing The open Form 
        Form_Close_cross_button_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Form_Close_cross_button_xpath)))
        Form_Close_cross_button_element.click()
        
        # Check After Card holder Name 
        After_Card_holder_Name_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'issuer-name-wrapper')))
        After_Card_holder_Name = After_Card_holder_Name_element.text
        logging.info(f"After Card Holder Name Check: {After_Card_holder_Name} ")
        
        
        
        assert Before_Card_holder_Name == After_Card_holder_Name
        
        logging.info("Before Card Holder Name After Card Holder Name Both Are Matched!.")  
        time.sleep(2) 
        print("Click Search-78")
        self.Croxx_Search_option()
        time.sleep(2)
        print("Check Issue Card Click-78")
        time.sleep(2)
            
    def Load_Fund_In_Personalized_Issue_Card(self, mobile, amt):
        self.Click_Business_Page()
        time.sleep(2)

        self.Click_Card_Program()
        time.sleep(2)

        self.Click_GPR_Card_Program()
        time.sleep(2)

        Wallet_Name = self.Take_Wallet_Name()
        logging.info(f"Print The Wallet Name: {Wallet_Name}")

        self.Click_Croxx_Button()
        time.sleep(2)

        self.Click_Card_Btn()
        print("2")
        time.sleep(5)
        self.Click_Search_option()
        print("Check_Clear_2")       
        time.sleep(1)
        self.Search_Mobile_In_Yes_Bank(mobile)
        time.sleep(2)

        self.Click_Search_option()
        time.sleep(2)

        Active_Status_Check = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//table//tbody//tr//td[10]'))
        ).text.strip()

        if Active_Status_Check.lower() == 'active':
            logging.info(f"Your Status is {Active_Status_Check}")

            Click_Check_GPR_Card_Details_Button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@variant="primary"]'))
            )
            Click_Check_GPR_Card_Details_Button.click()
            logging.info("Successfully Clicked Card Detail Button")
            time.sleep(2)

            self.Load_Money_Button()
            time.sleep(3)
            
            Wallet_Name_ele = self.driver.find_element(By.XPATH, "//div[text()='asdfasdf']")
            Check_Wallet_Name = Wallet_Name_ele.text.strip()

            logging.info(f"Checking row Wallet Name: {Check_Wallet_Name}")

            if Wallet_Name.lower() == Check_Wallet_Name.lower():
                logging.info(f"Wallet name matched: {Check_Wallet_Name}")

                Before_Load_wallet_Balance_ele = self.driver.find_element(By.XPATH, "//span[@class='wallet-balance']")
                Before_Load_wallet_Balance = Before_Load_wallet_Balance_ele.text.strip()

                self.Load_Money_INput_Box(amt)
                time.sleep(2)
                self.Click_Add_Money_Submit_button()
                time.sleep(2)
                # self.Search_Mobile_In_Yes_Bank(mobile)
                time.sleep(2)
                # self.Click_Search_option()
                time.sleep(2)

                Click_Check_GPR_Card_Details_Button.click()
                
                self.Load_Money_Button()
                time.sleep(3)                 

                After_Load_wallet_Balance_ele = self.driver.find_element(By.XPATH, "//span[@class='wallet-balance']")
                After_Load_wallet_Balance = After_Load_wallet_Balance_ele.text.strip()

                if Before_Load_wallet_Balance != After_Load_wallet_Balance:
                    logging.info(f"Before GPR Wallet Balance: {Before_Load_wallet_Balance}, Successfully Uploaded: {After_Load_wallet_Balance}")
                    WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='close'])[2]"))).click()
                    WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='close'])[1]"))).click()
                
                    time.sleep(2)
                    print("Click Search-1")
                    self.Croxx_Search_option()
                    time.sleep(2)
                    print("Check Issue Card Click-1")
                    time.sleep(2)
                    
                else:
                    logging.error("Wallet balance did not update.")
            else:
                logging.error("Wallet name did not match.")
        else:
            logging.info("Status does not match.")

    
    def test_Issued_Personalized_GPR_Card_Load_Fund_Check_Toast_Method(self, mobile, amt):
        self.Click_Business_Page()
        time.sleep(2)

        self.Click_Card_Program()
        time.sleep(2)

        self.Click_GPR_Card_Program()
        time.sleep(2)

        Wallet_Name = self.Take_Wallet_Name()
        logging.info(f"Print The Wallet Name: {Wallet_Name}")

        self.Click_Croxx_Button()
        time.sleep(2)

        self.Click_Card_Btn()
    
        time.sleep(2)
        self.Search_Mobile_In_Yes_Bank(mobile)
        time.sleep(2)

        self.Click_Search_option()
        time.sleep(2)

        Active_Status_Check = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//table//tbody//tr//td[10]'))
        ).text.strip()

        if Active_Status_Check.lower() == 'active':
            logging.info(f"Your Status is {Active_Status_Check}")

            Click_Check_GPR_Card_Details_Button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@variant="primary"]'))
            )
            Click_Check_GPR_Card_Details_Button.click()
            logging.info("Successfully Clicked Card Detail Button")
            time.sleep(2)

            self.Load_Money_Button()
            time.sleep(3)
            
            Wallet_Name_ele = self.driver.find_element(By.XPATH, "//div[text()='asdfasdf']")
            Check_Wallet_Name = Wallet_Name_ele.text.strip()

            logging.info(f"Checking row Wallet Name: {Check_Wallet_Name}")

            if Wallet_Name.lower() == Check_Wallet_Name.lower():
                logging.info(f"Wallet name matched: {Check_Wallet_Name}")

                self.Load_Money_INput_Box(amt)
                time.sleep(2)
                self.Click_Add_Money_Submit_button()
                time.sleep(2)
                
            else:
                logging.error("Wallet name did not match.")
        else:
            logging.info("Status does not match.")

    def Click_Cross_Buttons(self):
        
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='close'])[2]"))).click()
        time.sleep(1)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='close'])[1]"))).click()
        time.sleep(2)
        print("Click Search")
        self.Croxx_Search_option()
        time.sleep(2)
        print("Check Issue Card Click")
        time.sleep(2)     
    
    
    def Issued_Personalized_GPR_Card_Withdraw_Fund_Check_Toast_Method(self, mobile, amt):
        
        
        self.Search_Mobile_In_Yes_Bank(mobile)
        time.sleep(2)

        self.Click_Search_option()
        time.sleep(2)
        
        Click_Check_GPR_Card_Details_Button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@variant="primary"]'))
            )
        Click_Check_GPR_Card_Details_Button.click()
        logging.info("Successfully Clicked Card Detail Button")
        time.sleep(2)
        
        self.Withdwal_Fund_Button()
        time.sleep(2)
        
        self.Load_Money_INput_Box(amt)
        time.sleep(2)
        
        self.Click_withdrwal_Money_Submit_button()
        time.sleep(1)
            
    
    def Withdraw_Fund_In_Personalized_Issue_Card_For_GPR(self, mobile, amt):
        
        # self.Click_Card_Btn()
        # time.sleep(2)
        
        self.Search_Mobile_In_Yes_Bank(mobile)
        time.sleep(2)

        self.Click_Search_option()
        time.sleep(2)
        
        Click_Check_GPR_Card_Details_Button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@variant="primary"]'))
            )
        Click_Check_GPR_Card_Details_Button.click()
        logging.info("Successfully Clicked Card Detail Button")
        time.sleep(2)
        
        self.Withdwal_Fund_Button()
        time.sleep(2)
        
        Before_Wallet_Name_ele = self.driver.find_element(By.XPATH, "//div[@class='wallet-name word-break']")
        Check_Before_Wallet_Name = Before_Wallet_Name_ele.text.strip()
        
        Before_withdraw_wallet_Balance_ele = self.driver.find_element(By.XPATH, "//span[@class='wallet-balance']")
        Before_withdraw_wallet_Balance = Before_withdraw_wallet_Balance_ele.text.strip()
        
        self.Load_Money_INput_Box(amt)
        time.sleep(2)
        self.Click_withdrwal_Money_Submit_button()
        time.sleep(2)
        
        self.Croxx_Search_option()
        time.sleep(2)
        
        self.Search_Mobile_In_Yes_Bank(mobile)
        time.sleep(2)

        self.Click_Search_option()
        time.sleep(2)
        
        Click_Check_GPR_Card_Details_Button.click()
        time.sleep(2)
        
        self.Withdwal_Fund_Button()
        time.sleep(2)
        
        After_Wallet_Name_ele = self.driver.find_element(By.XPATH, "//div[@class='wallet-name word-break']")
        Check_After_Wallet_Name = After_Wallet_Name_ele.text.strip()
        
        After_withdraw_wallet_Balance_ele = self.driver.find_element(By.XPATH, "//span[@class='wallet-balance']")
        After_withdraw_wallet_Balance = After_withdraw_wallet_Balance_ele.text.strip()
        
        assert Check_Before_Wallet_Name == Check_After_Wallet_Name
        
        if Before_withdraw_wallet_Balance != After_withdraw_wallet_Balance:
            logging.info(f"Successfully Money Unloaded.")
        else:
            logging.info("Money Not Unloaded.")
        
        time.sleep(2)
        
        
    def Do_freeze_card_For_GPR_Personalized_Card(self, mobile):

        # self.Click_Card_Btn()
        # time.sleep(2)
        
        self.Search_Mobile_In_Yes_Bank(mobile)
        print("Hello world")
        time.sleep(2)

        self.Click_Search_option()
        print("Abc")
        time.sleep(2)

        # Get the last 4 digit number of the card
        card_4_digit_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table//tbody//tr//td[7]"))
        ).text
        logging.info(f"Last Card 4 Digit Number: {card_4_digit_number}")

        # Get the card status before freezing
        before_card_status = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table//tbody//tr//td[10]"))
        ).text
        logging.info(f"Before Card Status Is: {before_card_status}")

        # Click to check card details
        check_card_details_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@variant="primary"]'))
        )
        check_card_details_button.click()
        logging.info("Successfully clicked Card Detail Button")
        time.sleep(2)

        # Freeze the card
        self.Click_Freeze_Card_Button()
        time.sleep(2)

        self.Click_Conform_Freeze_Card_Button()

        # Verify the toast message
        expected_toast_message = f"Card ending with {card_4_digit_number} is LOCKED"
        logging.info(f"Expected Toast Message IS: {expected_toast_message}")

 
        current_toast_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='v-toast__text']"))
        ).text
        logging.info(f"Actual Toast Message: {current_toast_message}")

        assert expected_toast_message == current_toast_message, (
            f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        )

        # Get the card status after freezing
        after_card_status = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table//tbody//tr//td[10]"))
        ).text
        logging.info(f"After Card Status Is: {after_card_status}")

        # Check if the card status changed
        assert before_card_status != after_card_status, (
            f"Card status did not change: before {before_card_status}, after {after_card_status}"
        )
        
        if after_card_status == "frozen":
            logging.info(f"Card Status changed successfully, current status is: {after_card_status}")
            
        elif before_card_status == "active":
            logging.warning(f"Card Status did not change, current status is: {before_card_status}")
            
        else:
            logging.error("Something went wrong, card status is not showing correctly.")
        time.sleep(2) 
        self.Croxx_Search_option() 
        time.sleep(2)

    def Do_Unfreeze_card_For_GPR_Personalized_Card(self, mobile):

        # self.Click_Card_Btn()
        # time.sleep(2)
        
        self.Search_Mobile_In_Yes_Bank(mobile) 
        time.sleep(2)

        self.Click_Search_option() 
        time.sleep(2)

        # Get the last 4 digit number of the card
        card_4_digit_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table//tbody//tr//td[7]"))
        ).text
        logging.info(f"Last Card 4 Digit Number: {card_4_digit_number}")

        # Get the card status before freezing
        before_card_status = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table//tbody//tr//td[10]"))
        ).text
        logging.info(f"Before Card Status Is: {before_card_status}")

        # Click to check card details
        check_card_details_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@variant="primary"]'))
        )
        check_card_details_button.click()
        logging.info("Successfully clicked Card Detail Button")
        time.sleep(2)

        # Freeze the card
        self.Click_UnFreeze_Card_Button()
        time.sleep(2)

        self.Click_Conform_UnFreeze_Card_Button()

        # Verify the toast message
        expected_toast_message = f"Card ending with {card_4_digit_number} is ACTIVE"
        logging.info(f"Expected Toast Message IS: {expected_toast_message}")

 
        current_toast_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='v-toast__text']"))
        ).text
        logging.info(f"Actual Toast Message: {current_toast_message}")

        assert expected_toast_message == current_toast_message, (
            f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        )

        # Get the card status after freezing
        after_card_status = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table//tbody//tr//td[10]"))
        ).text
        logging.info(f"After Card Status Is: {after_card_status}")

        # Check if the card status changed
        assert before_card_status != after_card_status, (
            f"Card status did not change: before {before_card_status}, after {after_card_status}"
        )
        
        if after_card_status == "active":
            logging.info(f"Card Status changed successfully, current status is: {after_card_status}")
        
        elif before_card_status == "frozen":
            logging.warning(f"Card Status did not change, current status is: {before_card_status}")
            
        else:
            logging.error("Something went wrong, card status is Uncurrect Or not showing correctly.")

        time.sleep(2)
        self.Croxx_Search_option()
        time.sleep(2)
        
    def Do_Block_Card_For_GPR_Personalized_Card(self, mobile):
        
        # self.Click_Card_Btn()
        # time.sleep(2)
        
        self.Search_Mobile_In_Yes_Bank(mobile) 
        time.sleep(2)

        self.Click_Search_option() 
        time.sleep(2)

        # Get the last 4 digit number of the card
        card_4_digit_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table//tbody//tr//td[7]"))
        ).text
        logging.info(f"Last Card 4 Digit Number: {card_4_digit_number}")

        # Get the card status before freezing
        before_card_status = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table//tbody//tr//td[10]"))
        ).text
        logging.info(f"Before Card Status Is: {before_card_status}")

        # Click to check card details
        check_card_details_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@variant="primary"]'))
        )
        check_card_details_button.click()
        logging.info("Successfully clicked Card Detail Button")
        time.sleep(2)

        # Freeze the card
        self.Click_Block_Card_Button()
        time.sleep(2)

        self.Click_Damage_Input_Buttom()
        time.sleep(2)

        self.Click_Conform_Block_Card_Button()
        time.sleep(2)

        self.Click_Double_Conform_Block_Card_Button_Xpath()
        time.sleep(2)
        
        # Verify the toast message
        expected_toast_message = f"Card ending with {card_4_digit_number} is successfully BLOCKED"
        logging.info(f"Expected Toast Message IS: {expected_toast_message}")

 
        current_toast_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='v-toast__text']"))
        ).text
        logging.info(f"Actual Toast Message: {current_toast_message}")

        assert expected_toast_message == current_toast_message, (
            f"Toast message mismatch: expected {expected_toast_message}, got {current_toast_message}"
        )
        print("any body can dance ")
        time.sleep(10)
        # Get the card status after freezing
        after_card_status = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table//tbody//tr//td[10]"))
        ).text
        logging.info(f"After Card Status Is: {after_card_status}")

        # Check if the card status changed
        assert before_card_status != after_card_status, (
            f"Card status did not change: before {before_card_status}, after {after_card_status}"
        )
        
        if after_card_status == "blocked":
            logging.info(f"Card Status has successfully Block, current status is: {after_card_status}")
        
        elif before_card_status == "active":
            logging.warning(f"Card Status did not change, current status is: {before_card_status}")
            
        else:
            logging.error("Something went wrong, card status is not showing correctly.")
            
        time.sleep(2)
        self.Croxx_Search_option()
        time.sleep(2)