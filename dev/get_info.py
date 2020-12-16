import os
import pandas as pd

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file.txt")

df = pd.read_csv(data_path, sep='\t', low_memory=False)

columns = df.columns.tolist()
described_df = df.describe()

print(columns)
print(described_df)
print(df.info())
