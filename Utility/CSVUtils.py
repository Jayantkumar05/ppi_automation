import pandas as pd



def getRowCount(file):
    df = pd.read_csv(file)
    return df,len(df)



def getColumnCount(file):
    df = pd.read_csv(file)
    return df.shape[1]

    
def readData(data_frame,rownum, columnno):
    df = data_frame

    if df.isnull().iat[rownum,columnno-1]:
        return ""
    else:
        return df.iat[rownum,columnno-1]


def writeData(data_frame, rownum, columnno, data):
    # Read the CSV file
    df = data_frame
    df.iat[rownum, columnno-1] = data
    
    
    # Ensure the column we're writing to is of type object to handle mixed types
    # df[df.columns[columnno-1]] = df[df.columns[columnno-1]].astype('object')
    
    # Write the data to the specified cell
    
    # df.at[, 'name'] = 'sri devi'
    # Save the updated DataFrame back to the CSV file
