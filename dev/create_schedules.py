import os
import pandas as pd
from schedules import schedules

year = "2019"
path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data", "Call_Report_"+year, "Complete_Annual_Call_Report.txt")

whole_call_report = pd.read_csv(data_path, sep='\t', low_memory=False)

for x in schedules["schedule"]:
    new_schedule = whole_call_report[x["columns"]]
    print(new_schedule.head())