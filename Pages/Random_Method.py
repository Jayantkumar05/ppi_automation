import random
import string



class Random_Methods:
    
    
    def generate_12_random_aadhaar_numbers(self):
        # Generate a random 12-digit number
        return "".join(str(random.randint(0, 9)) for _ in range(12)) 

    def generate_10_digit_mobile_numbers(self):
        # Generate a random 12-digit number
        return "".join(str(random.randint(0, 9)) for _ in range(12))
    
    @staticmethod
    def generate_random_name():
        length = random.randint(2, 25)
        name = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        return name.capitalize()