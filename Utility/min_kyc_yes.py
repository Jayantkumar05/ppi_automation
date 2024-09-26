from Pages.Random_Method import Random_Methods
import requests
import pytest
import pprint
import json  

class Yes_Min_KYC:
    mobile = ""
    base_url = "https://ppi-api.qual.card91.in/"
    otp = "111111"
    
    # parameterized constructor

    def __init__(self, mob, name):
        self.mobile = mob
        self.name = name
        self.base_url  
        self.random_methods = Random_Methods()

    def register_Customer(self):
        path = "issuance/v1/cardholders/yesbank/register"
        PARAMS = {"mobile": self.mobile}
        URL = url = self.base_url+path
        r = requests.post(url=URL, json=PARAMS)
        print("R Response value =", r.text)
        response_json = json.loads(r.text)
        print("Vivek Response JSON ", response_json)
        print("Vivek Session ID ", response_json["sessionId"])
        return response_json["sessionId"]

    def verify_Customer(self):
        path = "issuance/v1/cardholders/yesbank/verify"
        session_id = self.register_Customer()
        PARAMS = {"mobile": self.mobile,
                  "otp": self.otp, "sessionId": session_id}
        r = requests.post(url=self.base_url+path, json=PARAMS)
        response_json = json.loads(r.text)
        # print(status_code)
        print("Vivek mpin Verify Response JSON", response_json)

    def submit_Aadhaar_MIN_KYC(self):

        self.verify_Customer()

        path = "issuance/v1/cardholders/yesbank/aadhaar"
        URL = self.base_url+path
        print(URL)
        # login_token=CustCardFlag.get_cust_auth_token(self)
        # headers={"Authorization": "Bearer "+lo
        # gin_token}
        # Aadhar_no = Random_Methods.generate_12_Random_AadhaarNumbers(self)
        Aadhar_no = self.random_methods.generate_12_random_aadhaar_numbers() 
        PARAMS = {
            "mobile": self.mobile,
            "name": self.name,
            # Random Aadhar put it 
            "aadhaarNumber": Aadhar_no,
            "dateOfBirth": "1998-05-27",
            "address": "Testing address",
            "pinCode": "560102",
            "gender": "M",
            "profession": "STUDENT",
            "educationQualification": "UNDER_GRADUATE",
            "annualIncome": "INCOME_0_1L",
            "sourceOfFund": "PENSION",
            "purposeOfCardIssuance": "GIFT",
            "selfEmployedProfession": "ARCHITECT"
        }

        # PARAMS = {"mobile": self.mobile,"otp": self.otp,"sessionId": session_id }
        r = requests.post(url=self.base_url+path, json=PARAMS)
        print("Get KYC Status ", r.text)
        response_json = json.loads(r.text)
        status_code = r.status_code
        print("Vivek Response JSON CARD FLAG", response_json)
        return status_code
    
    
    
    

    
    
    










# class NSDL_Min_KYC:
#     mobile = ""
#     # base_url = "https://ppi-api.sb.card91.in/"
#     otp = "111111"

#     # parameterized constructor
#     def __init__(self, mob, name):
#         self.mobile = mob
#         self.name = name
#         self.base_url = ReadConfig.get_api_base_url()
#     def cardHolder_otp(self):
#         path = "issuance/v1/cardholders/kyc/otp"
#         PARAMS = {"mobile": self.mobile}
#         URL = url = self.base_url+path
#         r = requests.post(url=URL, json=PARAMS)
#         print("R Response value =", r.text)
#         response_json = json.loads(r.text)
#         print("Vivek Response JSON ", response_json)
#         print("Vivek Session ID ", response_json["sessionId"])
#         return response_json["sessionId"]

#     def cardHolder_otp_verify(self):
#         path = "issuance/v1/cardholders/kyc/verify"
#         session_id = NSDL_Min_KYC.cardHolder_otp(self)
#         PARAMS = {"mobile": self.mobile,
#                   "otp": self.otp, "sessionId": session_id}
#         r = requests.post(url=self.base_url+path, json=PARAMS)
#         response_json = json.loads(r.text)
#         print("Vivek Complete Response", response_json)
#         print("Vivek Seeion ID for Min KYC", response_json["sessionId"])
#         return response_json["sessionId"]

