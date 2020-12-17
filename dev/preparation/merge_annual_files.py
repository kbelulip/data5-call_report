import os
import pandas as pd
import glob

year = "2019"
path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "..", "data")
target_data_path = os.path.join(data_path, "Call_Report_"+year)
result_data_path = os.path.join(target_data_path, "Complete_Annual_Call_Report.txt")

columns_to_drop = ['Reporting Period End Date', 'FDIC Certificate Number', 'OCC Charter Number', 'OTS Docket Number',
                   'Primary ABA Routing Number', 'Financial Institution Name', 'Financial Institution Address',
                   'Financial Institution City', 'Financial Institution State', 'Financial Institution Zip Code',
                   'Financial Institution Filing Type', 'Last Date/Time Submission Updated On']

files = glob.glob(os.path.join(target_data_path, "*"))

file1_path = os.path.join(target_data_path, files[0])
file2_path = os.path.join(target_data_path, files[1])

df1 = pd.read_csv(file1_path, sep='\t', low_memory=False)
df2 = pd.read_csv(file2_path, sep='\t', low_memory=False)

df2.drop(columns_to_drop, axis=1, inplace=True)

result = df1.merge(df2, left_on='IDRSSD', right_on='IDRSSD')

#names = result.columns.str.split(',').tolist()
result.drop(list(result.filter(regex='Unnamed')), axis=1, inplace=True)

result.to_csv(result_data_path, sep='\t', index=False)
