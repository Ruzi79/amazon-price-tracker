# Amazon Price Tracker (Selenium)

This project demonstrates how to track product prices on Amazon using Python and Selenium.

The script extracts the **product title**, **price**, and **currency**, and displays them directly in the terminal.

---

## Features
- Extracts product title, price, and currency symbol
- Uses explicit waits to ensure elements are loaded
- Outputs results in terminal for verification
- Handles missing price gracefully

---

## Code and Explanation

```python
# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
Explanation: Imports Selenium WebDriver and supporting modules for automation, element selection, waiting for elements, and automatic ChromeDriver management.

python
Copy code
# Set up Chrome browser options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
Explanation: Configures Chrome options; headless mode runs the browser in the background and window size ensures elements render correctly.

python
Copy code
# Initialize WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
Explanation: Launches Chrome browser with the specified options; driver allows interacting with the browser.

python
Copy code
# Open the Amazon product page
driver.get("https://www.amazon.com/ARVEXO-Christmas-Birthday-Gifts-Women/dp/B0FGJDSB4Z")
wait = WebDriverWait(driver, 20)
Explanation: Navigates to the product page and sets up a 20-second explicit wait for elements to load.

python
Copy code
# Extract product title
product = wait.until(
    EC.presence_of_element_located((By.ID, "productTitle"))
).text.strip()
Explanation: Waits until the product title appears, then extracts and cleans the text.

python
Copy code
# Initialize price variable
price = "Price not found"
Explanation: Default value in case the price is not found.

python
Copy code
# Extract product price and currency
try:
    symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol").text
    whole = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
    price = f"{whole}.{fraction} {symbol}"
except:
    pass
Explanation: Amazon splits price into three elements:

a-price-symbol → currency symbol ($, ₼, €)

a-price-whole → whole number part

a-price-fraction → decimal part
These are combined to form a full price (e.g., 86.00 ₼). The try-except ensures the script does not crash if any part is missing.

python
Copy code
# Print product name and price
print("Product:", product)
print("Price:", price)
Explanation: Displays the product name and price with currency in the terminal.

python
Copy code
# Close the browser
driver.quit()
Explanation: Closes the browser and frees resources.
