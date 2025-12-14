from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://www.amazon.com/ARVEXO-Christmas-Birthday-Gifts-Women/dp/B0FGJDSB4Z")

wait = WebDriverWait(driver, 20)

product = wait.until(
    EC.presence_of_element_located((By.ID, "productTitle"))
).text.strip()

price = "Price not found"

try:
    symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol").text
    whole = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
    price = f"{whole}.{fraction} {symbol}"
except:
    pass

print("Product:", product)
print("Price:", price)

driver.quit()
