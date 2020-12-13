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
description = new_df.describe()

pivot_df = new_df.pivot_table(index='Financial Institution State', values=['RCFD2170', 'RCFD2930', 'RCFD2948',
                                                                           'RCFD3210', 'RCFN2200', 'RCON2170',
                                                                           'RCON2200',	'RCON2930',	'RCON2948'])
pivot_df = pivot_df.reset_index().sort_values(by='RCON2170', ascending=False)

fig, ax = plt.subplots()

ax.barh(pivot_df['Financial Institution State'], pivot_df['RCON2170'], align='center')
ax.set_yticks(pivot_df['Financial Institution State'])
ax.invert_yaxis()
ax.set_xlabel('Average Total Assets ($ in Thousands)')
ax.set_title('Average total assets per state for 41 and 51 Banks for the 3rd quarter of ' + year)

plt.show()
print(new_df['Financial Institution State'].unique())
banks_with_state_0 = new_df.loc[new_df['Financial Institution State'] == '0 ']

banks_with_state_0 = banks_with_state_0[['Financial Institution State', 'Financial Institution Name', 'Financial Institution City']]

plt.show()
