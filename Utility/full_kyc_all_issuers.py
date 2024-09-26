
from tabulate import tabulate
from Utilities.mathLogics import MathPage
import requests
import pytest
import pprint
import json
from Utilities.readConfiguration import ReadConfig
import base64
import hashlib
import hmac
# from Utilities.min_kyc_yes import min_kyc_yes


class YES_Full_KYC:
    mobile = ""
    # base_url = "https://ppi-api.develop.card91.in/"
    otp = "111111"

    # parameterized constructor

    def __init__(self, mob, name):
        self.mobile = mob
        self.name = name
        self.base_url = ReadConfig.get_api_base_url()

    def mp_admin_login(self):

        global login_token
        base_url = self.base_url
        path = "issuance/v1/admins/email"
        URL = base_url+path
        PARAMS = {
            "email": ReadConfig.get_MP_Admin_LoginEmail(),
            "password": ReadConfig.get_MP_AdminLogin_Password()
        }
        # Send the POST request
        response = requests.post(url=URL, json=PARAMS)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract LOGIN_TOKEN from the response headers
            login_token = response.headers.get("Login_token")
            if login_token:
                print("LOGIN_TOKEN:", login_token)
                return login_token
            else:
                print("No LOGIN_TOKEN found in the response headers.")
        else:
            print("Failed to retrieve LOGIN_TOKEN. Status code:",
                  response.status_code)

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

    def get_biometric_key(self):

        self.verify_Customer()

        login_token = self.mp_admin_login()
        path = f"issuance/v1/cardholders/{self.mobile}/kyc/biometricKey"
        URL = self.base_url+path
        # print(URL)
        # login_token=CustCardFlag.get_cust_auth_token(self)
        headers = {"Authorization": "Bearer "+login_token}
        PARAMS = {
            "profession": "STUDENT",
            "educationQualification": "UNDER_GRADUATE",
            "annualIncome": "INCOME_0_1L",
            "sourceOfFund": "PENSION",
            "purposeOfCardIssuance": "GIFT",
            "selfEmployedProfession": "ARCHITECT"
        }

        # PARAMS = {"mobile": self.mobile,"otp": self.otp,"sessionId": session_id }
        r = requests.post(url=URL, json=PARAMS, headers=headers)

        if r.status_code == 200:
            print("KYC biometric key submitted successfully!")
            response_data = r.json()
            if isinstance(response_data, dict):
                # If the response data is a dictionary, convert it to a list of lists for tabulation
                table = [[key, value]
                         for key, value in response_data.items()]
                print(tabulate(table, headers=[
                    "Key", "Value"], tablefmt="grid"))
        else:
            print("Failed to submit KYC biometric key. Status code:",
                  r.status_code)

    def submit_biometric_data(self):
        self.get_biometric_key()
        path = "issuance/v1/cardholders/kyc/biometric"
        URL = self.base_url+path
        # Define the payload
        PARAMS = {
            "mobileNumber": self.mobile,
            "aadhaarNumber": "XXpUOXXXPXXP",
            "isLeftHand": "true",
            "isRightHand": "false",
            "fingerData": "middle",
            "deviceSerialNumber": "XXXXXXXXXXXX",
            "deviceSessionKey": "XXXXXXXXXXXX",
            "deviceTimeStamp": "XXXXXXXXXXXX",
            "deviceType": "MORPHO",
            "deviceVersionNumber": "v2",
            "deviceCertExpiryDate": "XXXXXXXXXXXX",
            "deviceDataXml": "XXXXXXXXXXXX"
        }
        # Define the headers with Bearer token
        headers = {"Authorization": "Bearer "+login_token}
        # Send the POST request
        response = requests.post(url=URL, json=PARAMS, headers=headers)
        # Check the response
        if response.status_code == 200:
            print("Biometric data submitted successfully!")
            response_data = response.json()
            if isinstance(response_data, dict):
                # If the response data is a dictionary, convert it to a list of lists for tabulation
                table = [[key, value] for key, value in response_data.items()]
                print(tabulate(table, headers=[
                      "Key", "Value"], tablefmt="grid"))
                return response.status_code
        else:
            print("Failed to submit biometric data. Status code:",
                  response.status_code)

    def do_Full_KYC(self):

        response_code = self.submit_biometric_data()
        return response_code


