import os
import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URLS = [
    "https://shop.amul.com/en/product/amul-high-protein-plain-lassi-200-ml-or-pack-of-30",
    "https://shop.amul.com/en/product/amul-high-protein-buttermilk-200-ml-or-pack-of-30",
    "https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30",
    "https://shop.amul.com/en/product/amul-high-protein-paneer-400-g-or-pack-of-24",
    "https://shop.amul.com/en/product/amul-high-protein-paneer-400-g-or-pack-of-2",
    "https://shop.amul.com/en/product/amul-high-protein-milk-250-ml-or-pack-of-8"
]

EMAIL_USERNAME = os.environ['EMAIL_USERNAME']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
TO_EMAIL = os.environ['TO_EMAIL']

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; AmulBot/1.0; +https://github.com/singhharsh77/AMUL_CronJob)'
}

KEYWORDS = ["add to cart", "add-to-cart", "buy now", "addtocart"]

def check_stock(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for button in soup.find_all("a", class_="add-to-cart"):
            # Check for 'disabled' in attributes AND class
            is_disabled_attr = button.has_attr("disabled")
            # Some sites might set disabled="true", "1", blank, etc.—treat all as disabled
            disabled_value = button.get("disabled", "").lower()
            in_class_disabled = "disabled" in button.get("class", [])
            if not is_disabled_attr and not in_class_disabled:
                # Button is enabled (order allowed)
                print(f"Enabled Add to Cart found at {url}")
                return True
            elif disabled_value in ["false", "0"]:
                # Sometimes disabled="false" or "0" means enabled!
                print(f"Potentially enabled Add to Cart found at {url}")
                return True
        return False
    except Exception as e:
        print(f"❌ Error checking {url}: {e}")
        return False


def send_batch_email(in_stock_urls):
    subject = "Amul Products In Stock!"
    body_lines = ["The following products are now in stock:"]
    for url in in_stock_urls:
        body_lines.append(url)
    body = "\n".join(body_lines)
    message = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_USERNAME, TO_EMAIL, message)
        print(f"✅ Batch email sent for {len(in_stock_urls)} products.")
    except Exception as e:
        print(f"❌ Failed to send batch email: {e}")

def main():
    in_stock = []
    for url in PRODUCT_URLS:
        if check_stock(url):
            print(f"✅ In stock: {url}")
            in_stock.append(url)
        else:
            print(f"❌ Not in stock: {url}")
    if in_stock:
        send_batch_email(in_stock)
    else:
        print("No products in stock this cycle.")

if __name__ == "__main__":
    main()
