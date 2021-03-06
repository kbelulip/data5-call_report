from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import glob
import zipfile
from helper_fct import download_wait


path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "..", "data")
download_path = os.path.join(path, "..", "..", "..", "Downloads")
url = "https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx"
year = "2019"

# Initialize the browser and call the url
driver = webdriver.Chrome()
driver.get(url)

try:
    element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.TAG_NAME, "form")))

    selectProduct = Select(driver.find_element_by_id("ListBox1"))
    selectProduct.select_by_value("ReportingSeriesSubsetSchedulesFourPeriods")

    selectYear = Select(driver.find_element_by_id("DatesDropDownList"))
    selectYear.select_by_visible_text(year)

    driver.find_element_by_id("Download_0").click()
    driver.implicitly_wait(download_wait(download_path, 40))

finally:
    driver.quit()

# Get latest latest filename with path
list_of_files = glob.glob(os.path.join(download_path, "*"))
latest_file_path = max(list_of_files, key=os.path.getctime)

# Extract the filename from path
file = os.path.basename(os.path.normpath(latest_file_path))

# Create destination path to move the file
data_move_path = os.path.join(data_path, file)

# Move the file from downloads directory to destination
os.replace(latest_file_path, data_move_path)

# Unzip downloaded file
z = zipfile.ZipFile(data_move_path)
z.extractall(os.path.join(data_move_path, "..", "Call_Report_"+year))
z.close()

# Delete zipped file
os.remove(data_move_path)