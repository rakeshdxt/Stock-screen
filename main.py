import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

def run_human_scraper():
    # 1. Setup Chrome for the Cloud (Headless)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)

    # 2. Stealth: Make the cloud bot look like a real person
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    try:
        # 3. Visit the URL (Replace with your Screen URL)
        print("Opening Screener.in...")
        driver.get("https://www.screener.in/screens/YOUR_SCREEN_ID_HERE/")
        
        # Human Pause: Thinking time
        time.sleep(random.uniform(4, 8))

        # 4. Slow Reading: Mimicking a human scrolling
        print("Reading data at human speed...")
        for i in range(3):
            scroll_dist = random.randint(300, 600)
            driver.execute_script(f"window.scrollBy(0, {scroll_dist});")
            time.sleep(random.uniform(2, 5)) # Pause to "read"

        # 5. Extract Table
        table_element = driver.find_element("css selector", "table.data-table")
        table_html = table_element.get_attribute('outerHTML')
        
        # Convert to CSV using Pandas
        df = pd.read_html(table_html)[0]
        df.to_csv("rsd_latest_data.csv", index=False)
        print("Success: Data saved to rsd_latest_data.csv")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_human_scraper()
