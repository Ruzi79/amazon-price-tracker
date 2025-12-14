Explanation of Work

This Python script automates the task of scraping product information (specifically the product name and price) from an Amazon product page using Selenium. It runs in headless mode, meaning it does not open a visible browser window, which makes the script run more efficiently in an automated environment.

How the Script Works:

Importing Necessary Libraries:
The script starts by importing required libraries:

selenium.webdriver for browser automation.

webdriver_manager.chrome for automatically downloading the required ChromeDriver.

expected_conditions and WebDriverWait to ensure elements are fully loaded before interacting with them.

By for defining the methods to locate elements on the page (such as by ID, CLASS_NAME, etc.).

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


Setting Up Chrome Browser with Options:
The script configures Chrome to run in headless mode (without showing a browser window) for improved performance. It also defines the window size for consistency.

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Runs Chrome in headless mode
options.add_argument("--window-size=1920,1080")  # Defines browser window size


Launching the Browser:
The script uses Selenium WebDriver to launch Chrome with the specified options. It also uses ChromeDriverManager to ensure the correct ChromeDriver version is installed and used automatically.

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),  # Automatically installs ChromeDriver
    options=options  # Applies the specified Chrome options
)


Loading the Amazon Product Page:
Once the browser is set up, the script navigates to the provided Amazon product page using the get() method. In this case, the example product URL is hardcoded.

driver.get("https://www.amazon.com/ARVEXO-Christmas-Birthday-Gifts-Women/dp/B0FGJDSB4Z")


Waiting for Elements to Load:
Since Amazon pages are dynamically loaded with JavaScript, the script waits for the necessary elements (such as the product title) to appear on the page. This is done using WebDriverWait combined with expected_conditions to ensure the page is fully loaded before the script interacts with any elements.

wait = WebDriverWait(driver, 20)  # Wait for up to 20 seconds for elements to load
product = wait.until(
    EC.presence_of_element_located((By.ID, "productTitle"))
).text.strip()


Extracting Product Title and Price:

The product title is located using the ID productTitle and is extracted by calling .text.strip().

The script then tries to extract the price from the page by looking for specific CSS classes:

a-price-symbol: The currency symbol (e.g., "$").

a-price-whole: The whole part of the price.

a-price-fraction: The fractional part of the price.

If the price is found, it is formatted as a string and stored in the price variable. If the price cannot be found, the script will display "Price not found".

price = "Price not found"
try:
    symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol").text
    whole = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
    price = f"{whole}.{fraction} {symbol}"
except:
    pass


Output:
After retrieving the product title and price, the script prints them to the console.

print("Product:", product)
print("Price:", price)


The output will look something like this:

Product: ARVEXO Christmas Birthday Gifts for Women
Price: $19.99


Closing the Browser:
Once the necessary data has been extracted, the script gracefully closes the browser using the quit() method.

driver.quit()  # Closes the browser and ends the session
