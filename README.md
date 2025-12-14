from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
selenium: Used for automating interactions with web pages.

By: Defines various methods for finding elements (such as ID, CLASS_NAME, etc.).

Service: Used to launch the Chrome browser through Selenium.

WebDriverWait: Waits for an element to load before proceeding (ensures the page is fully loaded).

expected_conditions: Waits for specific conditions to be met, such as checking if an element is present (e.g., presence_of_element_located).

ChromeDriverManager: Helps in automatically finding the correct driver for Chrome.

Creating the Chrome Browser:
python
Copy code
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Runs browser without a graphical interface, headless mode
options.add_argument("--window-size=1920,1080")  # Defines the size of the browser window

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),  # Installs ChromeDriver automatically
    options=options  # Applies the specified options (headless mode, etc.)
)
ChromeOptions(): This object allows you to configure the Chrome browser settings.

headless mode: Ensures the script runs without opening a visible browser window, making the process faster.

window-size=1920,1080: Sets the size of the browser window.

webdriver.Chrome(): Launches the Chrome browser with the specified configurations.

Loading the Amazon Product Page:
python
Copy code
driver.get("https://www.amazon.com/ARVEXO-Christmas-Birthday-Gifts-Women/dp/B0FGJDSB4Z")
get(): Directs the browser to the specified URL. In this case, it opens an Amazon product page.

Waiting for Elements to Load (Explicit Wait):
python
Copy code
wait = WebDriverWait(driver, 20)  # Waits for a maximum of 20 seconds

product = wait.until(
    EC.presence_of_element_located((By.ID, "productTitle"))
).text.strip()
WebDriverWait: Waits for a specific element to be present on the page.

presence_of_element_located: Checks if an element with the specified ID (in this case, "productTitle") is present.

.text.strip(): Retrieves the text of the element and removes any leading or trailing whitespace.

Finding the Price (with Error Handling):
python
Copy code
price = "Price not found"

try:
    symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol").text
    whole = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
    price = f"{whole}.{fraction} {symbol}"
except:
    pass
find_element(By.CLASS_NAME, "a-price-symbol"): This code is used to find the currency symbol (e.g., "$").

find_element(By.CLASS_NAME, "a-price-whole"): Retrieves the whole part of the price.

find_element(By.CLASS_NAME, "a-price-fraction"): Retrieves the fractional part of the price.

f"{whole}.{fraction} {symbol}": Combines the whole part, fractional part, and symbol into the complete price.

try...except: If any of the price elements are not found, the script handles the error without breaking and sets Price not found as the result.

Printing the Final Results:
python
Copy code
print("Product:", product)
print("Price:", price)
This part prints the product name and its price to the console.

Closing the Browser:
python
Copy code
driver.quit()  # Closes the browser
quit(): Closes the browser and completes the operation.

