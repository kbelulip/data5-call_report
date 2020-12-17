import pandas as pd
import os
from datetime import datetime

path = os.path.dirname(__file__)

years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020"]
quarters = ["0331", "0630", "0930", "1231"]
concat_column = ["IDRSSD"]
por_columns = ["FDIC Certificate Number", "OTS Docket Number", "Primary ABA Routing Number",
               "Financial Institution Name", "Financial Institution City", "Financial Institution State",
               "Financial Institution Filing Type"]
rc_columns = ["RCFD2170", "RCFD2948", "RCFDG105", "RCON2170", "RCON2948", "RCONG105"]
ri_columns = ["RIAD4340", "RIAD4107", "RIAD4073", "RIAD4079", "RIAD4093"]
rcr_columns = ["RCFA7204", "RCFA7205", "RCOA7204", "RCOA7205"]
new_columns = ["period", "year", "quarter"]

master_df = pd.DataFrame(columns=concat_column + por_columns + rc_columns + ri_columns + rcr_columns + new_columns)

for year in years:
    year_data_path = os.path.join(path, "..", "data", "Call_Report_" + year)
    print(year)

    for index, quarter in enumerate(quarters):

        if (year == "2020") and (quarter == "1231"):
            continue

        datetimeobject = datetime.strptime(quarter + year, '%m%d%Y')

        por_file_path = os.path.join(year_data_path, "FFIEC CDR Call Bulk POR " + quarter + year + ".txt")
        rc_file_path = os.path.join(year_data_path, "FFIEC CDR Call Schedule RC " + quarter + year + ".txt")
        ri_file_path = os.path.join(year_data_path, "FFIEC CDR Call Schedule RI " + quarter + year + ".txt")
        rcr_file_path = os.path.join(year_data_path, "FFIEC CDR Call Schedule RCRI " + quarter + year + ".txt")

        df_por = pd.read_csv(por_file_path, sep='\t', usecols=concat_column + por_columns, low_memory=False)
        df_rc = pd.read_csv(rc_file_path, sep='\t', low_memory=False, usecols=concat_column + rc_columns, skiprows=[1])
        df_ri = pd.read_csv(ri_file_path, sep='\t', low_memory=False, usecols=concat_column + ri_columns, skiprows=[1])
        df_rcr = pd.read_csv(rcr_file_path, sep='\t', low_memory=False, usecols=concat_column + rcr_columns, skiprows=[1])

        buffer_df = pd.merge(df_por, df_rc, how='inner', on='IDRSSD')
        buffer_df = pd.merge(buffer_df, df_ri, how='inner', on='IDRSSD')
        buffer_df = pd.merge(buffer_df, df_rcr, how='inner', on='IDRSSD')

        buffer_df[new_columns[0]] = datetimeobject.strftime('%Y-%m-%d')
        buffer_df[new_columns[1]] = year
        buffer_df[new_columns[2]] = index+1

        master_df = pd.concat([master_df, buffer_df], ignore_index=True, sort=True)


master_df['RCFD_Return_on_Assets'] = master_df.apply(lambda x: x['RCFD2170'] if x['RCFD2170'] < 1 else x['RIAD4340'] / x['RCFD2170'], axis=1)
master_df['RCON_Return_on_Assets'] = master_df.apply(lambda x: x['RCON2170'] if x['RCON2170'] < 1 else x['RIAD4340'] / x['RCON2170'], axis=1)
master_df['RCFD_Equity_Ratio'] = master_df.apply(lambda x: x['RCFD2170'] if x['RCFD2170'] < 1 else x['RCFDG105'] / x['RCFD2170'], axis=1)
master_df['RCON_Equity_Ratio'] = master_df.apply(lambda x: x['RCON2170'] if x['RCON2170'] < 1 else x['RCONG105'] / x['RCON2170'], axis=1)

master_df['RCFD_Return_on_Assets'].fillna(master_df['RCON_Return_on_Assets'], inplace=True)
master_df['RCFD_Equity_Ratio'].fillna(master_df['RCON_Equity_Ratio'], inplace=True)
master_df['RCFD2170'].fillna(master_df['RCON2170'], inplace=True)
master_df['RCFD2948'].fillna(master_df['RCON2948'], inplace=True)
master_df['RCFDG105'].fillna(master_df['RCONG105'], inplace=True)
master_df['RCFA7204'].fillna(master_df['RCOA7204'], inplace=True)
master_df['RCFA7205'].fillna(master_df['RCOA7205'], inplace=True)


master_df.drop(['RCON_Return_on_Assets', 'RCON_Equity_Ratio', 'RCON2170', 'RCON2948', 'RCONG105', 'RCOA7204', 'RCOA7205'],
               axis=1, inplace=True)
master_df.rename(columns={'RCFD_Return_on_Assets': 'Return_on_Assets', 'RCFD_Equity_Ratio': 'Equity_Ratio',
                          'RCFD2170': 'Total_Assets', 'RCFD2948': 'Total_Liabilities', 'RCFDG105': 'Total_Equity_Capital',
                          'RCFA7204': 'Leverage_Ratio', 'RCFA7205': 'Total_Capital_Ratio', 'RIAD4340': 'Net_Income',
                          'RIAD4107': 'Total_Interest_Income', 'RIAD4073': 'Total_Interest_Expense',
                          'RIAD4079': 'Total_Noninterest_Income', 'RIAD4093': 'Total_Noninterest_Expense'},
                 inplace=True)


master_data_path = os.path.join(path, "..", "data", "master_cr_file_14-20.txt")
master_df.to_csv(master_data_path, sep='\t', index=False)