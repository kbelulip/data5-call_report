import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)

new_df_2007 = df.loc[(df['year'] == 2007) & (df['quarter'] == 3)]
new_df_2018 = df.loc[(df['year'] == 2018) & (df['quarter'] == 3)]

#bank_count_relative = new_df['State'].value_counts(normalize=True)
bank_count_2007 = new_df_2007['State'].value_counts()
bank_count_2018 = new_df_2018['State'].value_counts()

bank_count_2018.name = "2018"
bank_count_2007.name = "2007"

final_df = pd.concat([bank_count_2007, bank_count_2018], axis=1, sort=True)
final_df['state'] = final_df.index
final_df.reset_index()
print(final_df)
#df_tr = final_df.T

