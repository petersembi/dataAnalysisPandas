import pandas as pd
import os.path
df = pd.read_excel("stem_statement.xlsx")
modDf = df.drop([df.columns[0],df.columns[1],df.columns[2],df.columns[4],df.columns[6],df.columns[8], df.columns[10], df.columns[12]],axis='columns')
# print(df.to_string())

new_df = modDf.dropna(how="any", subset=['Memo'])
print(new_df.to_string())

speciesdata = new_df ['Memo'].unique()

for i in speciesdata:
    a = new_df [new_df ["Memo"].str.contains(i)]
    a.to_excel(os.path.join('new_files', i+'.xlsx'))
