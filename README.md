# Explanation of the Script:

This Python script is designed to scrape product information, specifically the product name and price, from an Amazon product page using Selenium. Selenium automates the web browser to retrieve data, making it a powerful tool for web scraping tasks.

# How the Script Works:

Setting Up the Browser with Selenium:

The script starts by setting up Selenium WebDriver for Chrome, configuring it to run in headless mode (without a graphical interface). This makes it faster and more efficient for automated tasks.

The window size is explicitly set to ensure the page renders correctly for consistent scraping.

Navigating to the Product Page:

Using driver.get("URL"), the script opens a specific Amazon product page. You can easily change the URL to scrape data for different products.

Waiting for Page Elements to Load:

The script uses explicit waits with WebDriverWait and expected_conditions to ensure that elements, such as the product title, have fully loaded before the script proceeds. This prevents errors that may occur if the script attempts to scrape data from elements that aren't yet visible.

Extracting Product Information:

The script extracts the product title by looking for an element with the ID productTitle, which contains the name of the product.

It then looks for the price information by searching for multiple elements:

a-price-symbol: Contains the currency symbol (e.g., $).

a-price-whole: Contains the whole number part of the price (e.g., 25).

a-price-fraction: Contains the fractional part of the price (e.g., .99).

If the price information is found, the script combines these parts into a complete price string (e.g., 25.99 $).

Handling Missing Data:

If the price or product title cannot be found, the script gracefully handles this by returning a default message, such as "Price not found".

Printing the Data:

After extracting the product name and price, the script prints this information to the console, providing a clear output.

Closing the Browser:

After the data has been collected, the script closes the browser with driver.quit() to free up system resources.
