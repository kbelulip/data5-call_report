import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file_15-20.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)

new_df = df.loc[(df['year'] == 2018) & (df['quarter'] == 3)]
description = new_df.describe()

pivot_df = new_df.pivot_table(index='Financial Institution State', values=['Total_Assets', 'Total_Liabilities',
                                                                           'Total_Equity_Capital'])
pivot_df = pivot_df.reset_index().sort_values(by='Total_Assets', ascending=False)

fig, ax = plt.subplots()

ax.barh(pivot_df['Financial Institution State'], pivot_df['Total_Assets'], align='center')
ax.set_yticks(pivot_df['Financial Institution State'])
ax.invert_yaxis()
ax.set_xlabel('Average Total Assets ($ in Thousands)')
ax.set_title('Average total assets per state for 41 and 51 Banks for the 3rd quarter of 2018')

plt.show()
print(new_df['Financial Institution State'].unique())
banks_with_state_0 = new_df.loc[new_df['Financial Institution State'] == '0 ']

banks_with_state_0 = banks_with_state_0[['Financial Institution State', 'Financial Institution Name', 'Financial Institution City']]

plt.show()
