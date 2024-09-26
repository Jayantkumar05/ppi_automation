import pandas as pd

def show_top_5_rows(csv_file_path):
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    
    # for reading columns names...
    # columns = df.columns
    # print(columns)
    
    # taking rows how much you want , just write the number
    # df = pd.read_csv(csv_file_path, nrows=9)
    
    # fOR ADDING COLUMNS in table
    # df = pd.read_csv(csv_file_path , header=None, names = ["LOAD_AMOUNT", "FULL_NAME", "MOBILE", "DOB", "NAME_ON_CARD"," EMAIL"])

    # for skiping the rows
    # df = pd.read_csv(csv_file_path , skiprows=3)
    

    # Display the top 5 rows of the CSV file
    # print("Top 5 rows of the CSV file:")
    # print(df.head())
    # print("\n")   
    
    # Display the last 5 rows of the CSV file
    # print("Last 5 rows of the CSV file:")
    # print(df.tail())
    # print("\n")   
    
    print(df)


show_top_5_rows(r'C:\Users\user\Documents\WorkspaceCard91\Selanium_Project\GC_BULK_DATA_PRACTICE_FILE.csv')


# this method is for covert the bank name..
def convert_bank_card(cell):
    if cell == "UNION BANK":
        return 'No Bank'
    return cell

df = pd.read_csv(r"GC_BULK_DATA_PRACTICE_FILE.csv" , converters = {'NAME_ON_CARD': convert_bank_card})
print(df)
    


