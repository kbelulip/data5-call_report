import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)

new_df1 = df.loc[(df['year'] == 2018) & (df['quarter'] == 3)]
bank_count1 = new_df1['State'].value_counts()
ax1 = sns.barplot(x=bank_count1.index, y=bank_count1.values)
ax1.set_title("Absolute number of banks by state for the 3rd quarter of 2018")
ax1.set_ylabel('Number of banks')
ax1.set_xlabel('States')

new_df2 = df.loc[(df['year'] == 2007) & (df['quarter'] == 3)]
bank_count2 = new_df2['State'].value_counts()
ax2 = sns.barplot(x=bank_count2.index, y=bank_count2.values)
ax2.set_title("Absolute number of banks by state for the 3rd quarter of 2007")
ax2.set_ylabel('Number of banks')
ax2.set_xlabel('States')
