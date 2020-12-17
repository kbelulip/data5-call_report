import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)
df['period'] = pd.to_datetime(df['period'])

pivot_df = df.pivot_table(index=['year', 'Filing_Type'],
                          values=['IDRSSD'],
                          aggfunc=pd.Series.nunique)
nex_df = pivot_df.reset_index()
nex_df = nex_df.set_index(['year', 'Filing_Type'])

nex_df.unstack().plot(kind='bar', stacked=True)
plt.xlabel('Year')
plt.ylabel('Number of Banks')
plt.legend(['31', '41', '51'], title="Filing Type")
plt.title('Share of different kind of banks')
plt.xticks(pivot_df.index, rotation=45)
plt.show()