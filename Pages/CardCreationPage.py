import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# from Utilities.randomData import RandomData
# from Integration.Admin_Portal.pages.InsatKitCreationPage import InsatKitCreationPage
# import pytest
# from Integration.Admin_Portal.pages.NavigationPage import NavigationPage


class CardCreation:
    def __init__(self, driver):
        self.driver = driver

    # Click Card Section 
    card_button_id = "sideLi1"
    
    
    # Create Card Form Container
    CreateCardFormContainer_Xpath = "//div[@class='modal-content']"
    allBusiness_SearchBar_InputBox_Xpath = (
        "//div[@id='data-table-search-input']/form/input")
    
    # Get CardId Xpath
    cardId_Xpath = '//div[@class="row customer-detail mt-3 pt-2 pb-2"]//span[@class="info"]'
    
    # select Card Program
    select_card_program_drpDwn_Xpath =  '//legend[contains(text(),"Select Card Program")]//following::div[@class="multiselect__tags"]'

    # Enter Card Program
    enter_card_program_Xpath = '//legend[contains(text(),"Select Card Program")]//following::div//input[@class="multiselect__input"]'


    # Cards Menu Navigation Button
    card_Navigation_Btn_Xpath = "(//div[@class='card-header']/ul/li[2]/a)"

    # issue Card Button
    issueCard_Create_Btn_Xpath = "//button[normalize-space()='Issue Card']"

    # Full Name Input Box
    fullName_Card_InputBox_Xpath = "(//input[@class='form-control is-valid'])[1]"

    # Name On Card Input Box
    nameOnCard_Card_InputBox_Xpath = "(//input[@class='form-control is-valid'])[2]"
    
    # Kit Number Input Box
    kit_number_Card_InputBox_Xpath='//input[@name="Kit no."]'

    # Mobile Number Input Box
    mobileNumber_Card_InputBox_Xpath = "(//input[@class='form-control is-valid'])[3]"

    # Email ID Input Box
    emailID_Card_InputBox_Xpath = "(//input[@class='form-control is-valid'])[4]"

    # Digital Card Type Button
    Digital_CardType_Card_Btn_Xpath = "(//div[@class='btn-group-toggle d-inline-block']//label)[1]"

    # Personalized Card Type Button
    Personalized_CardType_Card_Btn_Xpath = "(//div[@class='btn-group-toggle d-inline-block']//label)[2]"

    # Insta Card Type Button
    Insta_CartType_Card_Btn_Xpath = "(//div[@class='btn-group-toggle d-inline-block']//label)[3]"

    # Starting Balance InputBox
    startingBalance_InputBox_Xpath = "(//div[@class='smart-wallets-wrapper']//div//input)[1]"

    # Select Document DropDown
    select_documentType_Card_DrpDwnBtn_Xpath = "(//div[@class='multiselect__select'])[3]"

    # Select PAN Number DropDown
    select_documentType_PanNumber_DrpDwn_Xpath = "//li[@id='null-5']//span[@class='multiselect__option']"

    # Select Aadhaar Number DropDown
    select_documentType_AadhaarNumber_DrpDwn_Xpath = "//li[@id='null-6']//span[@class='multiselect__option']"

    # Card Number Input Box
    # documentValue_Card_InputBox_Xpath = "(//input[@class='form-control is-valid'])[8]"

    # Document Value Input Box
    documentValue_InputBox_Xpath = "(//input[@aria-label='pan number'])"

    # Date of Birth Input
    DOB_Calender_Card_InputBox_Xpath = "//input[@aria-label='DOB']"
    
    # Enter Load Amount Input Field
    enter_load_amount_Xpath = '//input[@name="amount"]'

    # Gender Dropdown
    gender_Card_DrpDwn_Xpath = '//div[@class="multiselect__tags"]//span[contains(text(),"Select Gender")]'

    # Male DropDown
    select_Gender_Male_DrpDwn_Xpath = "(//span[normalize-space()='Male'])[2]"

    # Female DropDown
    select_Gender_Female_DrpDwn_Xpath = "(//span[normalize-space()='Female'])[2]"

    # Transgender DropDown
    select_Gender_Transgender_DrpDwn_Xpath = "(//span[normalize-space()='Transgender'])[2]"

    # House Number Input Box
    houseNo_Card_InputBox_Xpath = "//input[@name='addressLine1']"

    # Area Input Box
    area_Card_InputBox_Xpath = "//input[@name='addressLine2']"

    # Landmark Input Box
    landMark_Card_InputBox_Xpath = "//input[@name='landmark']"

    # Pincode Input Box
    pincode_Card_InputBox_Xpath = "//input[@name='pinCode']"

    # City Input Box
    City_Card_InputBox_Xpath = "//input[@name='city']"

    # State Input Box
    state_Card_InputBox_Xpath = "//input[@name='state']"

    # Issue Card Submit Button
    issueCard_SubmitBtn_Xpath = "(//div//button[contains(text(),'Issue Card')])[2]"

    # Send Card Without KYC
    sendCardWithoutKyc_Checkbox_Xpath = "//div[@class='custom-control custom-checkbox']//input"

    cardList_SearchBox_Xpath = "//input[@class='search-input py-3 pl-3 pr-5 border-radius-10 form-control']"

    # KYC Status Check of Created Card
    KycStatus_CreatedCard_StatusCheck_Xpath = "(//td[@class='vuetable-slot center aligned']//div//span)[1]"
    # Card Status Check of Created Card
    CardStatus_CreatedCard_StatusCheck_Xpath = "(//td[@class='first-letter-cap d-table-cell']//span)[1]"

    # Kit Number Input Box
    kitNo_Card_InputBox_Xpath = "//input[@name='Kit no.']"

    # Card Id Text
    cardId_Card_Text_Xpath = "//span[@class='sub-txt m-0 ml-1']//span"

    AllBusiness_ModuleNavBtn_Xpath = "//li[@data-flag='organization']/a"
    allBusiness_firstRowOrgName_PageBtn_Xpath = (
        "//td[@class='vuetable-slot text-center']//div//button")

    # Close Button
    business_creation_form_close_button_class = "close"

    # PrimaryOrg Creation Form Enter Value In Input Field Text Validation Check (added by Jay)
    cardCreation_FullName_field_validation_text_Xpath = '//input[@aria-label="full name"]//following-sibling::span'
    CardCreation_Card_on_name_field_validation_text_Xpath = '//input[@aria-label="name on card"]//following-sibling::span'
    CardCreation_MobileNum_Validation_Text_Xpath = '//input[@aria-label="mobile number"]//following-sibling::span'
    CardCreation_delivery_Address1_Validation_Text_Xpath = '//input[@aria-label="address line 1"]//following-sibling::span'
    CardCreation_delivery_Address2_Validation_Text_Xpath = '//input[@aria-label="address line 2"]//following-sibling::span'
    CardCreation_delivery_pincode_Validation_Text_Xpath = '//input[@aria-label="pincode"]//following-sibling::span'
    CardCreation_delivery_city_Validation_Text_Xpath = '//input[@aria-label="city"]//following-sibling::span'
    CardCreation_delivery_state_Validation_Text_Xpath = '//input[@aria-label="state"]//following-sibling::span'
    CardCreation_DOB_Validation_Text_Xpath = '//fieldset[@class="form-group"]//input[@aria-label="DOB"]/ancestor::div[@class="d-flex align-items-center justify-content-between"]/following-sibling::span[@class="errorText visible"]'
    CardCreation_documentValue_Validation_Text_Xpath = '//fieldset[@class="form-group"]//input[@aria-label="pan number"]/ancestor::div[@class="d-flex align-items-center justify-content-between"]/following-sibling::span[@class="errorText visible"]'
    CardCreation_gender_Validation_Text_Xpath = "//span[normalize-space()='Select your Gender']"

    # Toast Messages Elements
    business_ToastMsg_by_className = "//div[@class='v-toast v-toast--top']//div//p"

    # Navigate to card creation page

    # def navigate_to_Card_Creation_Page(self, primaryOrgName):
    #     # Click The Card Section
    #     cardSection = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, self.card_button_id)))
    #     time.sleep(2)
    #     cardSection.click()
       
        
        # AllBusinessModuleBtn = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, self.AllBusiness_ModuleNavBtn_Xpath)))
        # AllBusinessModuleBtn.click()
        # time.sleep(2)

        # allBusiness_SearchBar_InputBox = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, self.allBusiness_SearchBar_InputBox_Xpath)))
        # allBusiness_SearchBar_InputBox.send_keys(primaryOrgName + Keys.ENTER)
        # time.sleep(3)

        # firstRowOrgBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
        #     (By.XPATH, self.allBusiness_firstRowOrgName_PageBtn_Xpath)))
        # firstRowOrgBtn.click()
        # time.sleep(2)

        
        # # Navigate to Card Menu
        # card_menu_element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, self.card_Navigation_Btn_Xpath)))
        # card_menu_element.click()
        # time.sleep(2)
    
    def click_Cards_section(self):
        cardSection = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.card_button_id)))
        time.sleep(2)
        cardSection.click()

    def click_IssueCardBtn(self):
        issueCardBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.issueCard_Create_Btn_Xpath)))
        time.sleep(2)
        issueCardBtn.click()

    def enter_FullName(self, full_name):
        cardFullName = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.fullName_Card_InputBox_Xpath)))
        time.sleep(2)
        if full_name == "":
            pass
        else:
            cardFullName.send_keys(full_name)

    def enter_NameOnCard(self, NameOnCard):
        cardNameOnCard = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.nameOnCard_Card_InputBox_Xpath)))
        time.sleep(2)
        if NameOnCard == "":
            pass
        else:
            cardNameOnCard.send_keys(NameOnCard)

    def enter_MobileNumber(self, MobileNumber):
        cardMobileNumber = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.mobileNumber_Card_InputBox_Xpath)))
        time.sleep(2)
        cardMobileNumber.send_keys(MobileNumber)

    def enter_EmailID(self, Email):
        cardEmailID = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.emailID_Card_InputBox_Xpath)))
        time.sleep(2)
        cardEmailID.send_keys(Email)

    def select_card_type(self, card_type):
        if card_type == "Personalized":
            selectPersonalizedCardBtn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.Personalized_CardType_Card_Btn_Xpath)))
            selectPersonalizedCardBtn.click()
            time.sleep(2)

        elif card_type == "Insta Card":
            selectInstaCardBtn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.Insta_CartType_Card_Btn_Xpath)))
            time.sleep(2)
            selectInstaCardBtn.click()
        else:
            pass
        
    def select_card_program(self,cardProgram):
            # click on the dropdown to enter card program
            select_card_program_drpDwn=f'//div[@class="multiselect__tags"]//span[contains(text(),"{cardProgram}")]'
            print("Xpath",select_card_program_drpDwn)
            select_card_program_ele = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,select_card_program_drpDwn)))
            select_card_program_ele.click()
            time.sleep(1)
            # Enter the card program
            enter_card_program_ele = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.enter_card_program_Xpath)))
            enter_card_program_ele.send_keys(cardProgram)
            enter_card_program_ele.send_keys(Keys.ENTER)
            time.sleep(2)
            
    def select_card_program_for_GC_Cards(self,cardProgram):
        select_card_program_ele = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,self.select_card_program_drpDwn_Xpath)))
        select_card_program_ele.click()
        time.sleep(1)
        # Enter the card program
        enter_card_program_ele = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.enter_card_program_Xpath)))
        enter_card_program_ele.send_keys(cardProgram)
        enter_card_program_ele.send_keys(Keys.ENTER)
        time.sleep(2)
        

    def enter_Starting_WalletBalance(self, staring_balance):
        wallet_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.startingBalance_InputBox_Xpath)))
        # Scroll the page up to wallet field
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", wallet_field)
        time.sleep(2)
        firstWalletBalanceField = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.startingBalance_InputBox_Xpath)))
        time.sleep(2)
        firstWalletBalanceField.send_keys(staring_balance)

    def select_DocumentType_And_Provide_DocumentValue(self, documentType, documentValue):
        documentTypeDropDownBtn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.select_documentType_Card_DrpDwnBtn_Xpath)))

        documentTypeDropDownBtn.click()
        time.sleep(3)

        if documentType == "Pan Number":
            docTypePanNumber = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, self.select_documentType_PanNumber_DrpDwn_Xpath)))
            docTypePanNumber.click()

        elif documentType == "Aadhaar Number":
            docTypeAadhaarNumber = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, self.select_documentType_AadhaarNumber_DrpDwn_Xpath)))
            docTypeAadhaarNumber.click()
        else:
            raise Exception("Please Provide a valid document type and document value",
                            f"Actual Document Type is:{documentType} and Actual Document Value is:{documentValue}")

        documentValueField = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.documentValue_InputBox_Xpath)))
        documentValueField.clear()
        documentValueField.send_keys(documentValue)

    def enter_DOB_Calender(self, date):
        CalenderBtn_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.DOB_Calender_Card_InputBox_Xpath)))
        # CalenderBtn_element.click()
        # time.sleep(2)
        # self.driver.execute_script(
        #     "arguments[0].readOnly=false", CalenderBtn_element)
        # time.sleep(2)
        if CalenderBtn_element == "":
            pass
        else:
            CalenderBtn_element.send_keys(date)

    def SelectGender(self, gender):
        try:        
            genderDrpDown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.gender_Card_DrpDwn_Xpath)))
            WebDriverWait(self.driver,10).until(EC.visibility_of(genderDrpDown))
            # Scroll the element into view using JavaScript
            self.driver.execute_script("arguments[0].scrollIntoView(true);", genderDrpDown)

            # self.driver.execute_script(
            # "arguments[0].scrollIntoView();", genderDrpDown)
            time.sleep(5)
            genderDrpDown=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.gender_Card_DrpDwn_Xpath)))
            # self.driver.execute_script("arguments[0].click();", genderDrpDown)
            genderDrpDown.click()
            time.sleep(2)
        except Exception as e:
            print(f'Error Occurred while selecting Gender: {str(e)}')
        if gender == "":
            pass
        elif gender == "Male":
            maleDrpDown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.select_Gender_Male_DrpDwn_Xpath)))
            time.sleep(2)
            maleDrpDown.click()
        elif gender == "Female":
            femaleDrpDown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.select_Gender_Female_DrpDwn_Xpath)))
            time.sleep(2)
            femaleDrpDown.click()
        elif gender == "Transgender":
            transgenderDrpDown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.select_Gender_Transgender_DrpDwn_Xpath)))
            time.sleep(2)
            transgenderDrpDown.click()
        else:
            raise Exception(
                'Please provide valid Gender:"Male, Female, Transgender"',
                f'Actual Value is:{gender}')

    def enter_HouseNo(self, HouseNo):
        HouseNumber_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.houseNo_Card_InputBox_Xpath)))
        time.sleep(2)
        HouseNumber_element.send_keys(HouseNo)

    def enter_Area(self, area):
        areaElement = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.area_Card_InputBox_Xpath)))
        time.sleep(2)
        areaElement.send_keys(area)

    def enter_LandMark(self, landmark):
        landmark_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.landMark_Card_InputBox_Xpath)))
        time.sleep(2)
        landmark_element.send_keys(landmark)

    def enter_PinCode(self, pincode):
        pincode_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pincode_Card_InputBox_Xpath)))
        time.sleep(2)
        pincode_element.send_keys(pincode)

    def enter_City(self, city):
        city_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.City_Card_InputBox_Xpath)))
        time.sleep(2)
        city_element.send_keys(city)
        
    def enter_loadAmount(self,loadAmount):
        load_amount = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.enter_load_amount_Xpath)))
        load_amount.send_keys(loadAmount)

    def enter_State(self, state):
        state_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.state_Card_InputBox_Xpath)))
        time.sleep(2)
        state_element.send_keys(state)
        
    def enter_kit_number(self,kitnumber):
        kit_number_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.kit_number_Card_InputBox_Xpath)))
        kit_number_element.send_keys(kitnumber)

    def click_IssueCard_Submit_Btn(self):
        issueCardBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.issueCard_SubmitBtn_Xpath)))
        issueCardBtn.click()

    def click_close_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CLASS_NAME, self.business_creation_form_close_button_class))).click()

    def get_field_validation_msg_client(self, field_name):
        ErrorMsg_element = None
 
        if field_name == "full_name":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.cardCreation_FullName_field_validation_text_Xpath)))

        elif field_name == "name_on_card":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CardCreation_Card_on_name_field_validation_text_Xpath)))

        elif field_name == "mobile_number":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CardCreation_MobileNum_Validation_Text_Xpath)))

        elif field_name == "document_value":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CardCreation_documentValue_Validation_Text_Xpath)))

        elif field_name == "DOB":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CardCreation_DOB_Validation_Text_Xpath)))

        elif field_name == "Gender":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CardCreation_gender_Validation_Text_Xpath)))

        elif field_name == "house_no":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CardCreation_delivery_Address1_Validation_Text_Xpath)))

        elif field_name == "area":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CardCreation_delivery_Address2_Validation_Text_Xpath)))

        elif field_name == "pincode":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CardCreation_delivery_pincode_Validation_Text_Xpath)))

        elif field_name == "city":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CardCreation_delivery_city_Validation_Text_Xpath)))

        elif field_name == "state":
            ErrorMsg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CardCreation_delivery_state_Validation_Text_Xpath)))
        else:
            pass
        # message = ErrorMsg_element.text
        # return message
        if ErrorMsg_element:
            message = ErrorMsg_element.text
        else:
            message = ""  # Handle the case where ErrorMsg_element is not found
        
        return message

    # def get_field_validation_msg_server(self):
    #     try:
    #         toast_ErrorMsg_element = WebDriverWait(self.driver, 20).until(
    #             EC.presence_of_element_located((By.CLASS_NAME, self.business_ToastMsg_by_className)))
    #         toast_message = toast_ErrorMsg_element.text
    #         print("Jay Toast Error mssg:", toast_message)
    #         return toast_message
    #     except Exception as e:
    #         print("Error while getting toast message:", e)
    #         return None
    
    # def get_toast_message(self):
    #     toast_message = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.business_ToastMsg_by_className)))
    #     print("TOAST MESSAGE",toast_message)
    #     return toast_message
    
    # def get_cardId(self):
    #     cardId_element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.cardId_Xpath)))
    #     print("cardId",cardId_element)
    #     return cardId_element

    
    # def gpr_card_creation_sanity(self, primaryOrgName, issuerName, cardType, phone_number,card_program):
    #     # Navigate to Cards tab
    #     self.navigate_to_Card_Creation_Page(primaryOrgName)
    #     time.sleep(2)
        
    #     # Click on Issue card
    #     self.click_IssueCardBtn()
    #     time.sleep(2)
        
    #     # Prepare card data
    #     fullName = RandomData.generate_8_Random_Letters()
    #     nameOnCard = RandomData.generate_8_Random_Letters()
    #     pincode = RandomData.generate_Random_PinCode()
        
    #     # Common steps
    #     # Enter FullName
    #     self.enter_FullName(f"{cardType}{fullName}")
    #     time.sleep(2)
    #     # Enter Name on Card
    #     self.enter_NameOnCard(f"{cardType}{nameOnCard}")
    #     time.sleep(2)
    #     # Enter Mobile Number
    #     self.enter_MobileNumber(phone_number)
    #     time.sleep(2)
    #     # Select CardType
    #     self.select_card_type(cardType)
    #     time.sleep(2)
        
    #     # Issuer-specific steps
    #     if issuerName in ["YES", "NSDL"]:
    #         self.handle_issuer_yes_nsdl(cardType, pincode)
    #     elif issuerName == "FINO":
    #         self.handle_issuer_fino(cardType, pincode)
        
    #     # Click on Submit Button
    #     self.click_IssueCard_Submit_Btn()
    #     time.sleep(2)
        
    #     # Get Toast message
    #     toast_message = self.get_toast_message().text
    #     if toast_message == "Card creation is in progress":
    #         cardId,cardHolderName= self.verify_gpr_card_creation(cardType,primaryOrgName,phone_number,card_program)
    #         return cardId, cardHolderName
    #     else:
    #         pytest.fail("Card is not created. Something went wrong")

    # def handle_issuer_yes_nsdl(self, cardType, pincode):
    #     if cardType == "Personalized":
    #         self.enter_address_details(pincode)
    #     elif cardType in ["Digital Card", "Insta Card"]:
    #         pass

    # def handle_issuer_fino(self, cardType, pincode):
    #     if cardType == "Personalized":
    #         self.enter_address_details(pincode)
    #         self.enter_DOB_Calender("1984-07-28")
    #         self.SelectGender("Female")
    #     elif cardType in ["Digital Card", "Insta Card"]:
    #         self.enter_DOB_Calender("1984-07-28")
    #         self.SelectGender("Male")

    # def enter_address_details(self, pincode):
    #     self.enter_HouseNo("Address 1")
    #     time.sleep(2)
    #     self.enter_Area("Address 2")
    #     time.sleep(2)
    #     self.enter_LandMark("Test Landmark")
    #     time.sleep(2)
    #     self.enter_PinCode(pincode)
    #     time.sleep(2)
    #     self.enter_City("Bangalore")
    #     time.sleep(2)
    #     self.enter_State("Karnataka")
    #     time.sleep(2)

                
          
    # def verify_gpr_card_creation(self,cardType,business_name,mobile_number,card_program):
    #     print("In Verification of card creation method...")
    #     # Navigate to specific GPR Card under given business
    #     navigation_page = NavigationPage(self.driver)

    #     response,card_status,cardHolderName,kyc_status,last_4_digit = navigation_page.navigate_to_CardListing_Page_to_verify_card_creation(
    #         business_name, mobile_number, card_program)
    #     print("Card Status:",card_status)
    #     print("Card Holder Name:",cardHolderName)
    #     print("KYC Status:",kyc_status)
    #     print("Response:",response)
    #     print("Card Type:",cardType)
    #     print("Last 4 Digits:",last_4_digit)
    #     if cardType=="Personalized" or cardType=="Digital Card":
    #         if card_status=="inactive" and kyc_status=="pending":
    #             assert True
    #         else:
    #             print("Card Status and KYC Status does not match as expected")
    #             pytest.fail("Card Status and KYC Status does not match as expected")
    #     elif cardType=="Insta Card":
    #         if card_status=="pending" and kyc_status=="pending":
    #             assert True
    #         else:
    #             print("Card Status and KYC Status does not match as expected")
    #             pytest.fail("Card Status and KYC Status does not match as expected")
                
    #     else:
    #         pytest.fail("Valid Crad Type is not passed ")
        
    #     if response == "No Card exists" or response == "Card not found":

    #         print("No Card Exist with given mobile and CP")
    #         pytest.fail("No Card Exist with given mobile and CP")
    #     time.sleep(2)
        
    #     # Get Card ID from Card Detail Page
        
    #     # Click on arrow to get the card ID
    #     response=navigation_page.navigate_to_CardDetailPage_of_GPR_Card(business_name,mobile_number,card_program)
        
    #     if response == "No Card exists" or response == "Card not found":

    #         print("No Card Exist with given mobile and CP")
    #         pytest.fail("No Card Exist with given mobile and CP")        
    #     else:
    #         # Get Card Id from the Card Detail View Page
    #         cardId = self.get_cardId().text
    #         time.sleep(1)
    #         # Close the card detail view page
    #         self.click_close_button()
    #         time.sleep(1)
    #         return cardId,cardHolderName
        
    # # Physical and Digital GC Cards
    # def physical_and_digital_GC_card_creation_sanity(self,primaryOrgName,cardType,phone_number,card_program,issuerNetworkName,load_amount):
    #     # Navigate to Cards tab
    #     self.navigate_to_Card_Creation_Page(primaryOrgName)
    #     time.sleep(2)
        
    #     # Click on Issue card Button
    #     self.click_IssueCardBtn()
    #     time.sleep(2)
        
    #     # Prepare card data
    #     fullName = RandomData.generate_8_Random_Letters()
    #     nameOnCard = RandomData.generate_8_Random_Letters()
    #     pincode = RandomData.generate_Random_PinCode()
        
    #     # Common steps
    #     # Enter FullName
    #     self.enter_FullName(f"{cardType}{fullName}")
    #     # Enter Name on Card
    #     self.enter_NameOnCard(f"{cardType}{nameOnCard}")
    #     # Enter Mobile Number
    #     self.enter_MobileNumber(phone_number)
    #     # Select CardType
    #     self.select_card_type(cardType)
    #     # select Card Program
    #     self.select_card_program_for_GC_Cards(card_program)
    #     if issuerNetworkName!="YES-GIFTCARD":
    #         # Enter Date of Birth
    #         self.enter_DOB_Calender("1984-07-28")
    #     else:
    #         pass
    #     # Enter Load Amount
    #     self.enter_loadAmount(load_amount)
        
    #     # if Card Type is Personalized then enter the Address Detail
    #     if cardType=="Personalized":
    #         pincode = RandomData.generate_Random_PinCode()
    #         self.enter_address_details(pincode)
        
    #     # Click on Issue card Submit button
    #     self.click_IssueCard_Submit_Btn()
    #     time.sleep(2)
        
    #     # Get Toast Message
    #     toast_message = self.get_toast_message().text
    #     if toast_message == "Card creation is in progress":
    #         cardId,cardHolderName,last_4_digit= self.verify_GC_card_creation(primaryOrgName,phone_number,card_program,issuerNetworkName)
    #         return toast_message,cardId, cardHolderName,last_4_digit
    #     elif toast_message == "Total amount to be loaded into gift card should be in range of 100 and 10000":
    #         time.sleep(4)
    #         # Close the card details view page
    #         self.click_close_button()
    #         return toast_message,None, None,None
    #     else:
    #         pytest.fail("Card is not created. Something went wrong")   
            
    # def insta_GC_card_creation_sanity(self,primaryOrgName,phone_number,card_program,issuerNetworkName,load_amount):
    #     print("In insta GC card Creation sanity method")
    #     # Creating insta kit page obj to get kit number
    #     instaKitpage_obj=InsatKitCreationPage(self.driver)
    #     # Get insta Kit Number
    #     kit_number = instaKitpage_obj.fetch_InstaKit_BasedOnOrgAndCardProgram(primaryOrgName,card_program)
    #     if(kit_number=="No Available KIT" or kit_number=="No Insta Kit requested with given Card Program" ):

    #         pytest.fail("No Available KIT")
        
    #     # Navigate to Cards tab
    #     self.navigate_to_Card_Creation_Page(primaryOrgName)
    #     time.sleep(2)
        
    #     # Click on Issue card Button
    #     self.click_IssueCardBtn()
    #     time.sleep(2)
        
    #     # Prepare card data
    #     fullName = RandomData.generate_8_Random_Letters()
    #     nameOnCard = RandomData.generate_8_Random_Letters()
    #     pincode = RandomData.generate_Random_PinCode()
        
    #     # Common steps
    #     # Enter FullName
    #     self.enter_FullName(f"Insta{fullName}")
    #     # Enter Name on Card
    #     self.enter_NameOnCard(f"Insta{nameOnCard}")
    #     # Enter Mobile Number
    #     self.enter_MobileNumber(phone_number)
    #     # Select CardType
    #     self.select_card_type("Insta Card")
    #     # Enter the kitnumber
    #     self.enter_kit_number(kit_number)
    #     time.sleep(5)
    #     # select Card Program
    #     self.select_card_program_for_GC_Cards(card_program)
    #     if issuerNetworkName!="YES-GIFTCARD":
    #         # Enter Date of Birth
    #         self.enter_DOB_Calender("1984-07-28")
    #     else:
    #         pass
    #     # Enter Load Amount
    #     self.enter_loadAmount(load_amount)           
        
    #      # Click on Issue card Submit button
    #     self.click_IssueCard_Submit_Btn()
    #     time.sleep(2)
        
    #     # Get Toast Message
    #     toast_message = self.get_toast_message().text
    #     if toast_message == "Card creation is in progress":
    #         cardId,cardHolderName,last_4_digit= self.verify_GC_card_creation(primaryOrgName,phone_number,card_program,issuerNetworkName)
    #         return toast_message,cardId, cardHolderName,last_4_digit
    #     elif toast_message == "Total amount to be loaded into gift card should be in range of 100 and 10000":
    #         time.sleep(4)
    #         # Close the card details view page
    #         self.click_close_button()
    #         return toast_message,None, None,None
    #     else:
    #         pytest.fail("Card is not created. Something went wrong")    
    
    # def verify_GC_card_creation(self,business_name,mobile_number,card_program,issuerNetworkName):
    #     print("In Verification of card creation method...")
    #     # Navigate to specific GPR Card under given business
    #     navigation_page = NavigationPage(self.driver)

    #     response,card_status,cardHolderName,kyc_status,last_4_digit = navigation_page.navigate_to_CardListing_Page_to_verify_card_creation(
    #         business_name, mobile_number, card_program)
    #     print("Card Status:",card_status)
    #     print("Card Holder Name:",cardHolderName)
    #     print("KYC Status:",kyc_status)
    #     print("Response:",response)
    #     print("Last 4 Digits:",last_4_digit)
    #     if issuerNetworkName=="Fino - Gift Card":
            
    #         if card_status=="inactive" and kyc_status=="NA":
    #             assert True
    #         else:
    #             print("Card Status and KYC Status does not match as expected")
    #             pytest.fail("Card Status and KYC Status does not match as expected")
            
    #         if response == "No Card exists" or response == "Card not found":

    #             print("No Card Exist with given mobile and CP")
    #             pytest.fail("No Card Exist with given mobile and CP")
    #         time.sleep(2)
    #     elif issuerNetworkName == "NSDL Bank - Gift Card" or issuerNetworkName == "YES-GIFTCARD":
    #         if card_status == "active" and kyc_status=="NA":
    #             assert True
    #         else:
    #             print("Card Status and KYC Status does not match as expected")
    #             pytest.fail("Card Status and KYC Status does not match as expected")
            
    #         if response == "No Card exists" or response == "Card not found":

    #             print("No Card Exist with given mobile and CP")
    #             pytest.fail("No Card Exist with given mobile and CP")
    #     elif issuerNetworkName=="NSDL Bank -  Static PIN Gift Card":
    #         if card_status == "pending" and kyc_status=="NA":
    #             assert True
    #         else:
    #             print("Card Status and KYC Status does not match as expected")
    #             pytest.fail("Card Status and KYC Status does not match as expected")
            
    #         if response == "No Card exists" or response == "Card not found":

    #             print("No Card Exist with given mobile and CP")
    #             pytest.fail("No Card Exist with given mobile and CP")
            
    #     else:
    #         pytest.fail(f"Please pass the valid Issuer Network Name,actual issuer network is {issuerNetworkName} ")
        
    #     # Get Card ID from Card Detail Page
        
    #     # Click on arrow to get the card ID
    #     response=navigation_page.navigate_to_CardDetailPage_of_GPR_Card(business_name,mobile_number,card_program)
        
    #     if response == "No Card exists" or response == "Card not found":

    #         print("No Card Exist with given mobile and CP")
    #         pytest.fail("No Card Exist with given mobile and CP")        
    #     else:
    #         # Get Card Id from the Card Detail View Page
    #         cardId = self.get_cardId().text
    #         time.sleep(1)
    #         # Close the card detail view page
    #         self.click_close_button()
    #         time.sleep(1)
    #         return cardId,cardHolderName,last_4_digit        
        
        
            
        