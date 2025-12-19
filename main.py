import re                                  # For extracting numbers from text using regex
from datetime import datetime              # To get current date and time
from pathlib import Path                  # To handle file paths easily
import time                               # (ADDED) for retry loop timing

from selenium import webdriver            # Main Selenium WebDriver
from selenium.webdriver.common.by import By   # To locate elements (By.ID, By.CSS_SELECTOR, etc.)
from selenium.webdriver.chrome.options import Options  # Chrome browser options
from selenium.webdriver.support.ui import WebDriverWait  # To wait for elements to load
from selenium.webdriver.support import expected_conditions as EC  # Expected conditions for waits
from webdriver_manager.chrome import ChromeDriverManager  # Automatically manages ChromeDriver
from selenium.webdriver.chrome.service import Service     # ChromeDriver service
from selenium.common.exceptions import ElementClickInterceptedException  # (ADDED) click fallback


URL="https://www.amazon.com/ASUS-Swift-Gaming-Monitor-PG32UCDM/dp/B0CV26XVMD"   # Amazon product URL to track
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


# (ADDED) Keep clicking "Continue shopping" until product page is really open
def click_continue_shopping_until_open(d, max_wait=8):
    """
    If 'Continue shopping' appears, keep trying to click it (quick retries)
    until the product page is open (productTitle present) or timeout.
    """
    start = time.time()

    xpaths = [
        "//*[@id='continue-shopping']",
        "//a[normalize-space()='Continue shopping']",
        "//button[normalize-space()='Continue shopping']",
        "//input[@type='submit' and (contains(@value,'Continue shopping') or contains(@aria-label,'Continue shopping'))]",
    ]

    while time.time() - start < max_wait:
        # If product page is open, stop
        if d.find_elements(By.ID, "productTitle"):
            return True

        clicked_any = False

        for xp in xpaths:
            els = d.find_elements(By.XPATH, xp)  # immediate check (no long waits)
            if not els:
                continue

            el = els[0]
            try:
                d.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                el.click()
            except (ElementClickInterceptedException, Exception):
                d.execute_script("arguments[0].click();", el)

            clicked_any = True
            time.sleep(0.25)  # short pause for DOM refresh

        # If nothing to click, just wait a tiny bit and re-check
        time.sleep(0.25 if clicked_any else 0.35)

    return False


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

    # (ADDED) Click "Continue shopping" repeatedly until the product page is open
    click_continue_shopping_until_open(d, max_wait=8)

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

    print(f"Product: {title}\nPrice: {p} ({val})")  # Print product name and price

finally:
    d.quit()                               # Close the browser
