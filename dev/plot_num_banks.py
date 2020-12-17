import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)
df['period'] = pd.to_datetime(df['period'])

number_banks = df.pivot_table(index='year', values=['IDRSSD'], aggfunc=pd.Series.nunique)

plt.title('Total number of banks')
plt.bar(number_banks.index, number_banks.IDRSSD)
plt.xlabel('Year')
plt.ylabel('Number of Banks')
plt.xticks(number_banks.index, rotation=45)
plt.show()