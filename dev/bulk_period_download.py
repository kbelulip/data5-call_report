from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import numpy as np
import os
import time
import glob
import zipfile


# Helper function to keep the browser open until the file has been downloaded
def download_wait(directory, timeout, nfiles=None):
    """
    Wait for downloads to finish with a specified timeout.

    Args
    ----
    directory : str
        The path to the folder where the files will be downloaded.
    timeout : int
        How many seconds to wait until timing out.
    nfiles : int, defaults to None
        If provided, also wait for the expected number of files.

    """
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True

        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True

        seconds += 1
    return seconds


path = os.path.dirname(__file__)
data_path = os.path.join(path, "..", "data")
download_path = os.path.join(path, "..", "..", "Downloads")
url = "https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx"
years = ["2020"]

for year in years:

    periods = ["03/31/" + year, "06/30/" + year, "09/30/" + year, "12/31/" + year]

    # Initialize the browser and call the url
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        selectProduct = Select(driver.find_element_by_id("ListBox1"))
        selectProduct.select_by_value("ReportingSeriesSinglePeriod")

        for period in periods:
            selectYear = Select(driver.find_element_by_id("DatesDropDownList"))
            selectYear.select_by_visible_text(period)

            driver.find_element_by_id("Download_0").click()

        driver.implicitly_wait(download_wait(download_path, 40))
    finally:
        driver.quit()

    # Get latest latest filename with path
    list_of_files = glob.glob(os.path.join(download_path, "*"))

    # Convert list to np array
    list_of_files = np.array(list_of_files)

    # Get latest latest filename with path
    list_of_files = sorted(glob.glob(os.path.join(download_path, "*.zip")))

    list_of_files = np.array(list_of_files)

    for file_path in list_of_files[0:5]:
        # Extract the filename from path
        file = os.path.basename(os.path.normpath(file_path))

        # Create destination path to move the file
        data_move_path = os.path.join(data_path, file)

        # Move the file from downloads directory to destination
        os.replace(file_path, data_move_path)

        # Unzip downloaded file
        z = zipfile.ZipFile(data_move_path)
        z.extractall(os.path.join(data_move_path, "..", "Call_Report_" + year))
        z.close()

        # Delete zipped file
        os.remove(data_move_path)
