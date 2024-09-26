import pandas as pd

file_path = r"test_data\practice1.xlsx"
 
My_df = pd.read_excel(file_path) 

total_row = len(My_df.axes[0])
print("Total rows:", total_row)

total_column = len(My_df.axes[1])
print("Total Columns:", total_column)


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

# this is basically used for taking a emity list for storing a data values...
expected_results = []
result_matches = []

# this is iterate over each row using a for loop
for i in range(total_row):
    firstnum = My_df.loc[i, 'firstnum']
    secondnum = My_df.loc[i, 'secondnum']
    operator = My_df.loc[i, 'operator']
    actual_result = My_df.loc[i, 'actualresult']
     
    # this is basically we are using for add a expected_result in the list...
    expected_result = calculate_result(firstnum, secondnum, operator)
    expected_results.append(expected_result)
     
    # this is basically check the expected_result and actual_result both are magth or not...
    result_match = 'PASS' if actual_result == expected_result else 'FAIL'
    result_matches.append(result_match)
    
# this is basicalaly for making a column for showing the values in the excel sheet... 
My_df['expectedresult'] = expected_results
My_df['result_match'] = result_matches
 
print(My_df[['firstnum', 'secondnum', 'operator', 'actualresult', 'expectedresult', 'result_match']])

# for saving updated data in th excel file  
My_df.to_excel(file_path, index=False)
print(f"Updated DataFrame saved to {file_path}")
