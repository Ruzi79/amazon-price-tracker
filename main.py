import re                                  # For extracting numbers from text using regex
from datetime import datetime              # To get current date and time
from pathlib import Path                  # To handle file paths easily
from selenium import webdriver            # Main Selenium WebDriver
from selenium.webdriver.common.by import By   # To locate elements (By.ID, By.CSS_SELECTOR, etc.)
from selenium.webdriver.chrome.options import Options  # Chrome browser options
from selenium.webdriver.support.ui import WebDriverWait  # To wait for elements to load
from selenium.webdriver.support import expected_conditions as EC  # Expected conditions for waits
from webdriver_manager.chrome import ChromeDriverManager  # Automatically manages ChromeDriver
from selenium.webdriver.chrome.service import Service     # ChromeDriver service

URL="https://www.amazon.com/dp/B0DHZ65KSJ"   # Amazon product URL to track
HEADLESS=False                              # If True, Chrome runs in background

def f(d, css):
    try:
        return d.find_element(By.CSS_SELECTOR, css).text.strip()  # Try to get text from element
    except:
        return ""                          # Return empty string if element not found

def price_to_float(t):
    m = re.findall(r"[\d\.,]+", t or "")   # Extract numeric part of the price
    if not m:
        return None                        # If no number found, return None
    s = m[0]                               # Take the first matched number
    # Handle European number format (e.g. 1.299,99)
    s = s.replace(".","").replace(",",".") if (
        s.count(",")==1 and s.count(".")>=1 and s.rfind(",")>s.rfind(".")
    ) else s.replace(",","")               # Otherwise handle US format (e.g. 1,299.99)
    try:
        return float(s)                    # Convert cleaned string to float
    except:
        return None                        # Return None if conversion fails

o = Options()                              # Create Chrome options object
if HEADLESS:
    o.add_argument("--headless=new")       # Enable headless mode if needed
o.add_argument("--window-size=1400,900")  # Set browser window size
o.add_argument("--disable-blink-features=AutomationControlled")  # Reduce bot detection

# Start Chrome WebDriver with automatic driver management
d = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=o
)

try:
    d.get(URL)                             # Open the Amazon product page
    WebDriverWait(d,20).until(             # Wait until product title is loaded
        EC.presence_of_element_located((By.ID,"productTitle"))
    )

    title = d.find_element(By.ID,"productTitle").text.strip()  # Get product title

    # Try to get price from common Amazon price locations
    p = (
        f(d,"span.a-price span.a-offscreen") or
        f(d,"#corePriceDisplay_desktop_feature_div span.a-price span.a-offscreen")
    )

    if not p:                              # If price text not found
        whole = f(d,"span.a-price-whole")  # Get whole part of price
        frac  = f(d,"span.a-price-fraction")  # Get fractional part
        # Combine whole and fraction parts if available
        p = (whole.replace(".","") + ("."+frac if frac else "")) if whole else ""

    val = price_to_float(p)                # Convert price text to numeric value

    Path("data/screenshots").mkdir(parents=True, exist_ok=True)  # Create screenshots folder
    d.save_screenshot(                     # Save screenshot of the page
        f"data/screenshots/amazon_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    )

    print(f"Məhsul: {title}\nQiymət: {p} ({val})")  # Print product name and price

finally:
    d.quit()                               # Close the browser