#     def submit_NSDL_MIN_KYC(self):
#         # get sesssion_id for min_kyc_api recived inresponse of cardholder's OTP Verification
#         session_id = NSDL_Min_KYC.cardHolder_otp_verify(self)
#         path = "issuance/v1/cardholders/nsdl/min-kyc"
#         URL = self.base_url+path
#         # headers={"Authorization": "Bearer "+login_token}
#         pan_no = MathPage.generate_Random_PanNumber(self)
#         # doc_type="MASKED_AADHAAR"
#         # doc_number="last 4 digit of aadhar"
#         PARAMS = {
#             "mobile": self.mobile,
#             "sessionId": session_id,
#             "document":
#             {
#                 "docType": "PAN",
#                 "docValue": pan_no,
#                 "docImage": "https://validS3path.com/panPath",
#                 "country": "IND",
#                 "metaData":
#                 {
#                             "name": "Testing",
#                             "dob": "1998-02-28",
#                             "address": "Testing address",
#                             "pincode": "560103",
#                             "gender": "M"
#                 }
#             }
#         }

#         # PARAMS = {"mobile": self.mobile,"otp": self.otp,"sessionId": session_id }
#         r = requests.post(url=self.base_url+path, json=PARAMS)
#         print("Get KYC Status ", r.text)
#         response_json = json.loads(r.text)
#         status_code = r.status_code
#         print("Vivek Response JSON CARD FLAG", response_json)
#         return status_code


# class FINO_Min_KYC:
#     mobile = ""
#     # base_url = "https://ppi-api.sb.card91.in/"
#     otp = "111111"

#     # parameterized constructor
#     def __init__(self, mob, name):
#         self.mobile = mob
#         self.name = name
#         self.base_url = ReadConfig.get_api_base_url()

#     def mp_admin_login(self):

#         base_url = self.base_url
#         path = "issuance/v1/admins/email"
#         URL = base_url+path
#         PARAMS = {
#             "email": ReadConfig.get_MP_Admin_LoginEmail(),
#             "password": ReadConfig.get_MP_AdminLogin_Password()
#         }
#         # Send the POST request
#         response = requests.post(url=URL, json=PARAMS)
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Extract LOGIN_TOKEN from the response headers
#             login_token = response.headers.get("Login_token")
#             if login_token:
#                 print("LOGIN_TOKEN:", login_token)
#                 return login_token
#             else:
#                 print("No LOGIN_TOKEN found in the response headers.")
#         else:
#             print("Failed to retrieve LOGIN_TOKEN. Status code:",
#                   response.status_code)
            
#     def submit_FINO_MIN_KYC(self):
#         login_token = self.mp_admin_login()
#         path = "issuance/v1/cardholders/fino/register"
#         URL = self.base_url+path
#         print("PATH:",path)
#         headers={"Authorization": "Bearer "+login_token}

#         PARAMS = {

#             "mobile": self.mobile,
#             "otp": self.otp,
#             "sessionId": "DUMMYOTPP",
#             "title": "Ms",
#             "firstName": self.name,
#             "lastName": "",
#             "gender": "M",
#             "dateOfBirth": "1997-01-01",
#             "address":
#                         {
#                             "addressType": "PERMANENT_ADDRESS",
#                             "status": "ACTIVE",
#                             "address1": "1410 6th Main",
#                             "address2": "HSR layout",
#                             "city": "Bangalore",
#                             "countryISOCode": "IN",
#                             "pincode": "560102",
#                             "state": "Karanatka"
#                         },
#             "document":
#             {
#                             "docType": "PAN",
#                             "docValue": "AVMPT5121D"
#                         }

#         }

#         # PARAMS = {"mobile": self.mobile,"otp": self.otp,"sessionId": session_id }
#         r = requests.post(url=self.base_url+path, json=PARAMS,headers=headers)
#         print("Get KYC Status ", r.text)
#         response_json = json.loads(r.text)
#         print("RESPONSE",response_json)
#         status_code = r.status_code
#         print("Vivek Response JSON CARD FLAG", response_json)
#         return status_code


# # Yes_Min_KYC = Yes_Min_KYC(917347261590, "PhysicalCard detached")
# # Yes_Min_KYC.submit_Aadhaar_MIN_KYC()
