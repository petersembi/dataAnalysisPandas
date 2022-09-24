import pandas as pd
import os
import glob


# use glob to get all excel files in the folder
path = os.getcwd()
excel_files = glob.glob(os.path.join(path,"*.xlsx"))

#loop over the list of excel files
for f in excel_files:
    #read the csv file
    df = pd.read_excel(f)
    # delete unwanted columns
   
    newdf = df.drop(["Unnamed: 0"],axis='columns')
   
    newdf['Date '] = newdf['Date'].dt.strftime('%m/%d/%Y')
   
# shift column 'Date ' to second position
    date_column = newdf.pop('Date ')
  
# insert column using insert(position,column_name,
# first_column) function
    newdf.insert(2, 'Date ', date_column)
    newdf = newdf.drop(["Date"],axis='columns')
    

    sum_row = newdf[["Amount"]].sum()
    df_sum=pd.DataFrame(data=sum_row).T
    df_sum=df_sum.reindex(columns=df.columns)
    df_final=newdf.append(df_sum,ignore_index=True)
    new_f_df = df_final.dropna(how="all", axis=1)

    

    print(new_f_df.tail())
    new_f_df.info()

    new_f_df.to_excel(os.path.join('final_files', f ))
   
#    resources
        # https://www.journaldev.com/33492/pandas-dropna-drop-null-na-values-from-dataframe#:~:text=Pandas%20DataFrame%20dropna()%20function%20is%20used%20to%20remove%20rows,null%20values%20using%20None%2C%20pandas.