class NSDL_Full_KYC:
    mobile = ""
    otp = "111111"

    # parameterized constructor
    def __init__(self, mob):
        self.mobile = mob
        self.base_url = ReadConfig.get_api_base_url()
        # self.base_url = "https://ppi-api.qa.card91.in/"


    def mp_admin_login(self):

        global login_token
        base_url = self.base_url
        path = "issuance/v1/admins/email"
        URL = base_url+path
        print("path",URL)
        PARAMS = {
            "email": ReadConfig.get_MP_Admin_LoginEmail(),
            "password": ReadConfig.get_MP_AdminLogin_Password()
        }
        # Send the POST request
        response = requests.post(url=URL, json=PARAMS)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract LOGIN_TOKEN from the response headers
            login_token = response.headers.get("Login_token")
            if login_token:
                print("LOGIN_TOKEN:", login_token)
                return login_token
            else:
                print("No LOGIN_TOKEN found in the response headers.")
        else:
            print("Failed to retrieve LOGIN_TOKEN. Status code:",
                  response.status_code)

    
    def generate_signature(self,payload, nsdl_secret):
        # Concatenate relevant data from the payload
        data_to_sign = (
                payload.get("channelid", "")
                + payload.get("appid", "")
                + payload.get("partnerid", "")
                + payload.get("token", "")
                + payload.get("cardRefNo", "")
                + payload.get("useruniqid", "")
                + payload.get("reqbytype", "")
                + payload.get("reqby", "")
                + payload.get("verifyontype", "")
                + payload.get("verifyon", "")
                + payload.get("custname", "")
                + payload.get("kycStatus", "")
                + payload.get("response", "")
        )

        # Compute HMAC SHA-512 hash
        hashed_data = hmac.new(nsdl_secret.encode(), data_to_sign.encode(), hashlib.sha512)

        # Encode hash as Base64 to get the signature
        signature = base64.b64encode(hashed_data.digest()).decode()

        return signature
    
    def __get_customerID(self,mobile):
        path = f"issuance/v1/cardholders/{mobile}"
        URL = self.base_url+path
        print("URL",URL)

        login_token = self.mp_admin_login()
        print("login_token",login_token)
        headers = {"Authorization": "Bearer "+login_token}
        print("headers",headers)
        response = requests.get(url=URL, headers=headers)
        if response.status_code == 200:
            response_data = json.loads(response.text)
            print("ResponseData",response_data)
            CustId = response_data.get("cardHolderId")
            print("CustId",CustId)
            return CustId

    def do_NSDL_Full_KYC(self,cust_mobile):
        base_url = self.base_url
        url = f"{base_url}issuance/v1/nsdl/kyc/callback"
        print("URL",url)

        # Get customer id by customer mobile no
        customerID=self.__get_customerID(cust_mobile)

        print("Customer ID",customerID)

        env=ReadConfig.get_env_name()
        print("Enviornment",env)
        # if env=="DEV":
        #     nsdl_secret_key="wbJcjGpvFq8RWL1v9Qpoq93pbgw431PX3qlyt6dy3QUHgRgxSQU89oxrnIVzznUSSUWshz0nKwx29gEija8o2hL3OvRBerekOJpoRzEiMlw3H4lFG4p6o9b04mr4rNbk"
        #     chanel_id="dPSKuBsjasTaMQjPdZjP"
        #     partner_id="kd2SukVWGt"
        if env=="QA":
            nsdl_secret_key="PSajRqitLGEaZCyONXatjzZfUyFIOMLdLcCWSlkOICzMBVRRPAkdsRzjQgrfCtXWjHxsnjcWaZFlUrwkzqmGdKMcIuCUeHksJwEpEunqaqPMIwUQWdmfEkyrBANSqMOk"
            chanel_id="mdULJzpKHidiqACmlOsz"
            partner_id="PvpYwPMN5VO954xsB9UX"
        elif env=="MIGRATION" or env=="SANDBOX" or env=="DEV" or env=="QUALITY":
            nsdl_secret_key="wbJcjGpvFq8RWL1v9Qpoq93pbgw431PX3qlyt6dy3QUHgRgxSQU89oxrnIVzznUSSUWshz0nKwx29gEija8o2hL3OvRBerekOJpoRzEiMlw3H4lFG4p6o9b04mr4rNbk"
            chanel_id="XlRzplNArAzCBarfYswZ"
            partner_id="rfydXORP0t"

        else:
            pytest.fail("No Proper Enviornment")

    
        payload= {
                "appid": "COM.AGENT.NSDL",
                "token": "NA",
                "custname": "Maximillian",
                "response": "KYC success",
                "verifyon": "POBPS7025L",
                "cardRefNo": customerID,
                "channelid": chanel_id,
                "kycStatus": "S",
                "partnerid": partner_id,
                "reqbytype": "CUSTOMER",
                "useruniqid": "1232",
                "verifyontype": "PAN",
                "reqby": "9024245619"

            }

        # Generate signature
        signature = self.generate_signature(payload, nsdl_secret_key)
        

        print("Signd CS",signature)
        payload["signcs"] = signature
        print("Payload",payload)

        # Send the POST request
        response = requests.post(url, json=payload)


        # Check the response
        print("Getting error in response code")
        if response.status_code == 200:
            print("Registration successful first part!")
            response_data = json.loads(response.text)
            # response_data = response.json()
            print("Response data", response_data)
            # Print the response in a tabular form
            table_data = [[key, value] for key, value in response_data.items()]
            print(tabulate(table_data, headers=["Key", "Value"], tablefmt="grid"))
        else:
            print("Registration failed. Status code:", response.status_code)
        
