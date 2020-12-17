import os
import pandas as pd

path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "master_cr_file.txt")
df = pd.read_csv(data_path, sep='\t', low_memory=False)

# Fill missing Values wit 0
df['Total_Capital_Ratio'] = df['Total_Capital_Ratio'].fillna("0")
df['Leverage_Ratio'] = df['Leverage_Ratio'].fillna("0")

# Due to changed data format, some rows where falsly formated
# Remove of % and division with 100
# for Leverage Ratio
df.loc[df['Leverage_Ratio'].str.contains('%'), 'Leverage_Ratio'] = df['Leverage_Ratio'].loc[df['Leverage_Ratio'].str.contains('%')].str.replace('%', '').astype(float) / 100
df['Leverage_Ratio'] = df['Leverage_Ratio'].astype(float)

# and Total Capital Ratio
df.loc[df['Total_Capital_Ratio'].str.contains('%'), 'Total_Capital_Ratio'] = df['Total_Capital_Ratio'].loc[df['Total_Capital_Ratio'].str.contains('%')].str.replace('%', '').astype(float) / 100
df['Total_Capital_Ratio'] = df['Total_Capital_Ratio'].astype(float)

df.to_csv(data_path, sep='\t', index=False)