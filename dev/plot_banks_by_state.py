import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file_15-20.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)

new_df = df.loc[(df['year'] == 2018) & (df['quarter'] == 3)]

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