import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file_15-20.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)

new_df = df.loc[(df['year'] == 2018) & (df['quarter'] == 3)]

new_df = new_df.loc[new_df['Financial Institution State'] == 'UT']
new_df = new_df[['Financial Institution State', 'Financial Institution Name', 'Total_Assets']]

pivot_df_031 = new_df.pivot_table(index='Financial Institution Name', values="Total_Assets").sort_values(by='Total_Assets', ascending=False)
pivot_df_0X1 = new_df.pivot_table(index='Financial Institution Name', values="Total_Assets").sort_values(by='Total_Assets', ascending=False)
print(pivot_df_0X1)
