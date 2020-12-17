import os
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import rcParams
import seaborn as sns
sns.set()
rcParams['figure.figsize'] = 10,6

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "..", "data", "master_cr_file.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)
df['period'] = pd.to_datetime(df['period'])

pivot_df = df.pivot_table(index='period',
                          values=['Total_Assets', 'Total_Liabilities', 'Total_Equity_Capital'])
plt.title('Average of different balance sheet items')
plt.plot(pivot_df.index, pivot_df.Total_Assets, '.-', label='Total Assets')
plt.plot(pivot_df.index, pivot_df.Total_Liabilities, '.-', label='Total Liabilities')
plt.plot(pivot_df.index, pivot_df.Total_Equity_Capital, '.-', label='Total Equity Capital')
plt.legend()
plt.xlabel('Year')
plt.ylabel('US Dollars in Thousands')
plt.xticks(pivot_df.index[::4], rotation=45)
plt.show()