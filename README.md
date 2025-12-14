# ----------------------------------------------------------
# Amazon Price Tracker using Selenium
# ----------------------------------------------------------
# This script tracks the price of a specific product on Amazon.
# It extracts the product's name, price, and currency symbol and prints them in the terminal.
# The script uses Selenium WebDriver with explicit waits to handle dynamic content.
# It also handles missing price elements gracefully.
# ----------------------------------------------------------

# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Explanation:
# - webdriver: Used to automate browser actions.
# - By: Provides methods to locate elements on the page.
# - Service: Helps manage ChromeDriver service.
# - WebDriverWait and expected_conditions: Wait for elements to load dynamically.
# - webdriver_manager: Automatically downloads and manages ChromeDriver.

# Set up Chrome browser options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Run Chrome in background without opening window
options.add_argument("--window-size=1920,1080")  # Set window size to ensure proper rendering

# Explanation:
# Headless mode allows the script to run without displaying the browser.
# Window size ensures that all page elements are correctly loaded and visible for Selenium.

# Initialize WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Explanation:
# Launch Chrome browser with the specified options.
# The 'driver' object allows interacting with the browser (opening URLs, finding elements, etc.)

# Open the Amazon product page
driver.get("https://www.amazon.com/ARVEXO-Christmas-Birthday-Gifts-Women/dp/B0FGJDSB4Z")
wait = WebDriverWait(driver, 20)

# Explanation:
# Navigate to the product page.
# WebDriverWait is set to 20 seconds to wait for elements to appear.
# Explicit waits ensure the code doesn't fail if elements take time to load.

# Extract product title
product = wait.until(
    EC.presence_of_element_located((By.ID, "productTitle"))
).text.strip()

# Explanation:
# Waits until the product title element is present on the page.
# .text extracts the text from the element.
# .strip() removes any leading or trailing whitespace.
# Ensures a clean product name is obtained.

# Initialize price variable
price = "Price not found"

# Explanation:
# Set a default value in case the price is not found.
# This prevents the script from crashing if price elements are missing.

# Extract product price and currency
try:
    symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol").text
    whole = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
    price = f"{whole}.{fraction} {symbol}"
except:
    pass

# Explanation:
# Amazon splits price into three separate HTML elements:
# 1. 'a-price-symbol' -> currency symbol (e.g., $, ₼, €)
# 2. 'a-price-whole' -> whole number part of the price (e.g., 86)
# 3. 'a-price-fraction' -> fractional part of the price (after decimal, e.g., 00)
# These are combined into a single string to form a complete price like "86.00 ₼".
# The try-except block ensures the script doesn't crash if any part is missing.

# Print product name and price
print("Product:", product)
print("Price:", price)

# Explanation:
# Displays the product name and full price with currency in the terminal.
# Terminal output can be used for lab verification.

# Close the browser
driver.quit()

# Explanation:
# Properly closes the Chrome browser and frees system resources.
# Important to prevent memory leaks or leftover browser processes.

