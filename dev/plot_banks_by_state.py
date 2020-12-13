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

bank_count_relative = new_df['Financial Institution State'].value_counts(normalize=True)
bank_count_absolute = new_df['Financial Institution State'].value_counts()

ax1 = sns.barplot(x=bank_count_absolute.index, y=bank_count_absolute.values)
ax1.set_title("Absolute Number of Banks by state for the 3rd quarter of 2018")
ax1.set_ylabel('Number of Banks')
ax1.set_xlabel('States')

ax2 = sns.barplot(x=bank_count_relative.index, y=bank_count_relative.values)
ax2.set_title("Relative Number of Banks by state for the 3rd quarter of 2018")
ax2.set_ylabel('Number of Banks')
ax2.set_xlabel('States')