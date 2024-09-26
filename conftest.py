import pytest 
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# s = Service('C:\\Users\\user\\Downloads\\chromedriver.exe')

@pytest.fixture(scope='module')

def driver():
    
    driver = webdriver.Chrome( )
    
    # QA Bussiness Portal Page Url
    driver.get("https://ppi-business-portal.qual.card91.in/user/login") 
    
    # Maximizing the window
    driver.maximize_window()
    
    yield driver
    
    driver.quit()