import os
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import rcParams
import seaborn as sns
sns.set()
rcParams['figure.figsize'] = 10,6

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)
df['period'] = pd.to_datetime(df['period'])

pivot_df = df.pivot_table(index='period',
                          values=['Equity_Ratio', 'Leverage_Ratio', 'Return_on_Assets', 'year'])
plt.title('Average of different ratios over time')
plt.plot(pivot_df.index, pivot_df.Equity_Ratio, '.-', label='Equity Ratio')
plt.plot(pivot_df.index, pivot_df.Leverage_Ratio, '.-', label='Leverage Ratio')
plt.plot(pivot_df.index, pivot_df.Return_on_Assets, '.-', label='Return on Assets')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Ratio')
plt.xticks(pivot_df.index[::4], rotation=45)
plt.show()

