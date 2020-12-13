import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

year = "2018"
path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "Call_Report_"+year, "FFIEC CDR Call Bulk POR 09302018.txt")
rc_data_path = os.path.join(path, "..", "data", "Call_Report_"+year, "FFIEC CDR Call Schedule RC 09302018.txt")

df_info = pd.read_csv(data_path, sep='\t', low_memory=False)
df_rc = pd.read_csv(rc_data_path, sep='\t', low_memory=False, skiprows=[1])

new_df = pd.merge(df_info, df_rc, how='inner', on='IDRSSD')

new_df = new_df.loc[new_df['Financial Institution State'] == 'UT']
new_df = new_df[['Financial Institution State', 'Financial Institution Name', 'Financial Institution Zip Code',
                 'RCFD2170', 'RCON2170']]

pivot_df_031 = new_df.pivot_table(index='Financial Institution Name', values="RCFD2170").sort_values(by='RCON2170', ascending=False)
pivot_df_0X1 = new_df.pivot_table(index='Financial Institution Name', values="RCON2170").sort_values(by='RCON2170', ascending=False)
print(pivot_df_0X1)