class FINO_Full_KYC:
    mobile = ""
    otp = "111111"

    # parameterized constructor
    def __init__(self, mob, name):
        self.mobile = mob
        self.name = name
        self.base_url = ReadConfig.get_api_base_url()

    def mp_admin_login(self):

        global login_token
        base_url = self.base_url
        path = "issuance/v1/admins/email"
        URL = base_url+path
        PARAMS = {
            "email": ReadConfig.get_MP_Admin_LoginEmail(),
            "password": ReadConfig.get_MP_AdminLogin_Password()
        }
        # Send the POST request
        response = requests.post(url=URL, json=PARAMS)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract LOGIN_TOKEN from the response headers
            login_token = response.headers.get("Login_token")
            if login_token:
                print("LOGIN_TOKEN:", login_token)
                return login_token
            else:
                print("No LOGIN_TOKEN found in the response headers.")
        else:
            print("Failed to retrieve LOGIN_TOKEN. Status code:",
                  response.status_code)
            
    def submit_FINO_Full_KYC(self):
        login_token=self.mp_admin_login()
        path ="issuance/v1/fino/kyc/callback"
        URL = self.base_url+path
        print("PATH:",path)
        headers={"Authorization":"Bearer "+login_token}
        PARAMS = {
            "reason":"Completed",
            "clientId":"15",
            "kycStatus":"Approved",
            "mobileNo":self.mobile,
            "responseCode":"0"
            }
        

        r = requests.post(url=self.base_url+path, json=PARAMS,headers=headers)
        print("Get KYC Status ", r.text)
        response_json = json.loads(r.text)
        status_code = r.status_code
        print("Vivek Response JSON CARD FLAG", response_json)
        return status_code


