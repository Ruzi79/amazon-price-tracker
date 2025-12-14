Amazon Price Tracker

This script uses Selenium to scrape product information (product name and price) from an Amazon product page. It is designed to run in headless mode, meaning it doesn't open a visible browser window, making it faster and more efficient for automation tasks.

Requirements

Before running the script, make sure you have the following libraries installed:

selenium

webdriver_manager

You can install these using pip:

pip install selenium webdriver-manager

How the Script Works

Setup Chrome Browser:
The script uses Selenium with Chrome in headless mode, so it does not open a visible browser window.

ChromeOptions(): Configures Chrome to run in headless mode and defines the window size.

ChromeDriverManager: Automatically downloads and installs the correct ChromeDriver.

Access Amazon Product Page:
The script loads the product page URL using driver.get().

Wait for Elements:
It waits for the product title and price to be loaded on the page using WebDriverWait and expected_conditions.

Extract Product Information:

Product Name: Extracted using the productTitle ID.

Price: Extracted using CSS classes (a-price-symbol, a-price-whole, a-price-fraction) to get the symbol, whole part, and fractional part of the price.

Output:
The product name and price are printed to the console.

Close Browser:
Once the task is completed, the browser is closed using driver.quit().

Usage

Clone or download this repository.

Install the required libraries using pip install as mentioned above.

Run the script with the URL of the Amazon product you want to track. You can replace the sample URL in the script with any Amazon product page link.

driver.get("https://www.amazon.com/ARVEXO-Christmas-Birthday-Gifts-Women/dp/B0FGJDSB4Z")


The script will output the product name and its price in the terminal.

Example output:

Product: ARVEXO Christmas Birthday Gifts for Women
Price: $19.99

Code Explanation

Selenium WebDriver: Automates browser interactions.

WebDriverWait: Waits for elements to be present on the page before interacting with them.

Error Handling: If the price is not found, the script handles the exception and prints "Price not found"
