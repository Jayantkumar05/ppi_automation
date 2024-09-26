import csv
import random
import string
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table

class CsvGenerator:

    def generate_random_name(self):
        length = random.randint(2, 25)
        name = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        return name.capitalize()

    def generate_random_mobile(self):
        return f"{random.randint(6000000000, 9999999999)}"

    def generate_random_dob(self):
        start_date = datetime(1950, 1, 1)
        end_date = datetime(2000, 12, 31)
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        return random_date.strftime("%Y-%m-%d")

    def generate_random_email(self):
        return f"{self.generate_random_name().lower()}@example.com"

    def generate_random_bank_name(self):
        banks = ['Deutsche Bank', 'KOTAK MAHNDRA BANK', 'HDFC', 'YESBANK', 'UNION BANK', 'PUNJAB & SIND BANK', 'PUNJAB NATIONAL BANK']
        return random.choice(banks)

    def create_csv_file_for_gc_upload(self, filename='output.csv'):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['LOAD_AMOUNT', 'FULL_NAME', 'MOBILE', 'DOB', 'NAME_ON_CARD', 'EMAIL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for _ in range(20):
                writer.writerow({
                    'LOAD_AMOUNT': '1000', 
                    'FULL_NAME': self.generate_random_name(),
                    'MOBILE': self.generate_random_mobile(),
                    'DOB': self.generate_random_dob(),
                    'NAME_ON_CARD': self.generate_random_bank_name(),
                    'EMAIL': self.generate_random_email(),
                })

    def print_csv_file(self, filename='output.csv'):
        console = Console()
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)   
            rows = list(reader)      
          
            
            table = Table(show_header=True, header_style="bold magenta")
            for header in headers:
                table.add_column(header, style="dim", width=20)

            for row in rows:
                table.add_row(*row)

            console.print(table)

generator = CsvGenerator()
filename = 'GC_BULK_DATA_PRACTICE_FILE.csv'
generator.create_csv_file_for_gc_upload(filename)
generator.print_csv_file(filename)
