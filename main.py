import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Disable INFO-level logging messages from the WebDriver
logging.getLogger('selenium.webdriver').setLevel(logging.WARNING)


# Path to your Excel file
excel_file_path = "YOUR FILE"

# Set Chrome options with the correct path to Chrome binary and run in headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Initialize the webdriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get('THE WEBSITE')

# Open the Excel file
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active  # You can specify a sheet by name if needed

# Iterate through all rows in the Excel file
for row_number, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
    # Check if the value in the B column (2nd column) is not empty and is "maison" (case-insensitive)
    if any(cell and cell.lower() == 'maison' for cell in row[1:2]):
        # Extract credentials from the G column (7th column)
        credentials = row[6]  # Adjust the column index if needed

        # Split the 'credentials' string into username and password (try both '//', ' ')
        if '//' in credentials:
            username, password = credentials.split('//')
        else:
            # Attempt to split using space if double slash is not found
            split_by_space = credentials.split()
            if len(split_by_space) == 2:
                username, password = split_by_space
            else:
                print(f"Invalid format in row {row_number}: {credentials}")
                continue

        # Wait for the username field to be present and interactable
        username_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, 'userfield'))
        )

        # Wait for the password field to be present and interactable
        password_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, 'passwordfield'))
        )

        # Fill in the username and password fields
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the form (replace with the actual form submission action)
        password_field.send_keys(Keys.RETURN)

        # Check if the login was successful or not while waiting
        for _ in range(40):
            if 'https://www.maprimerenov.gouv.fr' in driver.current_url:
                print(f"Successful login on row {row_number}")
                with open('login_log.txt', 'a') as log_file:
                    log_file.write(f"Successful login on row {row_number}\n")
                break
            elif 'Unsuccessful-login-url' in driver.current_url:
                print(f"Unsuccessful login on row {row_number}")
                with open('login_log.txt', 'a') as log_file:
                    log_file.write(f"Unsuccessful login on row {row_number}\n")
                break
            time.sleep(1)

        # Close the current browser window
        driver.close()

        # Open a new browser window and navigate to the login page
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('')

# Close the last browser window
driver.quit()
