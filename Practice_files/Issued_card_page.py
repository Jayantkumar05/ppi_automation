# import random
# from selenium.webdriver.common.by import By
# import time 
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys


# class Issued_Card_class:
    
#     Click_Card_Btn_Id = "sideLi1"
#     Click_Issue_Card_Form_Xpath = "//button[@class='btn add-btn btn-primary']"
#     Name_Input_Xpath = "(//input[@class='form-control is-valid'])[1]"
#     Name_On_Card_xpath = "(//input[@class='form-control is-valid'])[2]"
#     Mobile_Number_xpath = "(//input[@class='form-control is-valid'])[3]"
#     Select_Card_Program_xpath = "(//div[@role='combobox'])[1]"
#     # Click_Insta_Card_Button_Xpath = "(//label[@class='btn btn-secondary'])[3]"
#     Input_Kit_Number_Xpath = "//input[@name='Kit No.']"
#     Wallet_Xpath = "//input[@aria-label='smart wallets']"
#     Calender_Input_Xpath = "//input[@name='DOB']"
#     Adress_house_number_Xpath = "(//input[@class='form-control is-valid'])[8]"
#     Area_Name_Xpath = "(//input[@class='form-control is-valid'])[9]"
#     Landmark_Xpath = "(//input[@class='form-control is-valid'])[10]"
#     Pincode_Xpath = "(//input[@class='form-control is-valid'])[11]"
#     City_Xpath = "(//input[@class='form-control is-valid'])[12]"
#     State_Xpath = "(//input[@class='form-control is-valid'])[13]"
#     Click_Issued_Card_Button_Xpath = "//button[@type='submit']" 
#     Toast_Message_Xpath = "//p[contains(text(),'Card creation is in progress')]"
    
    
#     # Contructor, Taking web driver. 
#     def __init__(self,driver):
        
#         self.driver = driver
    
#     def Click_Card_Btn(self):
#         Click_Card_Btn_element = self.driver.find_element(By.ID, self.Click_Card_Btn_Id)
#         Click_Card_Btn_element.click()
        
#     def Click_Issue_Card_Form(self):
#         Click_Issue_Card_Form_Xpath_element = self.driver.find_element(By.XPATH, self.Click_Issue_Card_Form_Xpath) 
#         time.sleep(10)
#         Click_Issue_Card_Form_Xpath_element.click()
        
#     def Name_Input(self, name):
#         Name_Input_element = self.driver.find_element(By.XPATH, self.Name_Input_Xpath)
#         Name_Input_element.send_keys(name)
        
#     def Name_On_Card(self,cardname):
#         Name_On_Card_element = self.driver.find_element(By.XPATH, self.Name_On_Card_xpath)
#         Name_On_Card_element.send_keys(cardname)
        
#     def Mobile_Number(self,mobile):
#         Mobile_Number_element = self.driver.find_element(By.XPATH, self.Mobile_Number_xpath)
#         Mobile_Number_element.send_keys(mobile)
    
#     # Generatiing a random mobile numbers...
#     # def generate_random_mobile(self):
#     #     return f"{random.randint(6000000000, 9999999999)}"
        
#     def Select_Card_Program(self,cardprogram):
#         Select_Card_Program_element = self.driver.find_element(By.XPATH, self.Select_Card_Program_xpath)
#         Select_Card_Program_element.send_keys(cardprogram)
   
#     # def Click_Insta_Card_Button(self):
#     #     Click_Insta_Card_Button_element = self.driver.find_element(By.XPATH, self.Click_Insta_Card_Button_Xpath)
#     #     Click_Insta_Card_Button_element.click()
        
#     def Input_Kit_Number(self,Inputkitnumber):
#         select_card_program_dropdown_element = self.driver.find_element(By.XPATH, self.Input_Kit_Number_Xpath)
#         select_card_program_dropdown_element.send_keys(Inputkitnumber)
        
#     def Wallet(self,wallet):
#         Wallet_element = self.driver.find_element(By.XPATH, self.Wallet_Xpath)
#         Wallet_element.send_keys(wallet)
        
#     def Calender_Input(self, calender):
#         Calender_Input_element = self.driver.find_element(By.XPATH, self.Calender_Input_Xpath)
#         Calender_Input_element.send_keys(calender)
    
#     def Adress_house_number(self, housenum):
#         Adress_house_number_element = self.driver.find_element(By.XPATH, self.Adress_house_number_Xpath)
#         Adress_house_number_element.send_keys(housenum)
        
#     def Area_Name(self, area):
#         Area_Name_element = self.driver.find_element(By.XPATH, self.Area_Name_Xpath)
#         Area_Name_element.send_keys(area)
        
#     def Landmark(self, landmark):
#         Landmark_element = self.driver.find_element(By.XPATH, self.Landmark_Xpath)
#         Landmark_element.send_keys(landmark)
        
#     def Pincode(self, pincode):
#         Pincode_element = self.driver.find_element(By.XPATH, self.Pincode_Xpath)
#         Pincode_element.send_keys(pincode)
        
#     def City(self, city):
#         City_element = self.driver.find_element(By.XPATH, self.City_Xpath)
#         City_element.send_keys(city)
        
#     def State(self, state):
#         State_element = self.driver.find_element(By.XPATH, self.State_Xpath)
#         State_element.send_keys(state)

#     def Click_Issued_Card_Button(self):
#         Click_Issued_Card_Button_element = self.driver.find_element(By.XPATH, self.Click_Issued_Card_Button_Xpath)
#         Click_Issued_Card_Button_element.click()
    
#     def Card_Creation_Progress_Toast_Message(self):
#         Toast_Message_element = self.driver.find_element(By.XPATH, self.Toast_Message_Xpath)
#         return Toast_Message_element.text
    
#     # Mwthod to Issued the Gift card..
#     def Issued_card_to_orj(self, name, cardname, mobile, cardprogram, kitnumber, wallet,
#                            calender, housenum, area, landmark, pincode, city, state):
#         self.Click_Card_Btn()
#         time.sleep(2)
#         self.Click_Issue_Card_Form()
#         time.sleep(2)
#         self.Name_Input(name)
#         time.sleep(2)
#         self.Name_On_Card(cardname)
#         time.sleep(2)
#         self.Mobile_Number(mobile) 
#         time.sleep(2)
#         self.Select_Card_Program(cardprogram + Keys.ENTER)
#         time.sleep(2)
#         # self.Click_Insta_Card_Button()
#         # time.sleep(2)
#         self.Input_Kit_Number(kitnumber)
#         time.sleep(2)
#         self.Wallet(wallet)
#         time.sleep(2)
#         self.Calender_Input(calender)
#         # add calender Method here...
#         time.sleep(2)
#         self.Adress_house_number(housenum)
#         time.sleep(2)
#         self.Area_Name(area)
#         time.sleep(2)
#         self.Landmark(landmark)
#         time.sleep(2)
#         self.Pincode(pincode)
#         time.sleep(2)
#         self.City(city)
#         time.sleep(2)
#         self.State(state)
#         time.sleep(2)
#         self.Click_Issued_Card_Button()
#         time.sleep(2)