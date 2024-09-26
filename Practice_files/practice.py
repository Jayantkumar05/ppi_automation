import pandas as pd
 
file_path = r"test_data\Math_check.xlsx"
 
My_df = pd.read_excel(file_path)
 
total_row = len(My_df.axes[0])
print("Total rows :", total_row)
total_column = len(My_df.axes[1])
print("Total Columns :", total_column)
 
print(My_df.columns)

def calculate_result(firstnum, secondnum, operator):
    if operator == 'ADD':
        return firstnum + secondnum
    elif operator == 'SUBTRACT':
        return firstnum - secondnum
    elif operator == 'MULTIPLY':
        return firstnum * secondnum
    elif operator == 'DIVIDE':
        return firstnum / secondnum
    else:
        return 'Invalid operator'


# So Here I am using apply function for applying all function inside in a apply function. 
# Axis is basically tell the apply function which direction to work rows or coloumn & asix = 'column' is basically work in a rows.
# Lambda row is like a smaller anamoys helper that takes the rows and does something with it..
My_df['expectedresult'] = My_df.apply(lambda row: calculate_result(row['firstnum'], row['secondnum'], row['operator']),axis='columns')


My_df['result_match'] = My_df['actualresult'] == My_df['expectedresult'] 
My_df['result_match'] = My_df['result_match'].replace({True:'PASS' , False:'FAIL'})


print(My_df[['firstnum', 'secondnum', 'operator', 'actualresult', 'expectedresult','result_match', ]])

 
# So i want to save data in a current folder not in a new folder Through This code...
My_df.to_excel(file_path, index=False)
print(f"Updated DataFrame saved to {file_path}")

# =================================================================================