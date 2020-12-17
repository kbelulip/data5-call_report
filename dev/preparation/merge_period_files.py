import os
import pandas as pd

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "..", "data")
cr1_path = os.path.join(data_path, "master_cr_file_01-08.txt")
cr2_path = os.path.join(data_path, "master_cr_file_09-13.txt")
cr3_path = os.path.join(data_path, "master_cr_file_14-20.txt")

df1 = pd.read_csv(cr1_path, sep='\t', low_memory=False)
df2 = pd.read_csv(cr2_path, sep='\t', low_memory=False)
df3 = pd.read_csv(cr3_path, sep='\t', low_memory=False)

frames = [df1, df2, df3]

master_df = pd.concat(frames, ignore_index=True, sort=True)

master_df.rename(columns={'FDIC Certificate Number': 'CERT', 'Financial Institution City': 'City',
                          'Financial Institution Filing Type': 'Filing_Type', 'Financial Institution Name': 'Bank',
                          'Financial Institution State': 'State', 'OTS Docket Number': 'OTS',
                          'Primary ABA Routing Number': 'ABA_R_NUM'
                          },
                 inplace=True)

master_df = master_df[['IDRSSD', 'CERT', 'OTS', 'ABA_R_NUM', 'Bank', 'Filing_Type', 'City', 'State', "period", "year",
                       "quarter", 'Return_on_Assets', 'Equity_Ratio', 'Total_Assets', 'Total_Liabilities',
                       'Total_Equity_Capital', 'Leverage_Ratio', 'Total_Capital_Ratio', 'Net_Income',
                       'Total_Interest_Income', 'Total_Interest_Expense', 'Total_Noninterest_Income',
                       'Total_Noninterest_Expense']]


master_data_path = os.path.join(data_path, "master_cr_file.txt")
master_df.to_csv(master_data_path, sep='\t', index=False)


