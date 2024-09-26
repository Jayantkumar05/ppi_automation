# import csv

# with open('profiles1.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     field = ["name", "age", "country"]

    
#     writer.writerow(field)
#     writer.writerow(["Oladele Damilola", "40", "Nigeria"])
#     writer.writerow(["Alina Hricko", "23", "Ukraine"])
#     writer.writerow(["Isabel Walter", "50", "United Kingdom"])

    
# import module 
import random as r 
 
ph_no = [] 

# the first number should be in the range of 6 to 9 
ph_no.append(r.randint(6, 9)) 

# the for loop is used to append the other 9 numbers. 
# the other 9 numbers can be in the range of 0 to 9. 
for i in range(1, 10): 
    ph_no.append(r.randint(0, 9))  

# printing the number 
for i in ph_no: 
    print(i, end="") 

   