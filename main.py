# Import necessary modules from Selenium and WebDriver Manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = webdriver.ChromeOptions()
# Remove headless mode to see the browser window
# options.add_argument("--headless=new")  # Commented out this line so the browser will open
# Set window size to ensure proper rendering
options.add_argument("--window-size=1920,1080")

# Initialize the Chrome WebDriver with options and driver manager
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),  # Automatically install and manage ChromeDriver
    options=options  # Use the defined options
)

# Navigate to the specified Amazon product page
driver.get("https://www.amazon.com/Webesh-Ceramic-Enthusiasts-Cappuccino-3-42%C3%974-7%C3%974-7in/dp/B096F3VYPQ")

# Create a WebDriverWait object with a timeout of 20 seconds
wait = WebDriverWait(driver, 20)

# Wait for the product title to be loaded on the page and retrieve it
product = wait.until(
    EC.presence_of_element_located((By.ID, "productTitle"))  # Wait for the product title element to appear
).text.strip()  # Extract the text and remove leading/trailing whitespaces

# Initialize the price variable with a default message
price = "Price not found"

# Try to extract the product price from the page
try:
    # Find the currency symbol (e.g., $)
    symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol").text
    # Find the whole part of the price (e.g., 25)
    whole = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    # Find the fractional part of the price (e.g., .99)
    fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
    # Combine the whole and fractional parts with the currency symbol to form the complete price
    price = f"{whole}.{fraction} {symbol}"
except:
    # If any of the elements are not found, the price will remain as "Price not found"
    pass

# Print the extracted product title and price to the console
print("Product:", product)
print("Price:", price)

# Close the browser once the task is complete
driver.quit()
