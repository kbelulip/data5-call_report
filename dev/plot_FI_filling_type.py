import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file_15-20.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)

new_df = df.loc[(df['year'] == 2018) & (df['quarter'] == 3)]
different_types = new_df['Financial Institution Filing Type'].value_counts(normalize=True)

fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(x=different_types.values, labels=different_types.index, autopct='%1.1f%%', startangle=90)
ax.set_title(different_types.name)
legend = ["Bank with Domestic Offices Only and Total Assets Less than $5 Billion", "Bank With Domestic Offices Only", "Bank With Domestic and Foreign Offices"]
ax.legend(wedges, legend, title="Forms", loc="best", bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
plt.setp(texts, size=8, weight="bold")

plt.show()
