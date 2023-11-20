# Automated Login Script with Selenium

This Python script is designed to automate the process of logging into a website using Selenium, a popular web testing library. It reads login credentials from an Excel file, attempts to log in, and logs the results in a text file.

## Prerequisites

Before you can use this script, make sure you have the following installed:

- Python 3.x: You can download Python from the official website: https://www.python.org/downloads/

- Selenium: Install the Selenium Python package using pip:

pip install selenium


- Chrome WebDriver: You will need the Chrome WebDriver to run Selenium with Google Chrome. Download it from the official website: https://sites.google.com/chromium.org/driver/

- OpenPyXL: Install the OpenPyXL Python package to work with Excel files:

pip install openpyxl


## Usage

1. Clone this repository or download the script (`main.py`) to your local machine.

2. Prepare an Excel file containing login credentials in the following format:

Email/Username // Password
user1@example.com // password123
user2@example.com // secret_password


- Each line represents a login attempt.
- Separate the email/username and password with `//` (or spaces).

3. Modify the `excel_file_path` variable in `main.py` to point to your Excel file.

4. Set the path to your Chrome binary in the `chrome_options.binary_location` line in `main.py`.

5. Customize the script to handle successful and unsuccessful login attempts according to your specific website's behavior.

6. Run the script using the following command:

python main.py


The script will automate the login attempts and log the results in a text file called `login_log.txt`.

## Customization

- Customize the logic within the script to match your specific website's login behavior.

- Adjust the waiting times, login success conditions, and other parameters as needed.


Happy automating!
