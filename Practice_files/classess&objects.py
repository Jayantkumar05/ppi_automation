# #This is a class..
# class Technologies:
    
#     #thi is a attributes..
#     atr1 = "Artificial Intelligence"
#     atr2 = "Robotics"
#     atr3 = "Internet of Thing"
    
#     #this is a Method..
#     def techno(self):
#         print("Latest Technologies 1: ",self.atr1)
#         print("Latest Technologies 2: ",self.atr2)
#         print("Latest Technologies 3: ",self.atr3)

# #for calling the class and accessing the method...

# Print_Technologies = Technologies()
# Print_Technologies.techno() 




# #This is a class..
# class Technologies: 
    
#     #this is a constructor..
#     def __init__(self,atr1,atr2,atr3):
        
#         self.atr1 = atr1
#         self.atr2 = atr2
#         self.atr3 = atr3
    
#     #this is method..
#     def techno(self):
#         print("Latest Technologies 1: " + self.atr1 +  "\nLatest Technologies 2: " + self.atr2 )
        
#     def techno2(self):
#         print("Latest Technologies 3: " + self.atr3)

# #for calling the class and accessing the method...
# obj = Technologies("Artificial Intelligence","Robotics","Internet of Thing")
# obj.techno()
# obj.techno2()


class Login_page:
    
    def __init__(driver, email,password):
        
        driver.email = email
        driver.password = "password"
        
    def login_function(driver):
        print("Your Email: " + driver.email + "\nYour Password: " + driver.password)

obj = Login_page('Jay123@gmail.com','5005005')
obj.login_function()
