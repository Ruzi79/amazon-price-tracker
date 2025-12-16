# Amazon Product Price Tracker

This Python script is designed to track product prices on Amazon product pages over time. Using Selenium WebDriver, it automates opening a product page, extracts the product price, and monitors any changes in the price. This is useful for tracking price drops or changes for your favorite products.

# Explanation of the Script:
Setting Up the Browser with Selenium:

The script sets up Selenium WebDriver for Chrome and opens the browser window.

The window size is explicitly set to ensure the page renders correctly for consistent price tracking.

Navigating to the Product Page:

The script navigates to a specific Amazon product page using driver.get("URL"). This can be customized to track different products by changing the URL.

Tracking Price Changes:

The script tracks the product price by scraping it each time it runs.

Price information is extracted using the elements:

a-price-symbol: Currency symbol (e.g., $).

a-price-whole: The whole number part of the price (e.g., 25).

a-price-fraction: The fractional part of the price (e.g., .99).

The script saves the current price and can compare it with previous prices to track changes over time.

Handling Missing Data:

If the price cannot be found, the script will print a message like "Price not found" and exit gracefully without crashing.

Tracking and Saving Data:

Prices can be saved to a local file or database for future tracking.

Optionally, you can set up the script to send an email or a notification when the price drops.

Printing the Data:

The script prints the product name, current price, and any changes since the last check to the console.

Closing the Browser:

After the tracking is done, the script closes the browser window with driver.quit() to free up resources.
